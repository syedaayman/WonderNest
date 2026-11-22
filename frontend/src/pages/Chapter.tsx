import { useEffect, useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";

import { RichText } from "../components/RichText";
import { Visualization } from "../components/Visualizations";
import { api, type ChapterContent } from "../lib/api";
import { pick, useLanguage } from "../lib/i18n";

const TABS = ["learn", "visualize", "notes", "videos", "quiz", "tutor"] as const;
type Tab = (typeof TABS)[number];

function isTab(value: string | null): value is Tab {
  return !!value && (TABS as readonly string[]).includes(value);
}

export default function Chapter() {
  const { chapterId } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const { lang, t } = useLanguage();

  const tabParam = searchParams.get("tab");
  const tab: Tab = isTab(tabParam) ? tabParam : "learn";

  const [content, setContent] = useState<ChapterContent | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const id = Number(chapterId);

  useEffect(() => {
    if (!Number.isFinite(id)) {
      setError("That chapter does not exist.");
      setLoading(false);
      return;
    }
    let active = true;
    setLoading(true);
    (async () => {
      try {
        const data = await api.chapterContent(id);
        if (!active) return;
        setContent(data);
        setError(null);
      } catch (err) {
        if (!active) return;
        setError(err instanceof Error ? err.message : "Could not load this chapter.");
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, [id]);

  const firstLessonId = useMemo(() => {
    const first = content?.topics.find((topic) => topic.lesson);
    return first?.lesson?.id ?? null;
  }, [content]);

  useEffect(() => {
    if (tab !== "learn" || !firstLessonId) return;
    void api.recordLessonProgress(firstLessonId, "opened").catch(() => undefined);
  }, [tab, firstLessonId]);

  function selectTab(next: Tab) {
    const params = new URLSearchParams(searchParams);
    params.set("tab", next);
    setSearchParams(params, { replace: true });
  }

  if (loading) {
    return (
      <div className="container">
        <div className="loader">
          <div className="spinner" />
          <span>{t("common.loading")}</span>
        </div>
      </div>
    );
  }

  if (error || !content) {
    return (
      <div className="container">
        <div className="alert alert-danger" role="alert">
          <strong>Something went wrong</strong>
          <p style={{ margin: "0.35rem 0 0" }}>{error ?? "Chapter not found."}</p>
        </div>
        <Link className="btn btn-ghost" to="/curriculum">
          ← {t("nav.curriculum")}
        </Link>
      </div>
    );
  }

  const chapter = content.chapter;
  const title = pick(lang, chapter.title_en, chapter.title_kn);
  const summary = pick(lang, chapter.summary_en, chapter.summary_kn);
  const notes = lang === "kn" ? content.notes_kn : content.notes_en.length ? content.notes_en : content.notes_kn;
  const vizKeys = content.visualizations.length ? content.visualizations : chapter.visualizations;
  const tutorHref = `/tutor?chapter=${chapter.id}&title=${encodeURIComponent(title)}${
    content.topics[0] ? `&topic=${content.topics[0].id}` : ""
  }${firstLessonId ? `&lesson=${firstLessonId}` : ""}`;

  return (
    <div className="container chapter-page">
      <div className="chapter-hero card">
        <div className="row-between" style={{ flexWrap: "wrap", gap: "0.75rem" }}>
          <Link className="link-back" to="/curriculum">
            ← {t("nav.curriculum")}
          </Link>
          <span className="badge badge-soft">
            {chapter.is_enrichment ? t("curriculum.enrichment") : chapter.category}
          </span>
        </div>
        <h1 className="chapter-hero-title">{title}</h1>
        {summary ? <p className="chapter-hero-summary">{summary}</p> : null}
        <div className="chapter-meta">
          <span>
            {content.topics.length} {t("chapter.objectives")}
          </span>
          <span aria-hidden="true">·</span>
          <span>
            {content.question_count} {t("common.questions")}
          </span>
          <span aria-hidden="true">·</span>
          <span>
            {chapter.estimated_minutes} {t("common.minutes")}
          </span>
        </div>
      </div>

      <nav className="tabs" aria-label="Chapter sections" role="tablist">
        {TABS.map((key) => (
          <button
            key={key}
            type="button"
            role="tab"
            aria-selected={tab === key}
            className={tab === key ? "tab active" : "tab"}
            onClick={() => selectTab(key)}
          >
            {t(`chapter.tab.${key}`)}
          </button>
        ))}
      </nav>

      {tab === "learn" ? (
        <section className="tab-panel">
          {content.topics.map((topic) => (
            <article key={topic.id} className="card topic-block">
              <h2 className="topic-title">{pick(lang, topic.title_en, topic.title_kn)}</h2>

              {topic.objectives.length ? (
                <>
                  <h3 className="subhead">{t("chapter.objectives")}</h3>
                  <ul className="objective-list">
                    {topic.objectives.map((objective) => (
                      <li key={objective.id}>
                        {pick(lang, objective.text_en, objective.text_kn)}
                      </li>
                    ))}
                  </ul>
                </>
              ) : null}

              {topic.lesson ? (
                <>
                  <div className="lesson-body">
                    <RichText
                      text={pick(lang, topic.lesson.body_en, topic.lesson.body_kn)}
                    />
                  </div>

                  {pick(lang, topic.lesson.example_en, topic.lesson.example_kn) ? (
                    <div className="callout callout-example">
                      <strong>{t("chapter.example")}</strong>
                      <p>
                        {pick(lang, topic.lesson.example_en, topic.lesson.example_kn)}
                      </p>
                    </div>
                  ) : null}

                  {topic.lesson.key_terms.length ? (
                    <>
                      <h3 className="subhead">{t("chapter.keyTerms")}</h3>
                      <dl className="term-grid">
                        {topic.lesson.key_terms.map((term) => (
                          <div key={`${topic.id}-${term.kn}`} className="term-card">
                            <dt>
                              <span lang="kn">{term.kn}</span>
                              <span className="term-en">{term.en}</span>
                            </dt>
                            <dd>{pick(lang, term.meaning_en, term.meaning_kn)}</dd>
                          </div>
                        ))}
                      </dl>
                    </>
                  ) : null}

                  <div className="row" style={{ gap: "0.5rem", flexWrap: "wrap" }}>
                    <Link className="btn btn-primary btn-sm" to={`/lesson/${topic.lesson.id}`}>
                      {t("curriculum.start")}
                    </Link>
                    <button type="button" className="btn btn-ghost btn-sm" onClick={() => selectTab("visualize")}>
                      {t("chapter.tab.visualize")}
                    </button>
                  </div>
                </>
              ) : (
                <p className="muted">Lesson notes are being prepared for this topic.</p>
              )}
            </article>
          ))}

          {!content.topics.length ? (
            <div className="card empty-state">
              <p>No topics yet for this unit.</p>
            </div>
          ) : null}
        </section>
      ) : null}

      {tab === "visualize" ? (
        <section className="tab-panel">
          <div className="panel-head">
            <h2>{t("chapter.visualizeTitle")}</h2>
            <p className="muted">{t("chapter.visualizeHint")}</p>
          </div>
          {vizKeys.length ? (
            <div className="viz-stack">
              {vizKeys.map((key) => (
                <Visualization key={key} vizKey={key} />
              ))}
            </div>
          ) : (
            <div className="card empty-state">
              <p>A diagram for this unit is coming soon.</p>
            </div>
          )}
        </section>
      ) : null}

      {tab === "notes" ? (
        <section className="tab-panel">
          <div className="panel-head row-between" style={{ flexWrap: "wrap", gap: "0.5rem" }}>
            <div>
              <h2>{t("chapter.notesTitle")}</h2>
              <p className="muted">{t("chapter.notesHint")}</p>
            </div>
            <button type="button" className="btn btn-ghost btn-sm" onClick={() => window.print()}>
              🖨 {t("chapter.print")}
            </button>
          </div>
          <div className="card notes-card">
            <ul className="notes-list">
              {notes.map((note, index) => (
                <li key={index}>{note}</li>
              ))}
            </ul>
          </div>
        </section>
      ) : null}

      {tab === "videos" ? (
        <section className="tab-panel">
          <div className="panel-head">
            <h2>{t("chapter.videosTitle")}</h2>
            <p className="muted">{t("chapter.videosHint")}</p>
          </div>
          <div className="video-grid">
            {content.videos.map((video, index) => {
              const href = video.video_id
                ? `https://www.youtube.com/watch?v=${video.video_id}`
                : `https://www.youtube.com/results?search_query=${encodeURIComponent(video.search_query)}`;
              return (
                <article key={`${video.title}-${index}`} className="video-card">
                  <a className="video-thumb" href={href} target="_blank" rel="noreferrer noopener">
                    {video.video_id ? (
                      <img
                        src={`https://i.ytimg.com/vi/${video.video_id}/hqdefault.jpg`}
                        alt=""
                        loading="lazy"
                      />
                    ) : (
                      <span className="video-thumb-fallback" aria-hidden="true">
                        ▶
                      </span>
                    )}
                  </a>
                  <div className="video-body">
                    <div className="row" style={{ gap: "0.4rem", flexWrap: "wrap" }}>
                      <span className="badge badge-muted">
                        {video.language === "kn" ? "ಕನ್ನಡ" : "English"}
                      </span>
                      <span className="badge badge-soft">{video.topic}</span>
                    </div>
                    <h3 className="video-title">{video.title}</h3>
                    <a
                      className="link-button"
                      href={href}
                      target="_blank"
                      rel="noreferrer noopener"
                    >
                      {video.video_id ? "Watch on YouTube ↗" : `${t("chapter.searchOnYoutube")} ↗`}
                    </a>
                  </div>
                </article>
              );
            })}
          </div>
          {!content.videos.length ? (
            <div className="card empty-state">
              <p>Video recommendations are being curated for this unit.</p>
            </div>
          ) : null}
        </section>
      ) : null}

      {tab === "quiz" ? (
        <section className="tab-panel">
          <div className="card quiz-cta">
            <h2>{t("chapter.quizTitle")}</h2>
            <p className="muted">{t("chapter.quizHint")}</p>
            <p>
              <strong>
                {content.question_count} {t("common.questions")}
              </strong>{" "}
              · {t("quiz.level")} Class 8
            </p>
            <Link className="btn btn-primary" to={`/quiz/${chapter.id}`}>
              {t("chapter.startQuiz")}
            </Link>
            <p className="muted" style={{ fontSize: "0.8rem", marginTop: "0.75rem" }}>
              {t("quiz.hint")}{" "}
              <Link to={tutorHref}>{t("chapter.tab.tutor")}</Link>
            </p>
          </div>
        </section>
      ) : null}

      {tab === "tutor" ? (
        <section className="tab-panel">
          <div className="card quiz-cta">
            <h2>{t("chapter.tutorTitle")}</h2>
            <p className="muted">{t("chapter.tutorHint")}</p>
            <Link className="btn btn-primary" to={tutorHref}>
              ✦ {t("chapter.openTutor")}
            </Link>
            <p className="muted" style={{ fontSize: "0.8rem", marginTop: "0.75rem" }}>
              {t("chapter.sourceNote")}: {chapter.source_note ?? "WonderNest original material."}
            </p>
          </div>
        </section>
      ) : null}
    </div>
  );
}
