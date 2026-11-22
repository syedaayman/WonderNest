import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";

import {
  ApiError,
  api,
  type Chapter,
  type ClassLevel,
  type Lesson,
  type Subject,
  type Topic,
} from "../lib/api";

export default function Curriculum() {
  const location = useLocation();
  const [classes, setClasses] = useState<ClassLevel[]>([]);
  const [subjects, setSubjects] = useState<Subject[]>([]);
  const [chapters, setChapters] = useState<Chapter[]>([]);
  const [classId, setClassId] = useState<number | null>(null);
  const [subjectId, setSubjectId] = useState<number | null>(null);
  const [expanded, setExpanded] = useState<number | null>(null);
  const [topics, setTopics] = useState<Record<number, Topic[]>>({});
  const [lessons, setLessons] = useState<Record<number, Lesson[]>>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Initial load: board -> class -> subject -> chapters.
  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const boards = await api.boards();
        if (!boards.length) throw new ApiError("No boards available.", 404);
        const classList = await api.classes(boards[0].id);
        if (!classList.length) throw new ApiError("No classes available.", 404);
        const subjectList = await api.subjects(classList[0].id);
        if (!active) return;
        setClasses(classList);
        setClassId(classList[0].id);
        setSubjects(subjectList);
        if (subjectList.length) {
          setSubjectId(subjectList[0].id);
          const chapterList = await api.chapters(subjectList[0].id);
          if (active) setChapters(chapterList);
        }
      } catch (err) {
        if (active) {
          setError(
            err instanceof ApiError
              ? err.message
              : "Could not load the curriculum. Is the backend running?",
          );
        }
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  // Deep link support: /curriculum#chapter-3 opens that chapter.
  useEffect(() => {
    const hash = location.hash.replace("#chapter-", "");
    const id = Number(hash);
    if (id) {
      setExpanded(id);
      document.getElementById(`chapter-${id}`)?.scrollIntoView({ behavior: "smooth" });
    }
  }, [location.hash, chapters]);

  async function chooseClass(id: number) {
    setClassId(id);
    setError(null);
    try {
      const subjectList = await api.subjects(id);
      setSubjects(subjectList);
      setChapters([]);
      setExpanded(null);
      if (subjectList.length) {
        setSubjectId(subjectList[0].id);
        setChapters(await api.chapters(subjectList[0].id));
      } else {
        setSubjectId(null);
      }
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not load subjects.");
    }
  }

  async function chooseSubject(id: number) {
    setSubjectId(id);
    setExpanded(null);
    setError(null);
    try {
      setChapters(await api.chapters(id));
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not load chapters.");
    }
  }

  async function toggleChapter(chapter: Chapter) {
    if (expanded === chapter.id) {
      setExpanded(null);
      return;
    }
    setExpanded(chapter.id);
    if (!topics[chapter.id]) {
      try {
        const list = await api.topics(chapter.id);
        setTopics((current) => ({ ...current, [chapter.id]: list }));
      } catch (err) {
        setError(err instanceof ApiError ? err.message : "Could not load topics.");
      }
    }
  }

  async function loadLessons(topic: Topic) {
    if (lessons[topic.id]) return;
    try {
      const list = await api.lessons(topic.id);
      setLessons((current) => ({ ...current, [topic.id]: list }));
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not load lessons.");
    }
  }

  const currentSubject = subjects.find((subject) => subject.id === subjectId) ?? null;

  return (
    <div className="container stack">
      <div className="row-between">
        <div>
          <span className="eyebrow">Curriculum</span>
          <h1 style={{ fontSize: "1.9rem", marginBottom: "0.2rem" }}>
            {currentSubject?.title_kn ?? "ವಿಜ್ಞಾನ"}{" "}
            <span className="muted" style={{ fontSize: "1rem" }}>
              {currentSubject?.title_en ?? "Science"}
            </span>
          </h1>
          <p className="muted" style={{ marginBottom: 0 }}>
            Karnataka State Board · Class 8 · pick a chapter to read the lesson and take the quiz.
          </p>
        </div>
        <Link className="btn btn-ghost" to="/tutor">
          ✦ Ask the tutor
        </Link>
      </div>

      {error ? (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      ) : null}

      <div className="card card-tight row" style={{ gap: "0.8rem" }}>
        <div className="field" style={{ minWidth: 190 }}>
          <label className="label" htmlFor="class-select">
            Class
          </label>
          <select
            id="class-select"
            className="select"
            value={classId ?? ""}
            onChange={(event) => chooseClass(Number(event.target.value))}
          >
            {classes.map((item) => (
              <option key={item.id} value={item.id}>
                {item.label}
              </option>
            ))}
          </select>
        </div>
        <div className="field" style={{ minWidth: 190 }}>
          <label className="label" htmlFor="subject-select">
            Subject
          </label>
          <select
            id="subject-select"
            className="select"
            value={subjectId ?? ""}
            onChange={(event) => chooseSubject(Number(event.target.value))}
          >
            {subjects.map((item) => (
              <option key={item.id} value={item.id}>
                {item.title_kn} ({item.title_en})
              </option>
            ))}
          </select>
        </div>
        <div className="spacer" />
        <span className="badge">{chapters.length} chapters</span>
      </div>

      {loading ? (
        <div className="loader">
          <div className="spinner" />
          <span>Loading chapters…</span>
        </div>
      ) : null}

      {!loading && !chapters.length ? (
        <div className="card">
          <h3>No chapters yet</h3>
          <p className="muted" style={{ marginBottom: 0 }}>
            Run <code>python -m app.curriculum.cli</code> in the backend folder to seed the
            Class 8 Science curriculum.
          </p>
        </div>
      ) : null}

      <div className="stack">
        {chapters.map((chapter) => {
          const chapterTopics = topics[chapter.id];
          return (
            <article className="chapter-card" key={chapter.id} id={`chapter-${chapter.id}`}>
              <div className="row-between">
                <div className="row">
                  <span className="chapter-number">{chapter.number}</span>
                  <div>
                    <h3 style={{ marginBottom: "0.1rem" }} className="kan">
                      {chapter.title_kn}
                    </h3>
                    <small>
                      {chapter.title_en} · {chapter.estimated_minutes} min
                    </small>
                  </div>
                </div>
                <div className="row" style={{ gap: "0.45rem" }}>
                  {chapter.is_sample ? <span className="badge badge-warn">Sample content</span> : null}
                  <button
                    type="button"
                    className="btn btn-soft btn-sm"
                    onClick={() => toggleChapter(chapter)}
                  >
                    {expanded === chapter.id ? "Hide topics" : "View topics"}
                  </button>
                  <Link className="btn btn-primary btn-sm" to={`/quiz/${chapter.id}`}>
                    Quiz
                  </Link>
                </div>
              </div>

              {chapter.summary_kn ? (
                <p className="muted kan" style={{ marginBottom: 0, fontSize: "0.92rem" }}>
                  {chapter.summary_kn}
                </p>
              ) : null}

              {expanded === chapter.id ? (
                <div>
                  {!chapterTopics ? (
                    <small className="muted">Loading topics…</small>
                  ) : (
                    chapterTopics.map((topic) => (
                      <div key={topic.id}>
                        <div className="topic-row">
                          <span className="dot" aria-hidden="true" />
                          <div style={{ flex: 1, minWidth: 160 }}>
                            <strong className="kan">{topic.title_kn}</strong>
                            <div>
                              <small>{topic.title_en}</small>
                            </div>
                          </div>
                          <button
                            type="button"
                            className="btn btn-ghost btn-sm"
                            onClick={() => loadLessons(topic)}
                          >
                            Show lessons
                          </button>
                        </div>
                        {lessons[topic.id] ? (
                          <div style={{ paddingLeft: "1.4rem", paddingBottom: "0.5rem" }}>
                            {lessons[topic.id].length === 0 ? (
                              <small className="muted">No lesson written for this topic yet.</small>
                            ) : (
                              lessons[topic.id].map((lesson) => (
                                <div className="row" key={lesson.id} style={{ padding: "0.25rem 0" }}>
                                  <Link
                                    className="btn btn-soft btn-sm"
                                    to={`/lesson/${lesson.id}`}
                                    state={{
                                      chapterId: chapter.id,
                                      chapterTitle: chapter.title_kn,
                                      topicId: topic.id,
                                      topicTitle: topic.title_kn,
                                    }}
                                  >
                                    Read lesson →
                                  </Link>
                                  <small className="muted">
                                    {lesson.example_kn ? "Includes an everyday example" : "Key terms included"}
                                  </small>
                                </div>
                              ))
                            )}
                          </div>
                        ) : null}
                      </div>
                    ))
                  )}
                  <div className="row" style={{ marginTop: "0.6rem" }}>
                    <Link
                      className="btn btn-ghost btn-sm"
                      to={`/tutor?chapter=${chapter.id}&title=${encodeURIComponent(chapter.title_kn)}`}
                    >
                      Ask the tutor about this chapter
                    </Link>
                  </div>
                </div>
              ) : null}
            </article>
          );
        })}
      </div>
    </div>
  );
}
