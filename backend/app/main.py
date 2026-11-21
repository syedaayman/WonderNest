"""WonderNest FastAPI application entry point."""

import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.api.auth import router as auth_router
from app.api.curriculum import router as curriculum_router
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


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "WonderNest"}


@app.exception_handler(SQLAlchemyError)
async def handle_database_error(request: Request, exc: SQLAlchemyError) -> JSONResponse:
    logger.error("Database error on %s %s: %s", request.method, request.url.path, type(exc).__name__)
    return JSONResponse(
        status_code=500,
        content={"detail": "A database error occurred. Please try again."},
    )
