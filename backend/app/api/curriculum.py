"""Curriculum browsing endpoints: boards, classes, subjects, chapters, topics and lessons."""

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.curriculum import units as curriculum_units
from app.models import Board, Chapter, ClassLevel, Lesson, PracticeQuestion, Subject, Topic, User
from app.models.curriculum import LearningObjective
from app.schemas.curriculum import (
    BoardOut,
    CategoryOut,
    ChapterContentOut,
    ChapterOut,
    ClassOut,
    KeyTermOut,
    LearningObjectiveOut,
    LessonOut,
    SubjectOut,
    TopicDetailOut,
    TopicOut,
    VideoOut,
)

router = APIRouter(prefix="/api/curriculum", tags=["curriculum"])


def _lesson_out(lesson: Lesson) -> LessonOut:
    key_terms = [
        KeyTermOut(
            kn=term.get("kn", ""),
            en=term.get("en", ""),
            meaning_kn=term.get("meaning_kn", ""),
            meaning_en=term.get("meaning_en"),
        )
        for term in (lesson.key_terms or [])
    ]
    return LessonOut(
        id=lesson.id,
        topic_id=lesson.topic_id,
        body_kn=lesson.body_kn,
        body_en=lesson.body_en,
        key_terms=key_terms,
        example_kn=lesson.example_kn,
        example_en=lesson.example_en,
        is_sample=lesson.is_sample,
        source_note=lesson.source_note,
    )


def _objective_out(objective: LearningObjective, lesson_id: int) -> LearningObjectiveOut:
    return LearningObjectiveOut(
        id=objective.id,
        lesson_id=lesson_id,
        position=objective.position,
        text_kn=objective.text_kn,
        text_en=objective.text_en,
    )


@router.get("/boards", response_model=list[BoardOut])
def list_boards(
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[Board]:
    return list(
        db.scalars(select(Board).where(Board.is_active.is_(True)).order_by(Board.id)).all()
    )


@router.get("/boards/{board_id}/classes", response_model=list[ClassOut])
def list_classes(
    board_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[ClassLevel]:
    board = db.scalar(select(Board).where(Board.id == board_id, Board.is_active.is_(True)))
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found.")
    return list(
        db.scalars(
            select(ClassLevel)
            .where(ClassLevel.board_id == board_id)
            .order_by(ClassLevel.level_number)
        ).all()
    )


@router.get("/classes/{class_id}/subjects", response_model=list[SubjectOut])
def list_subjects(
    class_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[Subject]:
    class_level = db.scalar(select(ClassLevel).where(ClassLevel.id == class_id))
    if class_level is None:
        raise HTTPException(status_code=404, detail="Class not found.")
    return list(
        db.scalars(
            select(Subject).where(Subject.class_id == class_id).order_by(Subject.id)
        ).all()
    )


@router.get("/categories", response_model=list[CategoryOut])
def list_categories() -> list[CategoryOut]:
    """The subject groupings the curriculum page renders, in display order."""
    return [
        CategoryOut(
            key=category["key"],
            label_en=category["label_en"],
            label_kn=category["label_kn"],
        )
        for category in curriculum_units.CATEGORIES
    ]


@router.get("/subjects/{subject_id}/chapters", response_model=list[ChapterOut])
def list_chapters(
    subject_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[Chapter]:
    subject = db.scalar(select(Subject).where(Subject.id == subject_id))
    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found.")
    return list(
        db.scalars(
            select(Chapter).where(Chapter.subject_id == subject_id).order_by(Chapter.number)
        ).all()
    )


@router.get("/chapters/{chapter_id}/content", response_model=ChapterContentOut)
def get_chapter_content(
    chapter_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ChapterContentOut:
    """One request with everything the chapter learning page needs.

    Bilingual text is returned side by side so the client can switch language without a
    round trip, and the page works offline of the language toggle.
    """
    chapter = db.scalar(select(Chapter).where(Chapter.id == chapter_id))
    if chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found.")

    topics = db.scalars(
        select(Topic).where(Topic.chapter_id == chapter_id).order_by(Topic.order)
    ).all()

    topic_details: list[TopicDetailOut] = []
    for topic in topics:
        lesson = db.scalar(select(Lesson).where(Lesson.topic_id == topic.id))
        objectives = db.scalars(
            select(LearningObjective)
            .where(LearningObjective.topic_id == topic.id)
            .order_by(LearningObjective.position)
        ).all()
        topic_details.append(
            TopicDetailOut(
                id=topic.id,
                order=topic.order,
                title_en=topic.title_en,
                title_kn=topic.title_kn,
                objectives=[
                    _objective_out(objective, lesson.id if lesson else 0)
                    for objective in objectives
                ],
                lesson=_lesson_out(lesson) if lesson else None,
            )
        )

    question_count = db.scalar(
        select(func.count())
        .select_from(PracticeQuestion)
        .where(PracticeQuestion.chapter_id == chapter_id)
    ) or 0

    return ChapterContentOut(
        chapter=ChapterOut.model_validate(chapter),
        topics=topic_details,
        notes_kn=list(chapter.notes_kn or []),
        notes_en=list(chapter.notes_en or []),
        videos=[
            VideoOut(
                title=video.get("title", ""),
                language=video.get("language", "en"),
                topic=video.get("topic", ""),
                search_query=video.get("search_query", ""),
                video_id=video.get("video_id"),
            )
            for video in (chapter.videos or [])
        ],
        visualizations=list(chapter.visualizations or []),
        question_count=question_count,
    )


@router.get("/chapters/{chapter_id}/topics", response_model=list[TopicOut])
def list_topics(
    chapter_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[Topic]:
    chapter = db.scalar(select(Chapter).where(Chapter.id == chapter_id))
    if chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found.")
    return list(
        db.scalars(
            select(Topic).where(Topic.chapter_id == chapter_id).order_by(Topic.order)
        ).all()
    )


@router.get("/topics/{topic_id}/lessons", response_model=list[LessonOut])
def list_topic_lessons(
    topic_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[LessonOut]:
    topic = db.scalar(select(Topic).where(Topic.id == topic_id))
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found.")
    lessons = db.scalars(select(Lesson).where(Lesson.topic_id == topic_id)).all()
    return [_lesson_out(lesson) for lesson in lessons]


@router.get("/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(
    lesson_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> LessonOut:
    lesson = db.scalar(select(Lesson).where(Lesson.id == lesson_id))
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found.")
    return _lesson_out(lesson)


@router.get("/lessons/{lesson_id}/objectives", response_model=list[LearningObjectiveOut])
def list_lesson_objectives(
    lesson_id: int = Path(ge=1),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[LearningObjectiveOut]:
    lesson = db.scalar(select(Lesson).where(Lesson.id == lesson_id))
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found.")
    objectives = db.scalars(
        select(LearningObjective)
        .where(LearningObjective.topic_id == lesson.topic_id)
        .order_by(LearningObjective.position.asc())
    ).all()
    # Objectives belong to the topic; they are reported against this lesson, which is the topic's lesson.
    return [_objective_out(objective, lesson.id) for objective in objectives]
