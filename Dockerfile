# WonderNest: React SPA built with Vite, served by the FastAPI backend that also hosts
# the Gemini powered AI tutor. The Gemini key is supplied at runtime through the hosting
# environment and is never baked into an image layer.

# ---------- Stage 1: build the frontend ----------
FROM node:24-alpine AS frontend

WORKDIR /build/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN if [ -f package-lock.json ]; then npm ci --no-audit --no-fund; else npm install --no-audit --no-fund; fi
COPY frontend/ ./
RUN npm run build

# ---------- Stage 2: python runtime ----------
FROM python:3.13-alpine AS runtime

RUN echo "os-refresh 2026-11-22" && apk upgrade --no-cache

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DATABASE_URL=sqlite:////app/data/wondernest.db

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY backend/ ./
# main.py resolves the SPA from <repo root>/frontend/dist, which is /frontend/dist here.
COPY --from=frontend /build/frontend/dist /frontend/dist

RUN adduser -D -u 10001 appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Migrate, load the demo curriculum (idempotent), then serve the API and the SPA.
CMD ["sh", "-c", "alembic upgrade head && python -m app.curriculum.cli && exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
