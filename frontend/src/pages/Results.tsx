import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { ApiError, api, type Quiz, type QuizResult } from "../lib/api";

const LETTERS = ["A", "B", "C", "D", "E"];

export default function Results() {
  const { attemptId } = useParams();
  const id = Number(attemptId);
  const [result, setResult] = useState<QuizResult | null>(null);
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const data = await api.attempt(id);
        if (!active) return;
        setResult(data);
        try {
          const quizData = await api.quiz(data.chapter_id);
          if (active) setQuiz(quizData);
        } catch {
          // Options are only used for the review labels; the score is still valid.
        }
      } catch (err) {
        if (active) {
          setError(
            err instanceof ApiError ? err.message : "Could not load this result. Try again.",
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

  if (loading) {
    return (
      <div className="container">
        <div className="loader">
          <div className="spinner" />
          <span>Checking your answers…</span>
        </div>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="container-narrow">
        <div className="alert alert-danger" role="alert">
          {error ?? "Result not found."}
        </div>
        <p>
          <Link to="/progress">← Back to progress</Link>
        </p>
      </div>
    );
  }

  const percentage = result.total ? Math.round((result.score / result.total) * 100) : 0;
  const encouragement =
    percentage >= 80
      ? "Excellent work! You have understood this chapter well."
      : percentage >= 50
        ? "Good effort. Review the explanations below and try again."
        : "Every attempt teaches you something. Read the explanations and give it another go.";

  function optionsFor(questionId: number): string[] {
    return quiz?.questions.find((question) => question.id === questionId)?.options_kn ?? [];
  }

  return (
    <div className="container-narrow stack">
      <div className="crumb">
        <Link to="/curriculum">Curriculum</Link>
        <span>› {result.chapter_title_kn}</span>
        <span>› Results</span>
      </div>

      <section className="card score-hero">
        <div className="score-ring" style={{ ["--pct" as string]: `${percentage}%` }}>
          <div>
            <strong>{percentage}%</strong>
            <small>
              {result.score}/{result.total}
            </small>
          </div>
        </div>
        <div>
          <span className="eyebrow">Quiz result</span>
          <h1 style={{ fontSize: "1.6rem", marginBottom: "0.3rem" }} className="kan">
            {result.chapter_title_kn}
          </h1>
          <p style={{ marginBottom: "0.6rem" }}>{encouragement}</p>
          <div className="row">
            <Link className="btn btn-primary" to={`/quiz/${result.chapter_id}`}>
              Try again
            </Link>
            <Link className="btn btn-ghost" to="/progress">
              View progress
            </Link>
            <Link
              className="btn btn-soft"
              to={`/tutor?chapter=${result.chapter_id}&title=${encodeURIComponent(result.chapter_title_kn)}`}
            >
              ✦ Ask the tutor to explain
            </Link>
          </div>
        </div>
      </section>

      <h2>Review</h2>
      <div className="stack">
        {result.answers.map((answer, index) => {
          const options = optionsFor(answer.question_id);
          return (
            <article
              className={`card review ${answer.is_correct ? "review-ok" : "review-bad"}`}
              key={answer.question_id}
            >
              <div className="row-between" style={{ alignItems: "flex-start" }}>
                <div className="row" style={{ alignItems: "flex-start", flexWrap: "nowrap" }}>
                  <span className="chapter-number" style={{ flex: "0 0 auto" }}>
                    {index + 1}
                  </span>
                  <h3 className="kan" style={{ marginBottom: 0 }} lang="kn">
                    {answer.question_kn}
                  </h3>
                </div>
                <span className={answer.is_correct ? "badge badge-ok" : "badge badge-bad"}>
                  {answer.is_correct ? "Correct" : "Needs practice"}
                </span>
              </div>

              <div className="stack" style={{ marginTop: "0.8rem", gap: "0.4rem" }}>
                <div className="option" aria-disabled="true">
                  <span className="option-letter">
                    {answer.selected_index === null ? "–" : LETTERS[answer.selected_index]}
                  </span>
                  <span className="kan" lang="kn">
                    {answer.selected_index === null
                      ? "Not answered"
                      : options[answer.selected_index] ?? `Option ${LETTERS[answer.selected_index]}`}
                  </span>
                  <span className="muted" style={{ marginLeft: "auto", fontSize: "0.78rem" }}>
                    Your answer
                  </span>
                </div>
                <div className="option correct">
                  <span className="option-letter">{LETTERS[answer.correct_index]}</span>
                  <span className="kan" lang="kn">
                    {options[answer.correct_index] ?? `Option ${LETTERS[answer.correct_index]}`}
                  </span>
                  <span className="muted" style={{ marginLeft: "auto", fontSize: "0.78rem" }}>
                    Correct answer
                  </span>
                </div>
              </div>

              {answer.explanation_kn ? (
                <p className="kan" lang="kn" style={{ margin: "0.8rem 0 0", fontSize: "0.92rem" }}>
                  <strong>ವಿವರಣೆ: </strong>
                  {answer.explanation_kn}
                </p>
              ) : null}
            </article>
          );
        })}
      </div>
    </div>
  );
}
