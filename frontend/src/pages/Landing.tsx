import { Link } from "react-router-dom";

import { useAuth } from "../lib/auth";

const features = [
  {
    icon: "🤖",
    title: "Gemini AI tutor",
    body: "Ask anything about Class 8 Science in Kannada or English. Real Gemini responses, with hints instead of answers.",
  },
  {
    icon: "📚",
    title: "Curriculum, chapter by chapter",
    body: "Karnataka State Board · Class 8 · Science. Every lesson has key terms, an everyday example and learning objectives.",
  },
  {
    icon: "🎯",
    title: "Practice quizzes",
    body: "Chapter quizzes with instant scoring, Kannada explanations and a record of every attempt.",
  },
  {
    icon: "📈",
    title: "Visible progress",
    body: "Lessons opened, lessons completed, quiz scores - all saved to your student profile.",
  },
];

export default function Landing() {
  const { user } = useAuth();

  return (
    <>
      <header className="topbar">
        <div className="container topbar-inner">
          <Link to="/" className="brand">
            <span className="brand-mark" aria-hidden="true">
              ✦
            </span>
            WonderNest
          </Link>
          <nav className="nav-links" aria-label="Landing">
            <a className="nav-link" href="#features">
              Features
            </a>
            <a className="nav-link" href="#journey">
              How it works
            </a>
          </nav>
          <div className="nav-user">
            <Link className="btn btn-ghost btn-sm" to="/login">
              Log in
            </Link>
            <Link className="btn btn-primary btn-sm" to={user ? "/dashboard" : "/login"}>
              {user ? "Go to dashboard" : "Start learning"}
            </Link>
          </div>
        </div>
      </header>

      <section className="hero">
        <div className="container hero-inner">
          <div>
            <span className="badge badge-gemini">✦ Powered by Google Gemini</span>
            <h1 style={{ marginTop: "0.8rem" }}>
              Learn Science in the language you think in.
            </h1>
            <p className="lead kan" lang="kn">
              ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ 8ನೇ ತರಗತಿಯ ವಿಜ್ಞಾನವನ್ನು ಸರಳವಾಗಿ ಕಲಿಯಿರಿ — ನಿಮ್ಮ
              ಸ್ವಂತ AI ಶಿಕ್ಷಕರೊಂದಿಗೆ.
            </p>
            <p className="lead">
              WonderNest pairs the Karnataka State Board Class 8 Science syllabus with a
              real Gemini tutor that explains concepts simply, uses everyday examples and
              gives hints instead of answers.
            </p>
            <div className="row" style={{ marginTop: "1.2rem" }}>
              <Link className="btn btn-primary" to={user ? "/dashboard" : "/login"}>
                Start learning free
              </Link>
              <Link className="btn btn-ghost" to={user ? "/tutor" : "/login"}>
                Try the AI tutor →
              </Link>
            </div>
            <p className="muted" style={{ marginTop: "0.9rem", fontSize: "0.85rem" }}>
              Demo student · <code>demo_student</code> · password from your backend
              <code> DEMO_PASSWORD</code>
            </p>
          </div>

          <div className="hero-preview" aria-label="Example tutor conversation">
            <div className="row-between">
              <span className="side-title">WonderNest AI Tutor</span>
              <span className="badge badge-gemini">Gemini</span>
            </div>
            <div className="bubble bubble-user">ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?</div>
            <div className="bubble bubble-ai">
              <strong>ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ</strong> ಎಂದರೆ ಸಸ್ಯಗಳು ಸೂರ್ಯನ ಬೆಳಕನ್ನು ಬಳಸಿ ತಮ್ಮ
              ಆಹಾರವನ್ನು ತಯಾರಿಸುವ ಕ್ರಿಯೆ.
              <br />
              <span className="muted">ಉದಾಹರಣೆ: ಬಿಸಿಲಿನಲ್ಲಿ ಇಟ್ಟ ಸಸ್ಯ ಹಸಿರಾಗಿರುತ್ತದೆ.</span>
            </div>
            <div className="bubble bubble-user">Can you give me 5 practice questions?</div>
            <div className="bubble bubble-ai">
              Here are 5 questions on photosynthesis - try them first, then I&apos;ll give
              you a hint. 🌱
            </div>
            <div className="typing" aria-hidden="true">
              <span />
              <span />
              <span />
            </div>
          </div>
        </div>
      </section>

      <section className="container page" id="features">
        <span className="eyebrow">What you get</span>
        <h2 style={{ marginBottom: "1.2rem" }}>A complete study companion, not a chatbot demo</h2>
        <div className="grid grid-4">
          {features.map((feature) => (
            <article className="card" key={feature.title}>
              <div style={{ fontSize: "1.5rem", marginBottom: "0.4rem" }} aria-hidden="true">
                {feature.icon}
              </div>
              <h3>{feature.title}</h3>
              <p className="muted" style={{ marginBottom: 0, fontSize: "0.92rem" }}>
                {feature.body}
              </p>
            </article>
          ))}
        </div>
      </section>

      <section className="container page" id="journey" style={{ paddingTop: 0 }}>
        <div className="card">
          <span className="eyebrow">The student journey</span>
          <h2>From first question to finished chapter</h2>
          <div className="grid grid-4" style={{ marginTop: "0.8rem" }}>
            {[
              ["1", "Log in", "Your JWT session keeps your progress private."],
              ["2", "Pick a chapter", "Photosynthesis, force, cells and more."],
              ["3", "Read & ask", "Open the lesson, then ask the tutor to explain it."],
              ["4", "Quiz & track", "Score the chapter and watch your progress grow."],
            ].map(([step, title, body]) => (
              <div className="stat" key={step}>
                <div className="badge" style={{ marginBottom: "0.4rem" }}>
                  Step {step}
                </div>
                <strong>{title}</strong>
                <p className="muted" style={{ margin: "0.2rem 0 0", fontSize: "0.88rem" }}>
                  {body}
                </p>
              </div>
            ))}
          </div>
          <p className="muted" style={{ marginTop: "1rem", marginBottom: 0, fontSize: "0.85rem" }}>
            AI answers are generated for learning support. They are not official textbook
            material and may contain mistakes - always cross-check with your textbook.
          </p>
        </div>
      </section>
    </>
  );
}
