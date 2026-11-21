"""Response schemas for curriculum browsing endpoints."""

from pydantic import BaseModel, ConfigDict


class BoardOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    name_en: str
    name_kn: str


class ClassOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    board_id: int
    level_number: int
    label: str


class SubjectOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    class_id: int
    code: str
    title_en: str
    title_kn: str


class ChapterOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    number: int
    title_en: str
    title_kn: str
    summary_kn: str | None
    estimated_minutes: int
    is_sample: bool
    source_note: str | None


class TopicOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chapter_id: int
    order: int
    title_en: str
    title_kn: str


class KeyTermOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    kn: str
    en: str
    meaning_kn: str


class LessonOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    topic_id: int
    body_kn: str
    key_terms: list[KeyTermOut]
    example_kn: str | None
    is_sample: bool
    source_note: str | None


class LearningObjectiveOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    lesson_id: int
    position: int
    text_kn: str
