"""Application settings loaded from environment variables and an optional .env file."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str = "sqlite:///./data/wondernest.db"

    JWT_SECRET: str = "dev-only-change-me-please-32-chars-min"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_MINUTES: int = 30
    REFRESH_TOKEN_DAYS: int = 14

    # --- AI tutor (Google Gemini) -------------------------------------------------
    # The key is read from the backend environment only and is never sent to the browser.
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-3.8-flash"
    # Tried in order when the primary model is missing or temporarily overloaded (503).
    GEMINI_FALLBACK_MODELS: str = "gemini-3.6-flash,gemini-3.5-flash,gemini-3.1-flash-lite"
    GEMINI_TIMEOUT_SECONDS: float = 30.0

    # Narration (text-to-speech). The model name is a preference: the service discovers the
    # TTS models the key can actually reach and only falls back to this name if it exists.
    GEMINI_TTS_MODEL: str = "gemini-3.8-flash-tts"
    GEMINI_TTS_VOICE_KN: str = "Kore"
    GEMINI_TTS_VOICE_EN: str = "Puck"
    GEMINI_TTS_TIMEOUT_SECONDS: float = 25.0
    GEMINI_MAX_OUTPUT_TOKENS: int = 1024

    # Per-student request budget for the tutor endpoint.
    AI_RATE_LIMIT_REQUESTS: int = 12
    AI_RATE_LIMIT_WINDOW_SECONDS: int = 60

    # Conversation context handling.
    AI_MAX_HISTORY_MESSAGES: int = 12
    AI_MAX_MESSAGE_CHARS: int = 1200

    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    MAX_UPLOAD_MB: int = 5

    DEMO_PASSWORD: str = "Demo@12345"

    APP_ENV: str = "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()
