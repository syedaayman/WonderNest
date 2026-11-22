import { useState, type FormEvent } from "react";
import { Link, Navigate, useLocation, useNavigate } from "react-router-dom";

import { ApiError } from "../lib/api";
import { useAuth } from "../lib/auth";

export default function Login() {
  const { user, login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const from = (location.state as { from?: string } | null)?.from ?? "/dashboard";

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  if (user) return <Navigate to={from} replace />;

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    setBusy(true);
    try {
      await login(username.trim(), password);
      navigate(from, { replace: true });
    } catch (err) {
      if (err instanceof ApiError) {
        setError(
          err.status === 401
            ? "That username or password is not correct. Please try again."
            : err.message,
        );
      } else {
        setError("Could not sign you in. Please try again.");
      }
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="container-narrow page">
      <div className="row-between" style={{ marginBottom: "1.4rem" }}>
        <Link to="/" className="brand">
          <span className="brand-mark" aria-hidden="true">
            ✦
          </span>
          WonderNest
        </Link>
        <Link to="/" className="muted" style={{ fontSize: "0.85rem" }}>
          ← Back to home
        </Link>
      </div>

      <div className="card">
        <span className="eyebrow">Student sign in</span>
        <h1 style={{ fontSize: "1.8rem" }}>Welcome back to WonderNest</h1>
        <p className="muted kan" lang="kn">
          ನಿಮ್ಮ ಕಲಿಕೆಯ ಪ್ರಗತಿ ಮತ್ತು AI ಶಿಕ್ಷಕರನ್ನು ಮುಂದುವರಿಸಲು ಲಾಗಿನ್ ಆಗಿ.
        </p>

        <form onSubmit={onSubmit} className="stack" style={{ marginTop: "1rem" }}>
          <div className="field">
            <label className="label" htmlFor="username">
              Username
            </label>
            <input
              id="username"
              className="input"
              autoComplete="username"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              placeholder="demo_student"
              required
            />
          </div>
          <div className="field">
            <label className="label" htmlFor="password">
              Password
            </label>
            <input
              id="password"
              className="input"
              type="password"
              autoComplete="current-password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="••••••••"
              required
            />
          </div>

          {error ? (
            <div className="alert alert-danger" role="alert">
              {error}
            </div>
          ) : null}

          <button className="btn btn-primary btn-block" type="submit" disabled={busy}>
            {busy ? "Signing in…" : "Sign in"}
          </button>
        </form>

        <div className="alert" style={{ marginTop: "1rem" }}>
          <strong>Demo student:</strong> username <code>demo_student</code>, password
          <code> Demo@12345</code>
          <button
            type="button"
            className="btn btn-soft btn-sm"
            style={{ marginTop: "0.6rem" }}
            onClick={() => {
              setUsername("demo_student");
              setPassword("Demo@12345");
            }}
          >
            Fill demo credentials
          </button>
        </div>
      </div>
    </div>
  );
}
