import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import {
  ApiError,
  api,
  type Chapter,
  type Progress,
  type StudentProfile,
  type Subject,
} from "../lib/api";
import { useAuth } from "../lib/auth";

export default function Dashboard() {
  const { user } = useAuth();
  const [profile, setProfile] = useState<StudentProfile | null>(null);
  const [progress, setProgress] = useState<Progress | null>(null);
  const [chapters, setChapters] = useState<{ chapter: Chapter; subject: Subject }[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const [profileData, progressData, boards] = await Promise.all([
          api.profile(),
          api.progress(),
          api.boards(),
        ]);
        if (!active) return;
        setProfile(profileData);
        setProgress(progressData);

        if (boards.length) {
          const classes = await api.classes(boards[0].id);
          if (classes.length) {
            const subjects = await api.subjects(classes[0].id);
            const lists = await Promise.all(subjects.map((subject) => api.chapters(subject.id)));
            if (!active) return;
            const flat = lists.flatMap((list, index) =>
              list.map((chapter) => ({ chapter, subject: subjects[index] })),
            );
            setChapters(flat);
          }
        }
      } catch (err) {
        if (!active) return;
        setError(
          err instanceof ApiError
            ? err.message
            : "Could not load your dashboard. Please refresh.",
        );
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  const completed = progress?.lessons_completed ?? 0;
  const opened = progress?.lessons_opened ?? 0;
  const attempts = progress?.quiz_attempts ?? 0;
  const nextChapter = chapters[0];

  if (loading) {
    return (
      <div className="container">
        <div className="loader">
          <div className="spinner" />
          <span>Loading your learning space…</span>
        </div>
      </div>
    );
  }

  return (
    <div className="container stack">
      <div className="row-between">
        <div>
          <span className="eyebrow">Dashboard</span>
          <h1 style={{ fontSize: "1.9rem", marginBottom: "0.2rem" }}>
            ನಮಸ್ಕಾರ, {profile?.display_name ?? user?.display_name} 👋
          </h1>
          <p className="muted" style={{ marginBottom: 0 }}>
            {profile?.class_label ?? "Class 8"} · {profile?.board_name_kn ?? "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಮಂಡಳಿ"} ·{" "}
            Science in Kannada &amp; English
          </p>
        </div>
        <Link className="btn btn-primary" to="/tutor">
          ✦ Ask the AI tutor
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
          <div className="stat-value">{attempts}</div>
          <div className="stat-label">Quiz attempts</div>
        </div>
        <div className="stat">
          <div className="stat-value">{chapters.length}</div>
          <div className="stat-label">Chapters available</div>
        </div>
      </div>

      <div className="grid grid-2">
        <section className="card stack">
          <div className="row-between">
            <h2 style={{ marginBottom: 0 }}>Continue learning</h2>
            <Link to="/curriculum" className="btn btn-ghost btn-sm">
              All chapters
            </Link>
          </div>

          {nextChapter ? (
            <div className="chapter-card" style={{ boxShadow: "none" }}>
              <div className="row">
                <span className="chapter-number">{nextChapter.chapter.number}</span>
                <div>
                  <h3 style={{ marginBottom: 0 }} className="kan">
                    {nextChapter.chapter.title_kn}
                  </h3>
                  <small>{nextChapter.chapter.title_en}</small>
                </div>
              </div>
              <p className="muted" style={{ fontSize: "0.9rem", marginBottom: 0 }}>
                {nextChapter.chapter.summary_kn ?? "Read the lesson, then practise with a quiz."}
              </p>
              <div className="row">
                <Link className="btn btn-soft btn-sm" to={`/curriculum#chapter-${nextChapter.chapter.id}`}>
                  Open chapter
                </Link>
                <Link className="btn btn-ghost btn-sm" to={`/quiz/${nextChapter.chapter.id}`}>
                  Take quiz
                </Link>
              </div>
            </div>
          ) : (
            <p className="muted">
              No chapters found yet. Run the seed command in the backend to load the Class 8
              Science curriculum.
            </p>
          )}
        </section>

        <section className="card stack">
          <h2 style={{ marginBottom: 0 }}>AI tutor</h2>
          <p className="muted" style={{ marginBottom: 0, fontSize: "0.92rem" }}>
            Powered by Google Gemini. Ask in Kannada or English, get simple explanations,
            everyday examples and hints instead of answers.
          </p>
          <div className="chips">
            <Link className="chip" to="/tutor?q=Explain%20photosynthesis%20in%20Kannada">
              Explain photosynthesis in Kannada
            </Link>
            <Link className="chip" to="/tutor?q=What%20is%20force%3F%20Give%20examples.">
              What is force? Give examples.
            </Link>
            <Link className="chip" to="/tutor?q=Give%20me%20five%20practice%20questions.">
              Give me five practice questions
            </Link>
          </div>
          <Link className="btn btn-primary" to="/tutor">
            Start a conversation
          </Link>
        </section>
      </div>

      <section className="card stack">
        <div className="row-between">
          <h2 style={{ marginBottom: 0 }}>Chapters</h2>
          <Link to="/progress" className="muted" style={{ fontSize: "0.85rem" }}>
            View progress →
          </Link>
        </div>
        <div className="grid grid-3">
          {chapters.map(({ chapter, subject }) => (
            <article className="chapter-card card-hover" key={chapter.id} id={`chapter-${chapter.id}`}>
              <div className="row">
                <span className="chapter-number">{chapter.number}</span>
                <div>
                  <h3 style={{ marginBottom: 0, fontSize: "1rem" }} className="kan">
                    {chapter.title_kn}
                  </h3>
                  <small>{subject.title_kn}</small>
                </div>
              </div>
              <div className="row" style={{ gap: "0.4rem" }}>
                <Link className="btn btn-soft btn-sm" to={`/quiz/${chapter.id}`}>
                  Quiz
                </Link>
                <Link className="btn btn-ghost btn-sm" to={`/curriculum#chapter-${chapter.id}`}>
                  Lessons
                </Link>
              </div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
