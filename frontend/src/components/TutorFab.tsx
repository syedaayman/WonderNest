import { Link } from "react-router-dom";

import { useLanguage } from "../lib/i18n";

/**
 * Persistent, unobtrusive entry point to the real Gemini tutor.
 * It sits in the corner so it never covers learning content and keeps the
 * student's selected language, because the tutor page reads the same setting.
 */
export function TutorFab() {
  const { t } = useLanguage();
  return (
    <Link className="fab-tutor" to="/tutor" aria-label={t("home.fab")} title={t("home.fab")}>
      <span className="fab-tutor-dot" aria-hidden="true">
        ✦
      </span>
      <span className="fab-tutor-label">{t("home.fab")}</span>
    </Link>
  );
}
