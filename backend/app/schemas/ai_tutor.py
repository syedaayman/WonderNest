"""Request and response schemas for the Gemini powered AI tutor."""

from typing import Literal

from pydantic import BaseModel, Field

LanguageCode = Literal["kn", "en"]
LearningLevel = Literal["beginner", "class8", "advanced"]
HistoryRole = Literal["user", "assistant"]


class TutorHistoryMessage(BaseModel):
    """One earlier turn supplied by the client for a stateless conversation."""

    role: HistoryRole
    content: str = Field(min_length=1, max_length=1200)


class TutorChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1200)
    language: LanguageCode = "kn"
    level: LearningLevel = "class8"
    # Optional curriculum context. Ids are validated against the database; the student
    # identity always comes from the access token, never from the request body.
    chapter_id: int | None = Field(default=None, ge=1)
    topic_id: int | None = Field(default=None, ge=1)
    lesson_id: int | None = Field(default=None, ge=1)
    conversation_id: int | None = Field(default=None, ge=1)
    history: list[TutorHistoryMessage] = Field(default_factory=list, max_length=12)


class TutorUsage(BaseModel):
    prompt_tokens: int | None = None
    response_tokens: int | None = None
    total_tokens: int | None = None


class TutorChatResponse(BaseModel):
    reply: str
    conversation_id: int
    provider: str = "google-gemini"
    model: str
    language: LanguageCode
    latency_ms: int
    usage: TutorUsage | None = None


class TutorStatusOut(BaseModel):
    """Non-secret configuration state, so the UI can explain a missing key."""

    configured: bool
    provider: str = "google-gemini"
    model: str
    message: str
    rate_limit_requests: int
    rate_limit_window_seconds: int
    max_message_chars: int


class SuggestedPrompt(BaseModel):
    id: str
    label: str
    label_kn: str
    prompt: str
    language: LanguageCode
    topic: str


class SuggestedPromptsOut(BaseModel):
    prompts: list[SuggestedPrompt]
