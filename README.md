# WonderNest

An AI tutor for Karnataka State Board Class 8 Science (Kannada + English), built on FastAPI,
SQLAlchemy, React and Google Gemini.

* **Backend** — `backend/` (FastAPI, JWT auth, SQLAlchemy + Alembic, Gemini tutor service)
* **Frontend** — `frontend/` (React + Vite SPA, served by FastAPI in production)
* **Container** — `Dockerfile` builds the SPA and runs migrations + demo seed on start

## Student journey

Landing → Login → Dashboard → Curriculum → Lesson → Quiz → Results → Progress, plus the
Gemini-powered **AI Tutor** page.

Demo student: `demo` / `Demo@12345` (override with `DEMO_PASSWORD`).

## The AI tutor

`POST /api/ai/tutor/chat` (JWT required, student role only):

* Google Gemini via the `google-genai` SDK; model configured by `GEMINI_MODEL`
  (default `gemini-3.8-flash`, automatic fallback across available Flash models).
* Student identity comes from the JWT — the request body never carries a user id.
* Answers in Kannada or English, adapts to `beginner` / `class8` / `advanced`, uses the
  current chapter/topic/lesson as context, gives everyday examples, glosses hard terms,
  generates practice questions, hints instead of answers, and asks a check-understanding
  question.
* Guardrails: 1200-character message limit, 12-request/60s sliding window per student,
  12-message history cap, 30s provider timeout.
* The API key stays in the backend process. Logs record user id, model, latency and token
  counts — never the key or the student's question text.
* Missing key → `503 ai_not_configured`; rejected key → `503 ai_invalid_key`; quota → `429
  ai_quota_exceeded`; rate limit → `429 ai_rate_limited` with `Retry-After`. No fake answers
  are ever substituted.

Other tutor endpoints: `GET /api/ai/tutor/status` (configuration/model report) and
`GET /api/ai/tutor/suggestions` (the six suggested prompts).

## Local setup

```bash
# backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then set GEMINI_API_KEY
alembic upgrade head
python -m app.curriculum.cli  # idempotent demo seed
uvicorn app.main:app --reload --port 8000

# frontend (second terminal)
cd frontend
npm install
npm run dev                   # http://localhost:5173, proxies /api to :8000
```

## Environment variables

| Name | Required | Purpose |
| --- | --- | --- |
| `GEMINI_API_KEY` | yes for the tutor | Google AI Studio key; backend only |
| `GEMINI_MODEL` | no | Default `gemini-3.8-flash` |
| `GEMINI_TIMEOUT_SECONDS` | no | Provider timeout (default 30) |
| `GEMINI_MAX_OUTPUT_TOKENS` | no | Response cap (default 1024) |
| `AI_RATE_LIMIT_REQUESTS` / `AI_RATE_LIMIT_WINDOW_SECONDS` | no | Per-student budget (12 / 60) |
| `AI_MAX_HISTORY_MESSAGES` / `AI_MAX_MESSAGE_CHARS` | no | Context and input limits (12 / 1200) |
| `JWT_SECRET` | yes in production | Token signing key (≥32 chars) |
| `DATABASE_URL` | no | Defaults to SQLite at `data/wondernest.db` |
| `DEMO_PASSWORD` | no | Password for the seeded demo student |
| `CORS_ORIGINS` | no | Only needed for a separate frontend origin |

Locally: put them in `backend/.env`. On AppJet: **Settings → Environment variables**
(`GEMINI_API_KEY`, `JWT_SECRET`). Never commit real values — `.env` is git-ignored.

## Deploying

The `Dockerfile` is the whole deployment contract: it builds the SPA, installs the pinned
Python dependencies on Alpine, runs `alembic upgrade head` plus the idempotent seed, then
serves `app.main:app` with `uvicorn` on `0.0.0.0:$PORT` (8000). The FastAPI process serves
both `/api/*` and the SPA, so no separate frontend host or API base URL is needed.

1. Set `GEMINI_API_KEY` and a strong `JWT_SECRET` in Settings → Environment variables.
2. Deploy the `appjet` branch.
3. Verify: `GET /api/health` should report `ai_tutor_configured: true`, then log in as the
   demo student and ask a Kannada question on the AI Tutor page.

SQLite lives inside the container, so on the Free plan the database (and quiz progress)
resets when the app is redeployed. A persistent disk (Starter/Pro) or a managed Postgres
`DATABASE_URL` makes it durable.

## Verifying a real Gemini call

```bash
cd backend
GEMINI_API_KEY=... python -m scripts.verify_gemini "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?"
```

It prints the model, latency and a reply preview, and exits non-zero when the call fails.

## Tests

```bash
cd backend && python -m pytest tests -q     # 71 tests
cd frontend && npm run typecheck && npm run build
```

The tutor tests replace only the single `_call_model` seam, so they cover auth, prompt
context, limits and every provider error path without spending Gemini quota.
