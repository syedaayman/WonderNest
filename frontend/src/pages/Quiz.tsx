import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import { ApiError, api, type Quiz } from "../lib/api";
import { pick, useLanguage } from "../lib/i18n";

const LETTERS = ["A", "B", "C", "D", "E"];

export default function QuizPage() {
  const { chapterId } = useParams();
  const id = Number(chapterId);
  const navigate = useNavigate();
  const { lang, t } = useLanguage();

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
          <span>{t("quiz.loading")}</span>
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
          <Link to="/curriculum">← {t("nav.curriculum")}</Link>
        </p>
      </div>
    );
  }

  const chapterTitle = pick(lang, quiz.chapter_title_en, quiz.chapter_title_kn);
  const tutorHref = `/tutor?chapter=${id}&title=${encodeURIComponent(chapterTitle)}`;

  return (
    <div className="container-narrow stack">
      <div className="crumb">
        <Link to="/curriculum">{t("nav.curriculum")}</Link>
        <span>› {chapterTitle}</span>
      </div>

      <div className="row-between">
        <div>
          <span className="eyebrow">{t("quiz.eyebrow")}</span>
          <h1 style={{ fontSize: "1.75rem", marginBottom: "0.2rem" }}>{chapterTitle}</h1>
          <small className="muted">{quiz.category} · Class 8 Science</small>
        </div>
        <span className="badge">
          {answeredCount}/{total} {t("quiz.answered")}
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
        {quiz.questions.map((question, index) => {
          const questionText = pick(lang, question.question_en, question.question_kn);
          const options = lang === "kn" ? question.options_kn : question.options_en.length
            ? question.options_en
            : question.options_kn;
          return (
            <article className="card" key={question.id}>
              <div className="row-between" style={{ alignItems: "flex-start" }}>
                <div className="row" style={{ alignItems: "flex-start", flexWrap: "nowrap" }}>
                  <span className="chapter-number" style={{ flex: "0 0 auto" }}>
                    {index + 1}
                  </span>
                  <h3
                    style={{ marginBottom: 0 }}
                    lang={lang === "kn" ? "kn" : "en"}
                    className={lang === "kn" ? "kan" : undefined}
                  >
                    {questionText}
                  </h3>
                </div>
                <span className="badge">
                  {t("quiz.level")} {question.difficulty}
                </span>
              </div>

              <div className="stack" style={{ marginTop: "0.9rem", gap: "0.5rem" }}>
                {options.map((option, optionIndex) => {
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
                      <span lang={lang === "kn" ? "kn" : "en"}>{option}</span>
                    </button>
                  );
                })}
              </div>
            </article>
          );
        })}
      </div>

      <div className="card card-tight row-between sticky-bar">
        <span className="muted" style={{ fontSize: "0.88rem" }}>
          {answeredCount === total
            ? t("quiz.allAnswered")
            : `${total - answeredCount} ${t("quiz.someUnanswered")}`}
        </span>
        <div className="row" style={{ gap: "0.5rem", flexWrap: "wrap" }}>
          <Link className="btn btn-ghost btn-sm" to={tutorHref}>
            {t("quiz.hint")}
          </Link>
          <button
            type="button"
            className="btn btn-primary"
            onClick={submit}
            disabled={submitting || !total}
          >
            {submitting ? t("quiz.checking") : t("quiz.submit")}
          </button>
        </div>
      </div>
    </div>
  );
}
