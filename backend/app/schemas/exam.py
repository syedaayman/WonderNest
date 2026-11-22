"""Schemas for the exam preparation section."""

from pydantic import BaseModel


class ExamQuestionOut(BaseModel):
    """One practice question with its model answer.

    ``answer_*`` and ``explanation_*`` are only revealed in the UI after the student asks for
    them; the API returns them so practice works offline and without a round trip.
    """

    id: str
    type: str
    marks: int
    difficulty: int
    question_en: str
    question_kn: str
    answer_en: str
    answer_kn: str
    explanation_en: str
    explanation_kn: str
    options_en: list[str]
    options_kn: list[str]
    correct_index: int | None = None


class ExamTypeOut(BaseModel):
    key: str
    label_en: str
    label_kn: str
    count: int


class ExamQuestionsOut(BaseModel):
    chapter_id: int
    chapter_number: int
    source_note: str
    total: int
    types: list[ExamTypeOut]
    questions: list[ExamQuestionOut]
