import { useEffect, useRef, useState } from "react";
import { Link, useLocation, useParams } from "react-router-dom";

import { ApiError, api, type Lesson, type Objective } from "../lib/api";

interface LessonNavState {
  chapterId?: number;
  chapterTitle?: string;
  topicId?: number;
  topicTitle?: string;
}

export default function LessonPage() {
  const { lessonId } = useParams();
  const id = Number(lessonId);
  const location = useLocation();
  const navState = (location.state as LessonNavState | null) ?? null;

  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [objectives, setObjectives] = useState<Objective[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [completed, setCompleted] = useState(false);
  const [saving, setSaving] = useState(false);
  const startedAt = useRef(Date.now());

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError(null);
    setCompleted(false);
    startedAt.current = Date.now();

    (async () => {
      try {
        const [lessonData, objectiveData] = await Promise.all([api.lesson(id), api.objectives(id)]);
        if (!active) return;
        setLesson(lessonData);
        setObjectives(objectiveData);
        // Opening a lesson is progress; failures here must not block reading.
        api.recordLessonProgress(id, "opened").catch(() => undefined);
      } catch (err) {
        if (!active) return;
        setError(
          err instanceof ApiError ? err.message : "Could not load this lesson. Please try again.",
        );
      } finally {
        if (active) setLoading(false);
      }
    })();

    return () => {
      active = false;
    };
  }, [id]);

  async function markComplete() {
    setSaving(true);
    try {
      const seconds = Math.round((Date.now() - startedAt.current) / 1000);
      await api.recordLessonProgress(id, "completed", Math.min(seconds, 36_000));
      setCompleted(true);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not save your progress.");
    } finally {
      setSaving(false);
    }
  }

  if (loading) {
    return (
      <div className="container">
        <div className="loader">
          <div className="spinner" />
          <span>Opening lesson…</span>
        </div>
      </div>
    );
  }

  if (error && !lesson) {
    return (
      <div className="container-narrow">
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
        <p>
          <Link to="/curriculum">← Back to curriculum</Link>
        </p>
      </div>
    );
  }

  const paragraphs = (lesson?.body_kn ?? "").split(/\n{2,}/).filter(Boolean);
  const tutorHref = `/tutor?${new URLSearchParams({
    ...(navState?.chapterId ? { chapter: String(navState.chapterId) } : {}),
    ...(navState?.topicId ? { topic: String(navState.topicId) } : {}),
    lesson: String(id),
    ...(navState?.chapterTitle ? { title: navState.chapterTitle } : {}),
  }).toString()}`;

  return (
    <div className="container-narrow stack">
      <div className="crumb">
        <Link to="/curriculum">Curriculum</Link>
        {navState?.chapterTitle ? <span>› {navState.chapterTitle}</span> : null}
        {navState?.topicTitle ? <span>› {navState.topicTitle}</span> : null}
      </div>

      <article className="card">
        <div className="row-between">
          <div>
            <span className="eyebrow">Lesson</span>
            <h1 style={{ fontSize: "1.75rem", marginBottom: "0.2rem" }} className="kan">
              {navState?.topicTitle ?? "ಪಾಠ"}
            </h1>
            <small>
              {navState?.chapterTitle ? `${navState.chapterTitle} · ` : ""}
              {lesson?.is_sample ? "Sample content" : "Curriculum content"}
            </small>
          </div>
          {completed ? <span className="badge badge-ok">✓ Completed</span> : null}
        </div>

        {error ? (
          <div className="alert alert-danger" role="alert" style={{ marginTop: "0.9rem" }}>
            {error}
          </div>
        ) : null}

        {objectives.length ? (
          <div className="card card-tight" style={{ marginTop: "1rem", background: "var(--surface-soft)" }}>
            <strong style={{ fontSize: "0.85rem" }}>What you will learn</strong>
            <ul className="list-plain kan" style={{ marginTop: "0.4rem" }}>
              {objectives.map((objective) => (
                <li key={objective.id}>• {objective.text_kn}</li>
              ))}
            </ul>
          </div>
        ) : null}

        <div className="lesson-body kan" lang="kn" style={{ marginTop: "1.1rem" }}>
          {paragraphs.map((paragraph, index) => (
            <p key={index}>{paragraph}</p>
          ))}
        </div>

        {lesson?.key_terms?.length ? (
          <section style={{ marginTop: "1rem" }}>
            <h3>Key terms · ಮುಖ್ಯ ಪದಗಳು</h3>
            <div className="grid grid-2">
              {lesson.key_terms.map((term) => (
                <div className="term" key={`${term.kn}-${term.en}`}>
                  <strong className="kan">{term.kn}</strong>
                  <small>{term.en}</small>
                  <span className="kan" style={{ fontSize: "0.9rem" }}>
                    {term.meaning_kn}
                  </span>
                </div>
              ))}
            </div>
          </section>
        ) : null}

        {lesson?.example_kn ? (
          <div className="alert alert-ok" style={{ marginTop: "1rem" }}>
            <strong>Everyday example · ದಿನನಿತ್ಯದ ಉದಾಹರಣೆ</strong>
            <p className="kan" style={{ margin: "0.3rem 0 0" }} lang="kn">
              {lesson.example_kn}
            </p>
          </div>
        ) : null}

        {lesson?.source_note ? (
          <p className="muted" style={{ fontSize: "0.8rem", marginTop: "0.8rem" }}>
            {lesson.source_note}
          </p>
        ) : null}

        <div className="row" style={{ marginTop: "1.2rem" }}>
          <button
            type="button"
            className="btn btn-primary"
            onClick={markComplete}
            disabled={saving || completed}
          >
            {completed ? "✓ Marked complete" : saving ? "Saving…" : "Mark as complete"}
          </button>
          {navState?.chapterId ? (
            <Link className="btn btn-ghost" to={`/quiz/${navState.chapterId}`}>
              Take chapter quiz
            </Link>
          ) : null}
          <Link className="btn btn-soft" to={tutorHref}>
            ✦ Ask the tutor about this lesson
          </Link>
        </div>
      </article>

      <p className="muted" style={{ fontSize: "0.82rem" }}>
        Lesson content is study material for WonderNest demos. AI explanations are generated
        for learning support, not official textbook material.
      </p>
    </div>
  );
}
