"""WonderNest FastAPI application entry point."""

import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError

from app.api.ai_tutor import router as ai_tutor_router
from app.api.auth import router as auth_router
from app.api.curriculum import router as curriculum_router
from app.api.quiz import router as quiz_router
from app.api.students import router as students_router
from app.core.config import get_settings

logger = logging.getLogger("wondernest")

settings = get_settings()

app = FastAPI(title="WonderNest API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(auth_router)
app.include_router(students_router)
app.include_router(curriculum_router)
app.include_router(quiz_router)
app.include_router(ai_tutor_router)

# Built single-page app, served by the same FastAPI process so the browser never needs a
# separate origin (and never sees any backend secret).
FRONTEND_DIST = Path(__file__).resolve().parents[2] / "frontend" / "dist"


@app.get("/api/health")
def health() -> dict[str, object]:
    from app.services import ai_tutor_service

    return {
        "status": "ok",
        "app": "WonderNest",
        "ai_tutor_configured": ai_tutor_service.is_configured(),
    }


if FRONTEND_DIST.is_dir():
    if (FRONTEND_DIST / "assets").is_dir():
        app.mount(
            "/assets", StaticFiles(directory=FRONTEND_DIST / "assets"), name="assets"
        )

    @app.get("/{full_path:path}", include_in_schema=False)
    def serve_frontend(full_path: str) -> FileResponse | JSONResponse:
        if full_path.startswith("api/"):
            return JSONResponse(status_code=404, content={"detail": "Not found."})
        candidate = (FRONTEND_DIST / full_path).resolve()
        if full_path and candidate.is_file() and FRONTEND_DIST in candidate.parents:
            return FileResponse(candidate)
        return FileResponse(FRONTEND_DIST / "index.html")

else:

    @app.get("/", include_in_schema=False)
    def root() -> dict[str, str]:
        return {
            "app": "WonderNest API",
            "docs": "/docs",
            "note": "Build the frontend with `npm install && npm run build` in frontend/.",
        }


@app.exception_handler(SQLAlchemyError)
async def handle_database_error(request: Request, exc: SQLAlchemyError) -> JSONResponse:
    logger.error("Database error on %s %s: %s", request.method, request.url.path, type(exc).__name__)
    return JSONResponse(
        status_code=500,
        content={"detail": "A database error occurred. Please try again."},
    )
