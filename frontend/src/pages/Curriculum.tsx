import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";

import { api, type Chapter, type Category, type Progress } from "../lib/api";
import { pick, useLanguage } from "../lib/i18n";

const CATEGORY_ORDER = ["biology", "physics", "chemistry", "enrichment"];

const CATEGORY_THEME: Record<string, { icon: string; accent: string }> = {
  biology: { icon: "🌿", accent: "var(--cat-bio)" },
  physics: { icon: "⚡", accent: "var(--cat-phys)" },
  chemistry: { icon: "⚗️", accent: "var(--cat-chem)" },
  enrichment: { icon: "✨", accent: "var(--cat-enrich)" },
};

const VISUAL_ICON: Record<string, string> = {
  photosynthesis: "🍃",
  brain: "🧠",
  microorganisms: "🦠",
  electricity: "🔌",
  forces: "🧲",
  matter: "🧊",
  light: "🔍",
};

function chapterIcon(chapter: Chapter): string {
  for (const key of chapter.visualizations) {
    if (VISUAL_ICON[key]) return VISUAL_ICON[key];
  }
  return CATEGORY_THEME[chapter.category]?.icon ?? "📘";
}

interface ChapterStat {
  best: number;
  total: number;
  attempts: number;
}

export default function Curriculum() {
  const { lang, t } = useLanguage();
  const [chapters, setChapters] = useState<Chapter[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [progress, setProgress] = useState<Progress | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [subjectId, setSubjectId] = useState<number | null>(null);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const [boardList, categoryList, progressData] = await Promise.all([
          api.boards(),
          api.categories().catch(() => [] as Category[]),
          api.progress().catch(() => null),
        ]);
        if (!active) return;
        setCategories(categoryList);
        setProgress(progressData);

        let resolvedSubject: number | null = null;
        for (const board of boardList) {
          const classes = await api.classes(board.id);
          if (!classes.length) continue;
          const subjects = await api.subjects(classes[0].id);
          const science = subjects.find((s) => /sci/i.test(s.code) || /ವಿಜ್ಞಾನ/.test(s.title_kn));
          if (science) {
            resolvedSubject = science.id;
            break;
          }
          if (subjects[0]) {
            resolvedSubject = subjects[0].id;
            break;
          }
        }
        if (!active) return;
        if (!resolvedSubject) {
          setChapters([]);
          return;
        }
        setSubjectId(resolvedSubject);
        const chapterList = await api.chapters(resolvedSubject);
        if (!active) return;
        setChapters(chapterList);
      } catch (err) {
        if (!active) return;
        setError(err instanceof Error ? err.message : "Could not load the curriculum.");
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  const stats = useMemo(() => {
    const map = new Map<number, ChapterStat>();
    for (const attempt of progress?.quiz_attempts_list ?? []) {
      const current = map.get(attempt.chapter_id) ?? { best: 0, total: attempt.total, attempts: 0 };
      const ratio = attempt.total ? attempt.score / attempt.total : 0;
      const bestRatio = current.total ? current.best / current.total : 0;
      map.set(attempt.chapter_id, {
        best: ratio > bestRatio ? attempt.score : current.best,
        total: attempt.total,
        attempts: current.attempts + 1,
      });
    }
    return map;
  }, [progress]);

  const categoryLabel = (key: string): string => {
    const found = categories.find((c) => c.key === key);
    if (found) return lang === "kn" ? found.label_kn : found.label_en;
    return key.charAt(0).toUpperCase() + key.slice(1);
  };

  const grouped = useMemo(() => {
    const keys = Array.from(new Set(chapters.map((c) => c.category)));
    keys.sort((a, b) => {
      const ai = CATEGORY_ORDER.indexOf(a);
      const bi = CATEGORY_ORDER.indexOf(b);
      return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
    });
    return keys.map((key) => ({
      key,
      chapters: chapters.filter((c) => c.category === key),
    }));
  }, [chapters]);

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

  return (
    <div className="container curriculum-page">
      <header className="page-head">
        <p className="eyebrow">{t("curriculum.eyebrow")}</p>
        <h1>{t("curriculum.title")}</h1>
        <p className="muted page-sub">{t("curriculum.subtitle")}</p>
      </header>

      {error ? (
        <div className="alert alert-danger" role="alert">
          <strong>{t("common.retry")}</strong>
          <p style={{ margin: "0.35rem 0 0" }}>{error}</p>
        </div>
      ) : null}

      {!chapters.length && !error ? (
        <div className="card empty-state">
          <span className="empty-icon" aria-hidden="true">
            📚
          </span>
          <p>{t("curriculum.empty")}</p>
        </div>
      ) : null}

      {grouped.map((group) => {
        const theme = CATEGORY_THEME[group.key] ?? CATEGORY_THEME.enrichment;
        return (
          <section
          key={group.key}
          id={`cat-${group.key}`}
          className="category-block"
          aria-labelledby={`cat-${group.key}`}
        >
            <div className="category-head">
              <span className="category-chip" style={{ background: theme.accent }}>
                <span aria-hidden="true">{theme.icon}</span> {categoryLabel(group.key)}
              </span>
              <span className="muted" style={{ fontSize: "0.8rem" }}>
                {group.chapters.length} {t("common.chapters")}
              </span>
            </div>
            <div className="chapter-grid">
              {group.chapters.map((chapter) => {
                const stat = stats.get(chapter.id);
                const percent = stat && stat.total ? Math.round((stat.best / stat.total) * 100) : 0;
                const title = pick(lang, chapter.title_en, chapter.title_kn);
                const summary = pick(lang, chapter.summary_en, chapter.summary_kn);
                const statusLabel = !stat
                  ? t("curriculum.notStarted")
                  : percent >= 80
                    ? t("curriculum.review")
                    : t("curriculum.continue");
                return (
                  <article
                    key={chapter.id}
                    className="chapter-card"
                    style={{ ["--accent" as string]: theme.accent }}
                  >
                    <div className="chapter-card-top">
                      <span className="chapter-art" aria-hidden="true">
                        {chapterIcon(chapter)}
                      </span>
                      <div className="chapter-badges">
                        <span className="badge badge-soft">
                          {chapter.is_enrichment ? t("curriculum.enrichment") : categoryLabel(group.key)}
                        </span>
                        <span className="badge badge-muted">#{chapter.number}</span>
                      </div>
                    </div>

                    <h3 className="chapter-title">{title}</h3>
                    {summary ? <p className="chapter-summary">{summary}</p> : null}

                    <div className="chapter-meta">
                      <span>
                        {chapter.estimated_minutes} {t("common.minutes")}
                      </span>
                      <span aria-hidden="true">·</span>
                      <span>{statusLabel}</span>
                      {stat ? (
                        <>
                          <span aria-hidden="true">·</span>
                          <span>
                            {t("curriculum.bestScore")} {stat.best}/{stat.total}
                          </span>
                        </>
                      ) : null}
                    </div>

                    <div
                      className="progress-track"
                      role="progressbar"
                      aria-valuenow={percent}
                      aria-valuemin={0}
                      aria-valuemax={100}
                      aria-label={t("curriculum.progress")}
                    >
                      <div className="progress-fill" style={{ width: `${percent}%` }} />
                    </div>

                    <div className="chapter-actions">
                      <Link className="btn btn-primary btn-sm" to={`/chapter/${chapter.id}`}>
                        {stat ? t("curriculum.continue") : t("curriculum.start")}
                      </Link>
                      <Link className="btn btn-ghost btn-sm" to={`/quiz/${chapter.id}`}>
                        {t("curriculum.quiz")}
                      </Link>
                    </div>
                  </article>
                );
              })}
            </div>
          </section>
        );
      })}

      {grouped.some((g) => g.key === "enrichment") ? (
        <p className="muted enrichment-note">{t("curriculum.enrichmentNote")}</p>
      ) : null}

      {subjectId ? (
        <p className="muted" style={{ fontSize: "0.78rem" }}>
          {t("chapter.sourceNote")}: Karnataka State Board · Class 8 Science · original WonderNest
          explanations written for this edition. Not a reproduction of textbook pages.
        </p>
      ) : null}
    </div>
  );
}
