"""Response schemas for student profile, progress and preference endpoints."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


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
