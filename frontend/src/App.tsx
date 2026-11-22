import type { ReactNode } from "react";
import { Link, NavLink, Navigate, Outlet, Route, Routes, useLocation } from "react-router-dom";

import { useAuth } from "./lib/auth";
import { LanguageProvider, useLanguage } from "./lib/i18n";
import Chapter from "./pages/Chapter";
import Curriculum from "./pages/Curriculum";
import Dashboard from "./pages/Dashboard";
import Landing from "./pages/Landing";
import LessonPage from "./pages/Lesson";
import Login from "./pages/Login";
import ProgressPage from "./pages/Progress";
import QuizPage from "./pages/Quiz";
import Results from "./pages/Results";
import Tutor from "./pages/Tutor";
import { TutorFab } from "./components/TutorFab";

function FullPageLoader({ label = "Loading WonderNest…" }: { label?: string }) {
  return (
    <div className="loader">
      <div className="spinner" />
      <span>{label}</span>
    </div>
  );
}

function RequireAuth({ children }: { children: ReactNode }) {
  const { user, loading } = useAuth();
  const location = useLocation();

  if (loading) return <FullPageLoader label="Checking your session…" />;
  if (!user) {
    return <Navigate to="/login" replace state={{ from: location.pathname + location.search }} />;
  }
  return <>{children}</>;
}

function LanguageToggle() {
  const { lang, setLang } = useLanguage();
  return (
    <div className="segmented segmented-lang" role="group" aria-label="Language">
      <button
        type="button"
        className={lang === "en" ? "segmented-item active" : "segmented-item"}
        onClick={() => setLang("en")}
        aria-pressed={lang === "en"}
      >
        EN
      </button>
      <button
        type="button"
        className={lang === "kn" ? "segmented-item active" : "segmented-item"}
        onClick={() => setLang("kn")}
        aria-pressed={lang === "kn"}
      >
        ಕನ್ನಡ
      </button>
    </div>
  );
}

function Shell() {
  const { user, logout } = useAuth();
  const { t } = useLanguage();
  const initials = (user?.display_name ?? "W").trim().slice(0, 1).toUpperCase();

  const navClass = ({ isActive }: { isActive: boolean }) =>
    isActive ? "nav-link active" : "nav-link";

  return (
    <>
      <header className="topbar">
        <div className="container topbar-inner">
          <Link to="/dashboard" className="brand">
            <span className="brand-mark" aria-hidden="true">
              ✦
            </span>
            WonderNest
          </Link>
          <nav className="nav-links" aria-label="Main">
            <NavLink to="/dashboard" className={navClass}>
              {t("nav.dashboard")}
            </NavLink>
            <NavLink to="/curriculum" className={navClass}>
              {t("nav.curriculum")}
            </NavLink>
            <NavLink to="/tutor" className={navClass}>
              {t("nav.tutor")}
            </NavLink>
            <NavLink to="/progress" className={navClass}>
              {t("nav.progress")}
            </NavLink>
          </nav>
          <div className="nav-user">
            <LanguageToggle />
            <span className="avatar" aria-hidden="true">
              {initials}
            </span>
            <span className="muted nav-user-name">{user?.display_name}</span>
            <button type="button" className="btn btn-ghost btn-sm" onClick={logout}>
              {t("nav.logout")}
            </button>
          </div>
        </div>
      </header>
      <main className="page">
        <Outlet />
      </main>
      <footer className="footer">
        <div className="container row-between">
          <span>
            WonderNest · Karnataka State Board · Class 8 Science · AI explanations are
            AI-generated study support, not official textbook content.
          </span>
        </div>
      </footer>
          <TutorFab />
    </>
  );
}

export default function App() {
  return (
    <LanguageProvider>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route
          element={
            <RequireAuth>
              <Shell />
            </RequireAuth>
          }
        >
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/curriculum" element={<Curriculum />} />
          <Route path="/chapter/:chapterId" element={<Chapter />} />
          <Route path="/lesson/:lessonId" element={<LessonPage />} />
          <Route path="/quiz/:chapterId" element={<QuizPage />} />
          <Route path="/results/:attemptId" element={<Results />} />
          <Route path="/progress" element={<ProgressPage />} />
          <Route path="/tutor" element={<Tutor />} />
        </Route>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </LanguageProvider>
  );
}
