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


class VideoOut(BaseModel):
    """A video recommendation.

    ``video_id`` is only set when the exact video is verified; otherwise the client renders a
    YouTube search link built from ``search_query`` so no invented video ID is ever shown.
    """

    title: str
    language: str
    topic: str
    search_query: str
    video_id: str | None = None


class ChapterOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    number: int
    title_en: str
    title_kn: str
    summary_kn: str | None
    summary_en: str | None
    category: str
    is_enrichment: bool
    visualizations: list[str]
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
    meaning_en: str | None = None


class LessonOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    topic_id: int
    body_kn: str
    body_en: str | None
    key_terms: list[KeyTermOut]
    example_kn: str | None
    example_en: str | None
    is_sample: bool
    source_note: str | None


class LearningObjectiveOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    lesson_id: int
    position: int
    text_kn: str
    text_en: str | None = None


class TopicDetailOut(BaseModel):
    """A topic with its objectives and lesson, as used by the chapter learning page."""

    id: int
    order: int
    title_en: str
    title_kn: str
    objectives: list[LearningObjectiveOut]
    lesson: LessonOut | None


class ChapterContentOut(BaseModel):
    """Everything the chapter learning page needs in a single response."""

    chapter: ChapterOut
    topics: list[TopicDetailOut]
    notes_kn: list[str]
    notes_en: list[str]
    videos: list[VideoOut]
    visualizations: list[str]
    question_count: int


class CategoryOut(BaseModel):
    key: str
    label_en: str
    label_kn: str
