import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import { ApiError, api, type Quiz } from "../lib/api";

const LETTERS = ["A", "B", "C", "D", "E"];

export default function QuizPage() {
  const { chapterId } = useParams();
  const id = Number(chapterId);
  const navigate = useNavigate();

  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const data = await api.quiz(id);
        if (active) setQuiz(data);
      } catch (err) {
        if (active) {
          setError(
            err instanceof ApiError
              ? err.message
              : "Could not load this quiz. Please try again.",
          );
        }
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, [id]);

  const answeredCount = Object.keys(answers).length;
  const total = quiz?.total ?? 0;

  async function submit() {
    if (!quiz) return;
    setSubmitting(true);
    setError(null);
    try {
      const payload = quiz.questions.map((question) => ({
        question_id: question.id,
        selected_index: answers[question.id] ?? null,
      }));
      const result = await api.submitQuiz(id, payload);
      navigate(`/results/${result.attempt_id}`);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not submit your answers.");
      setSubmitting(false);
    }
  }

  if (loading) {
    return (
      <div className="container">
        <div className="loader">
          <div className="spinner" />
          <span>Loading quiz…</span>
        </div>
      </div>
    );
  }

  if (!quiz) {
    return (
      <div className="container-narrow">
        <div className="alert alert-danger" role="alert">
          {error ?? "Quiz not found."}
        </div>
        <p>
          <Link to="/curriculum">← Back to curriculum</Link>
        </p>
      </div>
    );
  }

  return (
    <div className="container-narrow stack">
      <div className="crumb">
        <Link to="/curriculum">Curriculum</Link>
        <span>› {quiz.chapter_title_kn}</span>
      </div>

      <div className="row-between">
        <div>
          <span className="eyebrow">Practice quiz</span>
          <h1 style={{ fontSize: "1.75rem", marginBottom: "0.2rem" }} className="kan">
            {quiz.chapter_title_kn}
          </h1>
          <small>{quiz.chapter_title_en}</small>
        </div>
        <span className="badge">
          {answeredCount}/{total} answered
        </span>
      </div>

      <div className="progress-track">
        <div
          className="progress-fill"
          style={{ width: `${total ? (answeredCount / total) * 100 : 0}%` }}
        />
      </div>

      {error ? (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      ) : null}

      <div className="stack">
        {quiz.questions.map((question, index) => (
          <article className="card" key={question.id}>
            <div className="row-between" style={{ alignItems: "flex-start" }}>
              <div className="row" style={{ alignItems: "flex-start", flexWrap: "nowrap" }}>
                <span className="chapter-number" style={{ flex: "0 0 auto" }}>
                  {index + 1}
                </span>
                <h3 className="kan" style={{ marginBottom: 0 }} lang="kn">
                  {question.question_kn}
                </h3>
              </div>
              <span className="badge">Level {question.difficulty}</span>
            </div>

            <div className="stack" style={{ marginTop: "0.9rem", gap: "0.5rem" }}>
              {question.options_kn.map((option, optionIndex) => {
                const selected = answers[question.id] === optionIndex;
                return (
                  <button
                    key={optionIndex}
                    type="button"
                    className={selected ? "option selected" : "option"}
                    onClick={() =>
                      setAnswers((current) => ({ ...current, [question.id]: optionIndex }))
                    }
                  >
                    <span className="option-letter">{LETTERS[optionIndex]}</span>
                    <span className="kan" lang="kn">
                      {option}
                    </span>
                  </button>
                );
              })}
            </div>
          </article>
        ))}
      </div>

      <div className="card card-tight row-between" style={{ position: "sticky", bottom: "1rem" }}>
        <span className="muted" style={{ fontSize: "0.88rem" }}>
          {answeredCount === total
            ? "All questions answered — ready to submit."
            : `You can submit with ${total - answeredCount} unanswered.`}
        </span>
        <div className="row">
          <Link className="btn btn-ghost btn-sm" to="/tutor">
            Need a hint? Ask the tutor
          </Link>
          <button
            type="button"
            className="btn btn-primary"
            onClick={submit}
            disabled={submitting || !total}
          >
            {submitting ? "Checking…" : "Submit answers"}
          </button>
        </div>
      </div>
    </div>
  );
}
