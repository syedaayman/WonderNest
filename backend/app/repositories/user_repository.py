"""Read-only queries for users and learner profiles."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import LearnerProfile, User


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.scalar(select(User).where(User.username == username))


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.scalar(select(User).where(User.id == user_id))


def get_learner_profile(db: Session, user_id: int) -> LearnerProfile | None:
    return db.scalar(select(LearnerProfile).where(LearnerProfile.user_id == user_id))
