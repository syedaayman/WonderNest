"""ORM models. Importing this package registers every table on ``Base.metadata``."""

from app.models.curriculum import (
    Board,
    Chapter,
    ClassLevel,
    Language,
    LearningObjective,
    Lesson,
    PracticeQuestion,
    Subject,
    Topic,
)
from app.models.learning import (
    AIConversation,
    AIMessage,
    LessonProgress,
    MistakeRecord,
    QuizAnswer,
    QuizAttempt,
)
from app.models.preferences import UserPreference
from app.models.sync import SyncRecord
from app.models.user import LearnerProfile, RefreshToken, User

__all__ = [
    "AIConversation",
    "AIMessage",
    "Board",
    "Chapter",
    "ClassLevel",
    "LearnerProfile",
    "Language",
    "LearningObjective",
    "Lesson",
    "LessonProgress",
    "MistakeRecord",
    "PracticeQuestion",
    "QuizAnswer",
    "QuizAttempt",
    "RefreshToken",
    "Subject",
    "SyncRecord",
    "Topic",
    "User",
    "UserPreference",
]
