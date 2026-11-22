import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { ApiError, api, type Chapter, type Progress } from "../lib/api";

export default function ProgressPage() {
  const [progress, setProgress] = useState<Progress | null>(null);
  const [chapters, setChapters] = useState<Chapter[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const [progressData, boards] = await Promise.all([api.progress(), api.boards()]);
        if (!active) return;
        setProgress(progressData);

        if (boards.length) {
          const classes = await api.classes(boards[0].id);
          if (classes.length) {
            const subjects = await api.subjects(classes[0].id);
            const lists = await Promise.all(subjects.map((subject) => api.chapters(subject.id)));
            if (active) setChapters(lists.flat());
          }
        }
      } catch (err) {
        if (active) {
          setError(err instanceof ApiError ? err.message : "Could not load your progress.");
        }
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  if (loading) {
    return (
      <div className="container">
        <div className="loader">
          <div className="spinner" />
          <span>Loading your progress…</span>
        </div>
      </div>
    );
  }

  const opened = progress?.lessons_opened ?? 0;
  const completed = progress?.lessons_completed ?? 0;
  const attempts = progress?.quiz_attempts_list ?? [];
  const bestPercentage = attempts.reduce(
    (best, attempt) =>
      attempt.total ? Math.max(best, Math.round((attempt.score / attempt.total) * 100)) : best,
    0,
  );
  const averagePercentage = attempts.length
    ? Math.round(
        attempts.reduce(
          (sum, attempt) => sum + (attempt.total ? (attempt.score / attempt.total) * 100 : 0),
          0,
        ) / attempts.length,
      )
    : 0;

  function chapterTitle(chapterId: number): string {
    return chapters.find((chapter) => chapter.id === chapterId)?.title_kn ?? `Chapter ${chapterId}`;
  }

  return (
    <div className="container stack">
      <div className="row-between">
        <div>
          <span className="eyebrow">Progress</span>
          <h1 style={{ fontSize: "1.9rem", marginBottom: "0.2rem" }}>Your learning journey</h1>
          <p className="muted" style={{ marginBottom: 0 }}>
            Lessons opened, quizzes attempted and how you are improving.
          </p>
        </div>
        <Link className="btn btn-primary" to="/curriculum">
          Continue learning
        </Link>
      </div>

      {error ? (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      ) : null}

      <div className="grid grid-4">
        <div className="stat">
          <div className="stat-value">{opened}</div>
          <div className="stat-label">Lessons opened</div>
        </div>
        <div className="stat">
          <div className="stat-value">{completed}</div>
          <div className="stat-label">Lessons completed</div>
        </div>
        <div className="stat">
          <div className="stat-value">{bestPercentage}%</div>
          <div className="stat-label">Best quiz score</div>
        </div>
        <div className="stat">
          <div className="stat-value">{averagePercentage}%</div>
          <div className="stat-label">Average score</div>
        </div>
      </div>

      <div className="grid grid-2">
        <section className="card stack">
          <h2 style={{ marginBottom: 0 }}>Lesson progress</h2>
          {progress?.lesson_progress.length ? (
            <div className="stack" style={{ gap: "0.6rem" }}>
              {progress.lesson_progress.map((row) => (
                <div className="topic-row" key={row.lesson_id}>
                  <span className={row.completed_at ? "badge badge-ok" : "badge"}>
                    {row.completed_at ? "Completed" : "In progress"}
                  </span>
                  <div style={{ flex: 1 }}>
                    <strong>Lesson #{row.lesson_id}</strong>
                    <div>
                      <small className="muted">
                        {row.time_spent_seconds
                          ? `${Math.round(row.time_spent_seconds / 60)} min spent`
                          : "Opened"}
                      </small>
                    </div>
                  </div>
                  <Link className="btn btn-ghost btn-sm" to={`/lesson/${row.lesson_id}`}>
                    Open
                  </Link>
                </div>
              ))}
            </div>
          ) : (
            <p className="muted" style={{ marginBottom: 0 }}>
              No lessons opened yet. Start with a chapter in the curriculum.
            </p>
          )}
        </section>

        <section className="card stack">
          <h2 style={{ marginBottom: 0 }}>Quiz attempts</h2>
          {attempts.length ? (
            <div className="stack" style={{ gap: "0.6rem" }}>
              {attempts.map((attempt) => {
                const pct = attempt.total ? Math.round((attempt.score / attempt.total) * 100) : 0;
                return (
                  <div key={attempt.id}>
                    <div className="row-between">
                      <strong className="kan">{chapterTitle(attempt.chapter_id)}</strong>
                      <span className="badge">
                        {attempt.score}/{attempt.total} · {pct}%
                      </span>
                    </div>
                    <div className="progress-track" style={{ margin: "0.35rem 0 0.3rem" }}>
                      <div className="progress-fill" style={{ width: `${pct}%` }} />
                    </div>
                    <Link
                      to={`/results/${attempt.id}`}
                      className="muted"
                      style={{ fontSize: "0.82rem" }}
                    >
                      Review answers →
                    </Link>
                  </div>
                );
              })}
            </div>
          ) : (
            <p className="muted" style={{ marginBottom: 0 }}>
              No quiz attempts yet. Pick a chapter and test yourself.
            </p>
          )}
        </section>
      </div>
    </div>
  );
}
