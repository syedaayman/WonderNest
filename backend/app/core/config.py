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

    AI_PROVIDER: str = "demo"
    AI_API_KEY: str = ""
    AI_MODEL: str = ""
    AI_BASE_URL: str = ""

    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    MAX_UPLOAD_MB: int = 5

    DEMO_PASSWORD: str = "Demo@12345"

    APP_ENV: str = "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()
