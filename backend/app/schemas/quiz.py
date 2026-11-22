"""Request and response schemas for chapter quizzes and results.

Every question and explanation is returned in both languages so the student can switch
language mid-quiz without losing their place.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class QuizQuestionOut(BaseModel):
    """A quiz question without the correct answer, so the answer stays on the server."""

    id: int
    question_type: str
    question_kn: str
    question_en: str | None
    options_kn: list[str]
    options_en: list[str]
    difficulty: int


class QuizOut(BaseModel):
    chapter_id: int
    chapter_title_kn: str
    chapter_title_en: str
    category: str
    total: int
    questions: list[QuizQuestionOut]


class QuizAnswerIn(BaseModel):
    question_id: int = Field(ge=1)
    selected_index: int | None = Field(default=None, ge=0)


class QuizSubmitRequest(BaseModel):
    answers: list[QuizAnswerIn] = Field(default_factory=list, max_length=50)


class QuizAnswerResultOut(BaseModel):
    question_id: int
    selected_index: int | None
    correct_index: int
    is_correct: bool
    explanation_kn: str | None
    explanation_en: str | None
    question_kn: str
    question_en: str | None
    options_kn: list[str]
    options_en: list[str]


class QuizResultOut(BaseModel):
    attempt_id: int
    chapter_id: int
    chapter_title_kn: str
    chapter_title_en: str
    score: int
    total: int
    created_at: datetime
    answers: list[QuizAnswerResultOut]
