"""Response schemas for student profile, progress and preference endpoints."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class StudentProfileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    display_name: str
    role: str
    preferred_language: str
    class_id: int | None
    class_label: str | None
    board_id: int | None
    board_name_kn: str | None
    language_code: str | None
    daily_goal_minutes: int | None


class LessonProgressOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    lesson_id: int
    status: str
    opened_at: datetime
    completed_at: datetime | None
    time_spent_seconds: int


class LessonProgressIn(BaseModel):
    """Body for recording lesson progress. The student id always comes from the token."""

    status: Literal["opened", "completed"] = "completed"
    time_spent_seconds: int = Field(default=0, ge=0, le=36_000)


class QuizAttemptOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chapter_id: int
    score: int
    total: int
    created_at: datetime


class ProgressOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    lessons_opened: int
    lessons_completed: int
    quiz_attempts: int
    lesson_progress: list[LessonProgressOut]
    quiz_attempts_list: list[QuizAttemptOut]


class PreferenceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    key: str
    value: str
