import { useEffect, useMemo, useState, type CSSProperties } from "react";
import { Link, useNavigate } from "react-router-dom";

import { HeroScene, Mascot, SubjectArt } from "../components/Illustrations";
import {
  ApiError,
  api,
  type Chapter,
  type Progress,
  type StudentProfile,
  type Subject,
} from "../lib/api";
import { useAuth } from "../lib/auth";
import { pick, useLanguage } from "../lib/i18n";

type ChapterRow = { chapter: Chapter; subject: Subject };

const GREETINGS = [
  "home.tutor.greet1",
  "home.tutor.greet2",
  "home.tutor.greet3",
  "home.tutor.greet4",
];

const MOTIVATIONS = [
  "home.motivation.1",
  "home.motivation.2",
  "home.motivation.3",
  "home.motivation.4",
];

const SUBJECT_KEYS = ["biology", "physics", "chemistry"] as const;
type SubjectKey = (typeof SUBJECT_KEYS)[number];

/** Stable local day stamp, used to group study activity by calendar day. */
function dayStamp(value: Date): string {
  return `${value.getFullYear()}-${value.getMonth() + 1}-${value.getDate()}`;
}

function parseDay(iso: string | null | undefined): string | null {
  if (!iso) return null;
  const parsed = new Date(iso);
  return Number.isNaN(parsed.getTime()) ? null : dayStamp(parsed);
}

function dayOfYear(date: Date): number {
  const start = new Date(date.getFullYear(), 0, 0);
  return Math.floor((date.getTime() - start.getTime()) / 86_400_000);
}

/** Counts consecutive active days, ending today or yesterday. */
function streakLength(days: Set<string>, today: Date): number {
  const cursor = new Date(today);
  if (!days.has(dayStamp(cursor))) cursor.setDate(cursor.getDate() - 1);
  let streak = 0;
  while (days.has(dayStamp(cursor))) {
    streak += 1;
    cursor.setDate(cursor.getDate() - 1);
  }
  return streak;
}

