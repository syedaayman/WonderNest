"""Student endpoints: own profile, progress and preferences. Identity always comes from the token."""

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import require_roles
from app.core.database import get_db
from app.models import Board, ClassLevel, LessonProgress, QuizAttempt, User, UserPreference
from app.repositories import user_repository
from app.schemas.student import (
    LessonProgressOut,
    PreferenceOut,
    ProgressOut,
    QuizAttemptOut,
    StudentProfileOut,
)

router = APIRouter(prefix="/api/students", tags=["students"])


@router.get("/me", response_model=StudentProfileOut)
def get_my_profile(
    user: User = Depends(require_roles("student")),
    db: Session = Depends(get_db),
) -> StudentProfileOut:
    profile = user_repository.get_learner_profile(db, user.id)

    class_id = None
    class_label = None
    board_id = None
    board_name_kn = None
    language_code = None
    daily_goal_minutes = None

    if profile is not None:
        class_id = profile.class_id
        board_id = profile.board_id
        language_code = profile.language_code
        daily_goal_minutes = profile.daily_goal_minutes
        if profile.class_id is not None:
            class_level = db.scalar(select(ClassLevel).where(ClassLevel.id == profile.class_id))
            if class_level is not None:
                class_label = class_level.label
        if profile.board_id is not None:
            board = db.scalar(select(Board).where(Board.id == profile.board_id))
            if board is not None:
                board_name_kn = board.name_kn

    return StudentProfileOut(
        id=user.id,
        username=user.username,
        display_name=user.display_name,
        role=user.role,
        preferred_language=user.preferred_language,
        class_id=class_id,
        class_label=class_label,
        board_id=board_id,
        board_name_kn=board_name_kn,
        language_code=language_code,
        daily_goal_minutes=daily_goal_minutes,
    )


@router.get("/progress", response_model=ProgressOut)
def get_my_progress(
    user: User = Depends(require_roles("student")),
    db: Session = Depends(get_db),
) -> ProgressOut:
    lesson_rows = db.scalars(
        select(LessonProgress).where(LessonProgress.user_id == user.id).order_by(LessonProgress.id)
    ).all()
    attempt_rows = db.scalars(
        select(QuizAttempt)
        .where(QuizAttempt.user_id == user.id)
        .order_by(QuizAttempt.created_at.desc(), QuizAttempt.id.desc())
    ).all()

    lesson_progress = [LessonProgressOut.model_validate(row) for row in lesson_rows]
    quiz_attempts_list = [QuizAttemptOut.model_validate(row) for row in attempt_rows]

    return ProgressOut(
        lessons_opened=len(lesson_rows),
        lessons_completed=sum(1 for row in lesson_rows if row.status == "completed"),
        quiz_attempts=len(attempt_rows),
        lesson_progress=lesson_progress,
        quiz_attempts_list=quiz_attempts_list,
    )


@router.get("/preferences", response_model=list[PreferenceOut])
def get_my_preferences(
    user: User = Depends(require_roles("student")),
    db: Session = Depends(get_db),
) -> list[UserPreference]:
    return list(
        db.scalars(
            select(UserPreference)
            .where(UserPreference.user_id == user.id)
            .order_by(UserPreference.key)
        ).all()
    )
