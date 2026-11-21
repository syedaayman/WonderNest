"""Curriculum hierarchy: boards, languages, classes, subjects, chapters, topics, lessons and practice questions."""

from typing import Any

from sqlalchemy import Boolean, CheckConstraint, ForeignKey, Integer, JSON, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    name_en: Mapped[str] = mapped_column(String(200), nullable=False)
    name_kn: Mapped[str] = mapped_column(String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
    name_en: Mapped[str] = mapped_column(String(200), nullable=False)
    name_native: Mapped[str] = mapped_column(String(200), nullable=False)


class ClassLevel(Base):
    __tablename__ = "classes"
    __table_args__ = (UniqueConstraint("board_id", "level_number", name="uq_classes_board_level"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    board_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("boards.id", ondelete="CASCADE"), nullable=False
    )
    level_number: Mapped[int] = mapped_column(Integer, nullable=False)
    label: Mapped[str] = mapped_column(String(40), nullable=False)


class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = (UniqueConstraint("class_id", "code", name="uq_subjects_class_code"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    class_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("classes.id", ondelete="CASCADE"), nullable=False
    )
    code: Mapped[str] = mapped_column(String(40), nullable=False)
    title_en: Mapped[str] = mapped_column(String(200), nullable=False)
    title_kn: Mapped[str] = mapped_column(String(200), nullable=False)


class Chapter(Base):
    __tablename__ = "chapters"
    __table_args__ = (UniqueConstraint("subject_id", "number", name="uq_chapters_subject_number"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("subjects.id", ondelete="CASCADE"), index=True, nullable=False
    )
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    title_kn: Mapped[str] = mapped_column(String(300), nullable=False)
    title_en: Mapped[str] = mapped_column(String(300), nullable=False)
    summary_kn: Mapped[str | None] = mapped_column(Text, nullable=True)
    estimated_minutes: Mapped[int] = mapped_column(Integer, default=30, nullable=False)
    is_sample: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    source_note: Mapped[str | None] = mapped_column(Text, nullable=True)


class Topic(Base):
    __tablename__ = "topics"
    __table_args__ = (UniqueConstraint("chapter_id", "order", name="uq_topics_chapter_order"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chapter_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("chapters.id", ondelete="CASCADE"), index=True, nullable=False
    )
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    title_kn: Mapped[str] = mapped_column(String(300), nullable=False)
    title_en: Mapped[str] = mapped_column(String(300), nullable=False)


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("topics.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    body_kn: Mapped[str] = mapped_column(Text, nullable=False)
    # List of {"kn": str, "en": str, "meaning_kn": str}
    key_terms: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list, nullable=False)
    example_kn: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_sample: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    source_note: Mapped[str | None] = mapped_column(Text, nullable=True)


class PracticeQuestion(Base):
    __tablename__ = "practice_questions"
    __table_args__ = (
        CheckConstraint("question_type IN ('mcq', 'true_false')", name="ck_practice_questions_type"),
        CheckConstraint("difficulty BETWEEN 1 AND 3", name="ck_practice_questions_difficulty"),
        CheckConstraint("correct_index >= 0", name="ck_practice_questions_correct_index"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chapter_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("chapters.id", ondelete="CASCADE"), index=True, nullable=False
    )
    topic_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("topics.id", ondelete="SET NULL"), nullable=True
    )
    question_type: Mapped[str] = mapped_column(String(20), nullable=False)
    question_kn: Mapped[str] = mapped_column(Text, nullable=False)
    # List of option strings
    options_kn: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    correct_index: Mapped[int] = mapped_column(Integer, nullable=False)
    explanation_kn: Mapped[str | None] = mapped_column(Text, nullable=True)
    difficulty: Mapped[int] = mapped_column(Integer, default=1, nullable=False)


class LearningObjective(Base):
    __tablename__ = "learning_objectives"
    __table_args__ = (
        UniqueConstraint("topic_id", "position", name="uq_learning_objectives_topic_position"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("topics.id", ondelete="CASCADE"), index=True, nullable=False
    )
    position: Mapped[int] = mapped_column(Integer, nullable=False)
    text_kn: Mapped[str] = mapped_column(Text, nullable=False)