export default function Dashboard() {
  const { user } = useAuth();
  const { lang, t, setLang } = useLanguage();
  const navigate = useNavigate();

  const [profile, setProfile] = useState<StudentProfile | null>(null);
  const [progress, setProgress] = useState<Progress | null>(null);
  const [chapters, setChapters] = useState<ChapterRow[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [greetingIndex, setGreetingIndex] = useState(0);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const [nextProfile, nextProgress, boards] = await Promise.all([
          api.profile(),
          api.progress(),
          api.boards(),
        ]);
        const board = boards.find((item) => item.code === "KSB") ?? boards[0];
        const classes = board ? await api.classes(board.id) : [];
        const class8 = classes.find((item) => item.level_number === 8) ?? classes[0];
        const subjects = class8 ? await api.subjects(class8.id) : [];
        const grouped = await Promise.all(
          subjects.map(async (subject) => {
            const rows = await api.chapters(subject.id);
            return rows.map((chapter) => ({ chapter, subject }));
          }),
        );
        if (cancelled) return;
        setProfile(nextProfile);
        setProgress(nextProgress);
        setChapters(grouped.flat());
      } catch (err) {
        if (cancelled) return;
        setError(
          err instanceof ApiError
            ? err.message
            : "We could not load your dashboard just now. Please try again.",
        );
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  // The companion greets the student with a rotating, friendly prompt.
  useEffect(() => {
    const timer = window.setInterval(
      () => setGreetingIndex((current) => (current + 1) % GREETINGS.length),
      7000,
    );
    return () => window.clearInterval(timer);
  }, []);

  const derived = useMemo(() => {
    const today = new Date();
    const todayKey = dayStamp(today);
    const rows = progress?.lesson_progress ?? [];
    const attempts = progress?.quiz_attempts_list ?? [];

    const best = new Map<number, number>();
    const latest = new Map<number, string>();
    for (const attempt of attempts) {
      const percent = attempt.total > 0 ? Math.round((attempt.score / attempt.total) * 100) : 0;
      best.set(attempt.chapter_id, Math.max(best.get(attempt.chapter_id) ?? 0, percent));
      const previous = latest.get(attempt.chapter_id);
      if (!previous || new Date(attempt.created_at) > new Date(previous)) {
        latest.set(attempt.chapter_id, attempt.created_at);
      }
    }

    const categoryStats = SUBJECT_KEYS.map((key: SubjectKey) => {
      const inCategory = chapters.filter((row) => row.chapter.category === key);
      const scored = inCategory.filter((row) => best.has(row.chapter.id));
      const percent = scored.length
        ? Math.round(
            scored.reduce((sum, row) => sum + (best.get(row.chapter.id) ?? 0), 0) / scored.length,
          )
        : 0;
      return { key, count: inCategory.length, percent, started: scored.length };
    });

    const todayRows = rows.filter((row) => parseDay(row.completed_at ?? row.opened_at) === todayKey);
    const todayMinutes = Math.round(
      todayRows.reduce((sum, row) => sum + (row.time_spent_seconds ?? 0), 0) / 60,
    );
    const todayLessons = rows.filter((row) => parseDay(row.completed_at) === todayKey).length;

    const activeDays = new Set<string>();
    for (const row of rows) {
      const day = parseDay(row.completed_at ?? row.opened_at);
      if (day) activeDays.add(day);
    }
    for (const attempt of attempts) {
      const day = parseDay(attempt.created_at);
      if (day) activeDays.add(day);
    }

    const recent = [...chapters]
      .sort((a, b) => {
        const aAt = latest.get(a.chapter.id);
        const bAt = latest.get(b.chapter.id);
        if (aAt && bAt) return new Date(bAt).getTime() - new Date(aAt).getTime();
        if (aAt) return -1;
        if (bAt) return 1;
        return a.chapter.number - b.chapter.number;
      })
      .slice(0, 6);

    const goal = profile?.daily_goal_minutes ?? 20;

    return {
      best,
      categoryStats,
      recent,
      todayMinutes,
      todayLessons,
      streak: streakLength(activeDays, today),
      goal,
      goalPercent: Math.min(100, Math.round((todayMinutes / Math.max(goal, 1)) * 100)),
      hasActivity: rows.length > 0 || attempts.length > 0,
      motivationIndex: dayOfYear(today) % MOTIVATIONS.length,
    };
  }, [chapters, profile, progress]);

  const firstChapter = chapters[0]?.chapter;
  const lastStudied = derived.recent.find((row) => derived.best.has(row.chapter.id))?.chapter;
  const diagramChapter =
    chapters.find((row) => row.chapter.visualizations.length > 0)?.chapter ?? firstChapter;
  const studentName = profile?.display_name || user?.display_name || t("home.scientist");
  const totalChapters = derived.categoryStats.reduce((sum, stat) => sum + stat.count, 0);

  if (loading) {
    return (
      <div className="container dashboard">
        <div className="skeleton skeleton-hero" aria-hidden="true" />
        <div className="skeleton-row" aria-hidden="true">
          <div className="skeleton skeleton-card" />
          <div className="skeleton skeleton-card" />
          <div className="skeleton skeleton-card" />
        </div>
      </div>
    );
  }

  return (
    <div className="container dashboard">
      {error && <div className="alert">{error}</div>}

      <section className="hero-panel" aria-labelledby="hero-title">
        <div className="hero-copy">
          <span className="hero-eyebrow">
            <span aria-hidden="true">✦</span> {t("home.eyebrow")}
          </span>
          <h1 id="hero-title" className="hero-title">
            {t("home.greetingPrefix")}, {studentName}! <span aria-hidden="true">👋</span>
          </h1>
          <p className="hero-headline">{t("home.headline")}</p>
          <p className="hero-sub">{t("home.subline")}</p>
          <div className="hero-actions">
            <Link className="btn btn-primary btn-lg" to="/curriculum">
              {t("home.ctaStart")}
            </Link>
            <Link className="btn btn-ghost btn-lg" to="/tutor">
              {t("home.ctaTutor")}
            </Link>
          </div>
          <ul className="hero-facts">
            <li>
              <strong>{progress?.lessons_completed ?? 0}</strong> {t("home.stats.completed")}
            </li>
            <li>
              <strong>{totalChapters}</strong> {t("home.stats.chapters")}
            </li>
            <li>
              <strong>{progress?.quiz_attempts ?? 0}</strong> {t("home.stats.attempts")}
            </li>
          </ul>
        </div>
        <div className="hero-art">
          <HeroScene label={t("home.sceneLabel")} />
        </div>
      </section>

      <section className="companion" aria-labelledby="companion-title">
        <Mascot label={t("home.tutor.mascotLabel")} />
        <div className="companion-body">
          <div className="speech">
            <h2 id="companion-title" className="speech-title">
              {t("home.tutor.title")}
            </h2>
            <p className="speech-text" aria-live="polite">
              {t(GREETINGS[greetingIndex])}
            </p>
            <span className="speech-meta">
              <span className="gemini-dot" aria-hidden="true" />
              {t("home.tutor.gemini")}
            </span>
          </div>
          <div className="companion-actions">
            <Link
              className="action-chip"
              to={`/tutor?q=${encodeURIComponent(t("home.tutor.promptExplain"))}`}
            >
              {t("home.tutor.explain")}
            </Link>
            {lastStudied && (
              <Link className="action-chip" to={`/chapter/${lastStudied.id}`}>
                {t("home.tutor.continue")}
              </Link>
            )}
            {firstChapter && (
              <Link className="action-chip" to={`/quiz/${firstChapter.id}`}>
                {t("home.tutor.quiz")}
              </Link>
            )}
            <button
              type="button"
              className="action-chip"
              onClick={() => {
                setLang("kn");
                navigate(
                  `/tutor?q=${encodeURIComponent("ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು? ಸರಳವಾಗಿ ವಿವರಿಸಿ.")}`,
                );
              }}
            >
              {t("home.tutor.kannada")}
            </button>
            {diagramChapter && (
              <Link className="action-chip" to={`/chapter/${diagramChapter.id}?tab=visualize`}>
                {t("home.tutor.diagram")}
              </Link>
            )}
          </div>
        </div>
      </section>

      <section className="motivation" aria-labelledby="motivation-title">
        <div className="motivation-copy">
          <span className="section-eyebrow">{t("home.motivation.title")}</span>
          <p className="quote" id="motivation-title">
            “{t(MOTIVATIONS[derived.motivationIndex])}”
          </p>
        </div>
        <div className="goal-card">
          <div
            className="goal-ring"
            style={{ "--goal-p": derived.goalPercent } as CSSProperties}
            role="img"
            aria-label={`${derived.goalPercent}% ${t("home.goal.title")}`}
          >
            <span className="goal-ring-inner">{derived.goalPercent}%</span>
          </div>
          <div className="goal-copy">
            <strong>
              {derived.todayMinutes} / {derived.goal} {t("home.goal.minutes")}
            </strong>
            <span className="goal-label">{t("home.goal.time")}</span>
            <span className="goal-label">
              {derived.todayLessons} {t("home.goal.completed")}
            </span>
            <span className="streak">
              {derived.streak > 0
                ? `🔥 ${derived.streak} ${t("home.goal.streak")}`
                : t("home.goal.noStreak")}
            </span>
          </div>
        </div>
      </section>

      <section className="stack-sm" aria-labelledby="subjects-title">
        <div className="section-head">
          <h2 id="subjects-title">{t("home.subjects.title")}</h2>
          <Link className="text-link" to="/curriculum">
            {t("home.subjects.all")}
          </Link>
        </div>
        <div className="subject-grid">
          {derived.categoryStats.map((stat) => (
            <Link
              key={stat.key}
              className={`subject-card subject-card--${stat.key}`}
              to={`/curriculum#cat-${stat.key}`}
            >
              <span className="subject-art">
                <SubjectArt kind={stat.key} label={t(`home.subjects.${stat.key}.title`)} />
              </span>
              <h3 className="subject-name">{t(`home.subjects.${stat.key}.title`)}</h3>
              <p className="subject-body">{t(`home.subjects.${stat.key}.body`)}</p>
              <div className="subject-foot">
                <span>
                  {stat.count} {t("home.stats.chapters")}
                </span>
                <span className="subject-go">
                  {stat.percent > 0 ? `${stat.percent}%` : t("home.subjects.explore")} →{" "}
                </span>
              </div>
              {stat.percent > 0 && (
                <span className="bar" aria-hidden="true">
                  <span style={{ width: `${stat.percent}%` }} />
                </span>
              )}
            </Link>
          ))}
        </div>
      </section>

      <section className="stack-sm" aria-labelledby="continue-title">
        <div className="section-head">
          <h2 id="continue-title">{t("home.continue.title")}</h2>
        </div>
        {derived.hasActivity ? (
          <div className="continue-rail">
            {derived.recent.map(({ chapter, subject }) => {
              const percent = derived.best.get(chapter.id) ?? 0;
              return (
                <article key={chapter.id} className="continue-card">
                  <div className="continue-top">
                    <span className={`category-chip cat-${chapter.category}`}>
                      {t(`home.cat.${chapter.category}`)}
                    </span>
                    <span className="continue-meta">
                      {pick(lang, subject.title_en, subject.title_kn)}
                    </span>
                  </div>
                  <h3 className="continue-title">
                    {pick(lang, chapter.title_en, chapter.title_kn)}
                  </h3>
                  <p className="continue-summary">
                    {pick(lang, chapter.summary_en, chapter.summary_kn)}
                  </p>
                  <span className="bar" aria-hidden="true">
                    <span style={{ width: `${percent}%` }} />
                  </span>
                  <div className="continue-foot">
                    <span className="continue-meta">{percent}%</span>
                    <Link className="btn btn-primary btn-sm" to={`/chapter/${chapter.id}`}>
                      {percent > 0 ? t("home.continue.resume") : t("home.continue.start")}
                    </Link>
                  </div>
                </article>
              );
            })}
          </div>
        ) : (
          <div className="empty-state">
            <span className="empty-emoji" aria-hidden="true">
              🌱
            </span>
            <h3>{t("home.continue.empty")}</h3>
            <p>{t("home.continue.emptyBody")}</p>
            <Link className="btn btn-primary" to="/curriculum">
              {t("home.ctaStart")}
            </Link>
          </div>
        )}
      </section>
    </div>
  );
}
