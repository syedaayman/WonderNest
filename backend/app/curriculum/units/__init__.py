"""Original WonderNest learning units for Karnataka State Board, Class 8 Science.

Every explanation, note, example and quiz question in this package is written by
WonderNest. Nothing is copied from the textbook. The unit *titles* follow the unit list a
teacher supplied for the 2026-27 Class 8 Science course; they are not quoted official
chapter headings, and the ``SOURCE_NOTE`` below is attached to every seeded chapter so the
UI can say so too.

Shape of a unit dict::

    {
      "number": int,                  # chapter number inside the Science subject
      "category": "biology" | "physics" | "chemistry" | "enrichment",
      "is_enrichment": bool,
      "title_en": str, "title_kn": str,
      "summary_en": str, "summary_kn": str,
      "estimated_minutes": int,
      "visualizations": [str],        # keys understood by the frontend Visualize tab
      "topics": [
         {"title_en", "title_kn", "objectives_en": [str], "objectives_kn": [str],
          "body_en": [str], "body_kn": [str],
          "key_terms": [{"kn","en","meaning_kn","meaning_en"}],
          "example_en", "example_kn"},
      ],
      "notes_en": [str], "notes_kn": [str],
      "videos": [{"title", "language", "topic", "search_query"}],
      "quiz": [{"question_en","question_kn","options_en":[4],"options_kn":[4],
                "correct_index", "explanation_en", "explanation_kn", "difficulty"}],
    }
"""

from app.curriculum.units.biology import UNITS as _BIOLOGY
from app.curriculum.units.chemistry import UNITS as _CHEMISTRY
from app.curriculum.units.enrichment import UNITS as _ENRICHMENT
from app.curriculum.units.human_body import UNITS as _HUMAN_BODY
from app.curriculum.units.physics import UNITS as _PHYSICS

SOURCE_NOTE = (
    "Not official Karnataka State Board text. WonderNest original study content: unit titles "
    "follow the 2026-27 Karnataka Class 8 Science (Curiosity) unit list supplied by the school; "
    "explanations, notes, quizzes and diagrams are written by WonderNest."
)

CATEGORIES: tuple[dict[str, str], ...] = (
    {
        "code": "biology",
        "title_en": "Biology",
        "title_kn": "ಜೀವಶಾಸ್ತ್ರ",
        "blurb_en": "Living things, our body and health.",
        "blurb_kn": "ಜೀವಿಗಳು, ನಮ್ಮ ದೇಹ ಮತ್ತು ಆರೋಗ್ಯ.",
    },
    {
        "code": "physics",
        "title_en": "Physics",
        "title_kn": "ಭೌತಶಾಸ್ತ್ರ",
        "blurb_en": "Electricity, forces, light and how things move.",
        "blurb_kn": "ವಿದ್ಯುತ್, ಬಲಗಳು, ಬೆಳಕು ಮತ್ತು ಚಲನೆ.",
    },
    {
        "code": "chemistry",
        "title_en": "Chemistry",
        "title_kn": "ರಸಾಯನಶಾಸ್ತ್ರ",
        "blurb_en": "What matter is made of and how it behaves.",
        "blurb_kn": "ದ್ರವ್ಯ ಯಾವುದರಿಂದ ಮಾಡಲ್ಪಟ್ಟಿದೆ ಮತ್ತು ಅದು ಹೇಗೆ ವರ್ತಿಸುತ್ತದೆ.",
    },
    {
        "code": "enrichment",
        "title_en": "Visual Enrichment",
        "title_kn": "ದೃಶ್ಯ ಪೂರಕ ಪಾಠ",
        "blurb_en": "Extra illustrated topics that support the units above.",
        "blurb_kn": "ಮೇಲಿನ ಘಟಕಗಳಿಗೆ ಪೂರಕವಾದ ಹೆಚ್ಚುವರಿ ಚಿತ್ರಿತ ವಿಷಯಗಳು.",
    },
)

UNITS: tuple[dict, ...] = (*_BIOLOGY, *_PHYSICS, *_CHEMISTRY, *_ENRICHMENT, *_HUMAN_BODY)

BY_NUMBER: dict[int, dict] = {unit["number"]: unit for unit in UNITS}


def unit_by_number(number: int) -> dict | None:
    """Return the unit with this chapter number, or ``None`` when it is not seeded."""
    return BY_NUMBER.get(number)


def total_questions() -> int:
    return sum(len(unit["quiz"]) for unit in UNITS)


__all__ = ["BY_NUMBER", "CATEGORIES", "SOURCE_NOTE", "UNITS", "total_questions", "unit_by_number"]
