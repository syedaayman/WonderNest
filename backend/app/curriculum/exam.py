"""Original exam-style practice questions for WonderNest chapters.

These are *practice* questions written by WonderNest, not predictions of any examination and
not copied from a textbook or guide. Question banks are keyed by the seeded chapter number so
a chapter always gets questions about its own topic.

Chapters without an authored bank fall back to their own practice quiz questions (see
``questions_from_quiz``), which keeps every chapter-specific without inventing content.
"""

from __future__ import annotations

from typing import Any, Iterable

EXAM_TYPE_LABELS: dict[str, dict[str, str]] = {
    "very_short": {"en": "Very short answer", "kn": "ಅತಿ ಸಣ್ಣ ಉತ್ತರ"},
    "short": {"en": "Short answer", "kn": "ಸಣ್ಣ ಉತ್ತರ"},
    "long": {"en": "Long answer", "kn": "ದೊಡ್ಡ ಉತ್ತರ"},
    "mcq": {"en": "Multiple choice", "kn": "ಬಹು ಆಯ್ಕೆ"},
    "fill_blank": {"en": "Fill in the blank", "kn": "ಖಾಲಿ ತುಂಬಿರಿ"},
    "true_false": {"en": "True or false", "kn": "ಸರಿ ಅಥವಾ ತಪ್ಪು"},
    "diagram": {"en": "Diagram labelling", "kn": "ಚಿತ್ರ ಲೇಬಲ್ ಮಾಡುವುದು"},
    "concept": {"en": "Concept based", "kn": "ಪರಿಕಲ್ಪನೆ ಆಧಾರಿತ"},
}

DIFFICULTY_LABELS: dict[int, dict[str, str]] = {
    1: {"en": "Easy", "kn": "ಸುಲಭ"},
    2: {"en": "Medium", "kn": "ಮಧ್ಯಮ"},
    3: {"en": "Challenging", "kn": "ಕಠಿಣ"},
}


def _q(
    qtype: str,
    marks: int,
    difficulty: int,
    *,
    en: str,
    kn: str,
    answer_en: str,
    answer_kn: str,
    explain_en: str,
    explain_kn: str,
    options_en: list[str] | None = None,
    options_kn: list[str] | None = None,
    correct_index: int | None = None,
) -> dict[str, Any]:
    return {
        "type": qtype,
        "marks": marks,
        "difficulty": difficulty,
        "question_en": en,
        "question_kn": kn,
        "answer_en": answer_en,
        "answer_kn": answer_kn,
        "explanation_en": explain_en,
        "explanation_kn": explain_kn,
        "options_en": options_en or [],
        "options_kn": options_kn or [],
        "correct_index": correct_index,
    }


# --- 103: Human body and organ systems ------------------------------------------------

_HUMAN_BODY: tuple[dict[str, Any], ...] = (
    _q(
        "very_short",
        1,
        1,
        en="Name the three main parts of the human brain.",
        kn="ಮಾನವ ಮಿದುಳಿನ ಮೂರು ಮುಖ್ಯ ಭಾಗಗಳನ್ನು ಹೆಸರಿಸಿ.",
        answer_en="The cerebrum, the cerebellum and the brainstem.",
        answer_kn="ಸೆರೆಬ್ರಮ್, ಸೆರೆಬೆಲ್ಲಮ್ ಮತ್ತು ಮಿದುಳು ಕಾಂಡ.",
        explain_en=(
            "The cerebrum is the large folded upper part for thinking and senses, the "
            "cerebellum sits below it and keeps balance and movement smooth, and the brainstem "
            "joins the brain to the spinal cord and controls breathing and heartbeat."
        ),
        explain_kn=(
            "ಸೆರೆಬ್ರಮ್ ಎಂಬುದು ಯೋಚನೆ ಮತ್ತು ಇಂದ್ರಿಯಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ದೊಡ್ಡ ಮೇಲ್ಭಾಗ; "
            "ಅದರ ಕೆಳಗೆ ಇರುವ ಸೆರೆಬೆಲ್ಲಮ್ ಸಮತೋಲನ ಮತ್ತು ಚಲನೆಯನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ; "
            "ಮಿದುಳು ಕಾಂಡ ಮಿದುಳನ್ನು ಬೆನ್ನುಹುರಿಗೆ ಜೋಡಿಸಿ ಉಸಿರಾಟ ಮತ್ತು ಹೃದಯಬಡಿತವನ್ನು "
            "ನಿಯಂತ್ರಿಸುತ್ತದೆ."
        ),
    ),
    _q(
        "very_short",
        1,
        1,
        en="How many chambers does the human heart have?",
        kn="ಮಾನವ ಹೃದಯಕ್ಕೆ ಎಷ್ಟು ಕೋಣೆಗಳಿವೆ?",
        answer_en="Four: two atria on top and two ventricles below.",
        answer_kn="ನಾಲ್ಕು: ಮೇಲೆ ಎರಡು ಹೃತ್ಕರ್ಣಗಳು ಮತ್ತು ಕೆಳಗೆ ಎರಡು ಹೃತ್ಕುಕ್ಷಿಗಳು.",
        explain_en=(
            "The right atrium and right ventricle handle oxygen-poor blood going to the lungs; "
            "the left atrium and left ventricle handle oxygen-rich blood going to the body."
        ),
        explain_kn=(
            "ಬಲ ಹೃತ್ಕರ್ಣ ಮತ್ತು ಬಲ ಹೃತ್ಕುಕ್ಷಿ ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತವನ್ನು ಶ್ವಾಸಕೋಶಕ್ಕೆ "
            "ಕಳುಹಿಸುತ್ತವೆ; ಎಡ ಹೃತ್ಕರ್ಣ ಮತ್ತು ಎಡ ಹೃತ್ಕುಕ್ಷಿ ಆಮ್ಲಜನಕ ಹೆಚ್ಚಿರುವ ರಕ್ತವನ್ನು "
            "ದೇಹಕ್ಕೆ ಪಂಪ್ ಮಾಡುತ್ತವೆ."
        ),
    ),
    _q(
        "short",
        2,
        2,
        en="Trace the path of blood from the body back to the body in four steps.",
        kn="ದೇಹದಿಂದ ಬಂದ ರಕ್ತ ಮತ್ತೆ ದೇಹಕ್ಕೆ ತಲುಪುವ ಹಾದಿಯನ್ನು ನಾಲ್ಕು ಹಂತಗಳಲ್ಲಿ ಬರೆಯಿರಿ.",
        answer_en=(
            "Body → vena cava → right atrium → right ventricle → pulmonary artery → lungs → "
            "pulmonary veins → left atrium → left ventricle → aorta → body."
        ),
        answer_kn=(
            "ದೇಹ → ಮಹಾ ಅಭಿಧಮನಿ → ಬಲ ಹೃತ್ಕರ್ಣ → ಬಲ ಹೃತ್ಕುಕ್ಷಿ → ಶ್ವಾಸಕೋಶೀಯ ಅಪಧಮನಿ → "
            "ಶ್ವಾಸಕೋಶ → ಶ್ವಾಸಕೋಶೀಯ ಅಭಿಧಮನಿ → ಎಡ ಹೃತ್ಕರ್ಣ → ಎಡ ಹೃತ್ಕುಕ್ಷಿ → ಮಹಾಪಧಮನಿ → ದೇಹ."
        ),
        explain_en=(
            "Oxygen-poor blood always enters the right side of the heart and is sent to the "
            "lungs, and oxygen-rich blood always returns to the left side and is pumped out "
            "through the aorta. Valves stop blood from flowing backwards."
        ),
        explain_kn=(
            "ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತ ಯಾವಾಗಲೂ ಹೃದಯದ ಬಲ ಭಾಗಕ್ಕೆ ಬಂದು ಶ್ವಾಸಕೋಶಕ್ಕೆ "
            "ಹೋಗುತ್ತದೆ; ಆಮ್ಲಜನಕ ಹೆಚ್ಚಿರುವ ರಕ್ತ ಎಡ ಭಾಗಕ್ಕೆ ಬಂದು ಮಹಾಪಧಮನಿಯ ಮೂಲಕ "
            "ದೇಹಕ್ಕೆ ಹೋಗುತ್ತದೆ. ಕವಾಟಗಳು ರಕ್ತ ಹಿಂದಕ್ಕೆ ಹರಿಯದಂತೆ ತಡೆಯುತ್ತವೆ."
        ),
    ),
    _q(
        "short",
        2,
        2,
        en="Why are the walls of the left ventricle thicker than those of the right ventricle?",
        kn="ಎಡ ಹೃತ್ಕುಕ್ಷಿಯ ಗೋಡೆ ಬಲ ಹೃತ್ಕುಕ್ಷಿಯ ಗೋಡೆಗಿಂತ ದಪ್ಪವಾಗಿರುವುದೇಕೆ?",
        answer_en=(
            "The left ventricle pumps blood to the whole body, so it needs more force; the right "
            "ventricle only pumps blood a short distance to the lungs."
        ),
        answer_kn=(
            "ಎಡ ಹೃತ್ಕುಕ್ಷಿ ಇಡೀ ದೇಹಕ್ಕೆ ರಕ್ತವನ್ನು ಪಂಪ್ ಮಾಡುತ್ತದೆ, ಹಾಗಾಗಿ ಹೆಚ್ಚು ಬಲ "
            "ಬೇಕು; ಬಲ ಹೃತ್ಕುಕ್ಷಿ ಶ್ವಾಸಕೋಶಕ್ಕೆ ಸ್ವಲ್ಪ ದೂರ ಮಾತ್ರ ಪಂಪ್ ಮಾಡುತ್ತದೆ."
        ),
        explain_en=(
            "Thicker muscle means a stronger squeeze. The body is a long, high-resistance "
            "circuit compared with the short trip to the lungs."
        ),
        explain_kn=(
            "ದಪ್ಪ ಸ್ನಾಯು ಎಂದರೆ ಬಲವಾದ ಸಂಕೋಚನ. ಶ್ವಾಸಕೋಶದ ಚಿಕ್ಕ ಪ್ರಯಾಣಕ್ಕೆ ಹೋಲಿಸಿದರೆ "
            "ದೇಹವು ಉದ್ದವಾದ, ಹೆಚ್ಚು ಪ್ರತಿರೋಧವಿರುವ ಮಾರ್ಗ."
        ),
    ),
    _q(
        "long",
        4,
        3,
        en=(
            "Explain how the heart, blood vessels and lungs work together to supply oxygen to a "
            "leg muscle while you run."
        ),
        kn=(
            "ನೀವು ಓಡುವಾಗ ಹೃದಯ, ರಕ್ತನಾಳಗಳು ಮತ್ತು ಶ್ವಾಸಕೋಶಗಳು ಸೇರಿ ಕಾಲಿನ ಸ್ನಾಯುವಿಗೆ "
            "ಆಮ್ಲಜನಕ ಒದಗಿಸುವ ಬಗೆಯನ್ನು ವಿವರಿಸಿ."
        ),
        answer_en=(
            "Breathing fills the lungs with air, and oxygen crosses into the blood in the "
            "capillaries around the air sacs. The heart pumps this oxygen-rich blood through "
            "arteries to the leg, where capillaries deliver oxygen to muscle cells. Muscle cells "
            "release carbon dioxide, which travels back in veins to the heart and then to the "
            "lungs to be breathed out."
        ),
        answer_kn=(
            "ಉಸಿರಾಡುವಾಗ ಶ್ವಾಸಕೋಶಗಳು ಗಾಳಿಯಿಂದ ತುಂಬುತ್ತವೆ; ವಾಯುಕೋಶಗಳ ಸುತ್ತಲಿನ "
            "ಕೆಶಿಕೆಗಳಲ್ಲಿ ಆಮ್ಲಜನಕ ರಕ್ತಕ್ಕೆ ಸೇರುತ್ತದೆ. ಹೃದಯವು ಆಮ್ಲಜನಕಯುಕ್ತ ರಕ್ತವನ್ನು "
            "ಅಪಧಮನಿಗಳ ಮೂಲಕ ಕಾಲಿಗೆ ಪಂಪ್ ಮಾಡುತ್ತದೆ; ಅಲ್ಲಿ ಕೆಶಿಕೆಗಳು ಆಮ್ಲಜನಕವನ್ನು "
            "ಸ್ನಾಯು ಕಣಗಳಿಗೆ ಒದಗಿಸುತ್ತವೆ. ಸ್ನಾಯು ಕಣಗಳು ಬಿಡುಗಡೆ ಮಾಡುವ ಇಂಗಾಲದ "
            "ಡೈಆಕ್ಸೈಡ್ ಅಭಿಧಮನಿಗಳ ಮೂಲಕ ಹೃದಯಕ್ಕೆ, ನಂತರ ಶ್ವಾಸಕೋಶಕ್ಕೆ ಹೋಗಿ ಹೊರಬರುತ್ತದೆ."
        ),
        explain_en=(
            "The three systems form one loop: lungs load oxygen, the heart drives the flow, and "
            "blood vessels deliver and collect. During exercise the heart rate rises to move more "
            "blood per minute."
        ),
        explain_kn=(
            "ಮೂರು ವ್ಯವಸ್ಥೆಗಳು ಒಂದೇ ಚಕ್ರವನ್ನು ರೂಪಿಸುತ್ತವೆ: ಶ್ವಾಸಕೋಶ ಆಮ್ಲಜನಕ ತುಂಬುತ್ತದೆ, "
            "ಹೃದಯ ಹರಿವನ್ನು ನಡೆಸುತ್ತದೆ, ರಕ್ತನಾಳಗಳು ತಲುಪಿಸಿ ಸಂಗ್ರಹಿಸುತ್ತವೆ. "
            "ವ್ಯಾಯಾಮದಲ್ಲಿ ಹೃದಯಬಡಿತ ಹೆಚ್ಚಾಗಿ ನಿಮಿಷಕ್ಕೆ ಹೆಚ್ಚು ರಕ್ತ ಸಾಗುತ್ತದೆ."
        ),
    ),
    _q(
        "long",
        4,
        3,
        en="Describe the job of the nervous system and explain the difference between the brain and the spinal cord.",
        kn="ನರಮಂಡಲದ ಕೆಲಸವನ್ನು ವಿವರಿಸಿ ಮತ್ತು ಮಿದುಳು ಹಾಗೂ ಬೆನ್ನುಹುರಿಯ ವ್ಯತ್ಯಾಸವನ್ನು ತಿಳಿಸಿ.",
        answer_en=(
            "The nervous system collects information through sense organs, carries it as "
            "electrical signals along nerves, and produces a response in muscles or glands. The "
            "brain is the control centre that interprets signals and decides; the spinal cord is "
            "the main cable to the body and can also produce fast reflex actions without waiting "
            "for the brain."
        ),
        answer_kn=(
            "ನರಮಂಡಲವು ಇಂದ್ರಿಯಾಂಗಗಳ ಮೂಲಕ ಮಾಹಿತಿ ಸಂಗ್ರಹಿಸಿ, ನರಗಳ ಮೂಲಕ "
            "ವಿದ್ಯುತ್ ಸಂಕೇತಗಳಾಗಿ ಸಾಗಿಸಿ, ಸ್ನಾಯು ಅಥವಾ ಗ್ರಂಥಿಗಳಲ್ಲಿ ಪ್ರತಿಕ್ರಿಯೆ "
            "ಉಂಟುಮಾಡುತ್ತದೆ. ಮಿದುಳು ಸಂಕೇತಗಳನ್ನು ಅರ್ಥೈಸಿ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳುವ "
            "ನಿಯಂತ್ರಣ ಕೇಂದ್ರ; ಬೆನ್ನುಹುರಿ ದೇಹಕ್ಕೆ ಹೋಗುವ ಮುಖ್ಯ ನರಮಾರ್ಗ ಮತ್ತು "
            "ಮಿದುಳಿಗೆ ಕಾಯದೆ ವೇಗದ ಪ್ರತಿವರ್ತನಗಳನ್ನೂ ಉಂಟುಮಾಡಬಲ್ಲದು."
        ),
        explain_en=(
            "Reflexes are faster because the spinal cord can short-circuit the loop, which is why "
            "your hand moves away from a hot vessel before you feel the pain."
        ),
        explain_kn=(
            "ಪ್ರತಿವರ್ತನಗಳು ವೇಗವಾಗಿರುತ್ತವೆ ಏಕೆಂದರೆ ಬೆನ್ನುಹುರಿ ಚಕ್ರವನ್ನು "
            "ಸಂಕ್ಷಿಪ್ತಗೊಳಿಸಬಲ್ಲದು; ಬಿಸಿ ಪಾತ್ರೆಗೆ ಕೈ ತಗುಲಿದಾಗ ನೋವು ಅನುಭವಕ್ಕೆ ಮೊದಲೇ "
            "ಕೈ ಹಿಂದೆ ಸರಿಯುವುದು ಇದಕ್ಕೆ ಉದಾಹರಣೆ."
        ),
    ),
    _q(
        "mcq",
        1,
        1,
        en="Which blood vessel carries blood away from the heart?",
        kn="ಹೃದಯದಿಂದ ರಕ್ತವನ್ನು ಹೊರಗೆ ಸಾಗಿಸುವ ರಕ್ತನಾಳ ಯಾವುದು?",
        answer_en="An artery.",
        answer_kn="ಅಪಧಮನಿ.",
        explain_en="Arteries carry blood away from the heart; veins bring it back.",
        explain_kn="ಅಪಧಮನಿಗಳು ಹೃದಯದಿಂದ ರಕ್ತವನ್ನು ಹೊರಗೆ ಸಾಗಿಸುತ್ತವೆ; ಅಭಿಧಮನಿಗಳು ಹಿಂದಕ್ಕೆ ತರುತ್ತವೆ.",
        options_en=["An artery", "A vein", "A capillary", "A valve"],
        options_kn=["ಅಪಧಮನಿ", "ಅಭಿಧಮನಿ", "ಕೆಶಿಕೆ", "ಕವಾಟ"],
        correct_index=0,
    ),
    _q(
        "mcq",
        1,
        2,
        en="Which part of the brain keeps your balance while cycling?",
        kn="ಸೈಕಲ್ ಸವಾರಿ ಮಾಡುವಾಗ ಸಮತೋಲನ ಕಾಪಾಡುವ ಮಿದುಳಿನ ಭಾಗ ಯಾವುದು?",
        answer_en="The cerebellum.",
        answer_kn="ಸೆರೆಬೆಲ್ಲಮ್.",
        explain_en=(
            "The cerebellum coordinates balance, posture and smooth movement, which is exactly "
            "what cycling demands."
        ),
        explain_kn=(
            "ಸೆರೆಬೆಲ್ಲಮ್ ಸಮತೋಲನ, ದೇಹದ ನಿಲುವು ಮತ್ತು ನಯವಾದ ಚಲನೆಯನ್ನು ಸಮನ್ವಯ "
            "ಮಾಡುತ್ತದೆ; ಸೈಕಲ್ ಸವಾರಿಗೆ ಇದೇ ಬೇಕು."
        ),
        options_en=["The cerebellum", "The cerebrum", "The brainstem", "The spinal cord"],
        options_kn=["ಸೆರೆಬೆಲ್ಲಮ್", "ಸೆರೆಬ್ರಮ್", "ಮಿದುಳು ಕಾಂಡ", "ಬೆನ್ನುಹುರಿ"],
        correct_index=0,
    ),
    _q(
        "fill_blank",
        1,
        1,
        en="The largest artery in the human body is the ________.",
        kn="ಮಾನವ ದೇಹದ ಅತಿ ದೊಡ್ಡ ಅಪಧಮನಿ ________.",
        answer_en="aorta",
        answer_kn="ಮಹಾಪಧಮನಿ",
        explain_en=(
            "The aorta leaves the left ventricle and carries oxygen-rich blood to the whole body."
        ),
        explain_kn=(
            "ಮಹಾಪಧಮನಿ ಎಡ ಹೃತ್ಕುಕ್ಷಿಯಿಂದ ಹೊರಟು ಆಮ್ಲಜನಕಯುಕ್ತ ರಕ್ತವನ್ನು ಇಡೀ ದೇಹಕ್ಕೆ "
            "ಒಯ್ಯುತ್ತದೆ."
        ),
    ),
    _q(
        "true_false",
        1,
        1,
        en="Veins usually carry oxygen-poor blood back to the heart.",
        kn="ಅಭಿಧಮನಿಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತವನ್ನು ಹೃದಯಕ್ಕೆ ಹಿಂದಕ್ಕೆ ಒಯ್ಯುತ್ತವೆ.",
        answer_en="True.",
        answer_kn="ಸರಿ.",
        explain_en=(
            "Most veins carry oxygen-poor blood back to the heart, with the pulmonary veins being "
            "the well-known exception."
        ),
        explain_kn=(
            "ಬಹುತೇಕ ಅಭಿಧಮನಿಗಳು ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತವನ್ನು ಹೃದಯಕ್ಕೆ ಒಯ್ಯುತ್ತವೆ; "
            "ಶ್ವಾಸಕೋಶೀಯ ಅಭಿಧಮನಿಗಳು ಇದಕ್ಕೆ ಪ್ರಸಿದ್ಧ ಹೊರತು."
        ),
    ),
    _q(
        "diagram",
        3,
        2,
        en=(
            "On the heart diagram, label the four chambers and mark with an arrow which chamber "
            "sends blood to the lungs."
        ),
        kn=(
            "ಹೃದಯದ ಚಿತ್ರದಲ್ಲಿ ನಾಲ್ಕು ಕೋಣೆಗಳನ್ನು ಲೇಬಲ್ ಮಾಡಿ ಮತ್ತು ಶ್ವಾಸಕೋಶಕ್ಕೆ ರಕ್ತ "
            "ಕಳುಹಿಸುವ ಕೋಣೆಯನ್ನು ಬಾಣದಿಂದ ಗುರುತಿಸಿ."
        ),
        answer_en=(
            "Right atrium and right ventricle on the diagram's left side; left atrium and left "
            "ventricle on its right side; the arrow leaves the right ventricle through the "
            "pulmonary artery."
        ),
        answer_kn=(
            "ಚಿತ್ರದ ಎಡಬದಿಯಲ್ಲಿ ಬಲ ಹೃತ್ಕರ್ಣ ಮತ್ತು ಬಲ ಹೃತ್ಕುಕ್ಷಿ; ಬಲಬದಿಯಲ್ಲಿ ಎಡ ಹೃತ್ಕರ್ಣ "
            "ಮತ್ತು ಎಡ ಹೃತ್ಕುಕ್ಷಿ; ಬಾಣವು ಬಲ ಹೃತ್ಕುಕ್ಷಿಯಿಂದ ಶ್ವಾಸಕೋಶೀಯ ಅಪಧಮನಿಯ "
            "ಮೂಲಕ ಹೊರಡುತ್ತದೆ."
        ),
        explain_en=(
            "Diagram labels are written from the patient's point of view, so the right side of the "
            "heart appears on the left of the drawing."
        ),
        explain_kn=(
            "ಚಿತ್ರದ ಲೇಬಲ್‌ಗಳು ರೋಗಿಯ ದೃಷ್ಟಿಕೋನದಿಂದ ಬರೆಯಲ್ಪಡುತ್ತವೆ; ಹಾಗಾಗಿ ಹೃದಯದ "
            "ಬಲ ಭಾಗ ಚಿತ್ರದ ಎಡಬದಿಯಲ್ಲಿ ಕಾಣುತ್ತದೆ."
        ),
    ),
    _q(
        "concept",
        2,
        3,
        en=(
            "A student says 'the heart rests between beats'. Explain what actually happens in the "
            "heart between two beats."
        ),
        kn=(
            "ಒಬ್ಬ ವಿದ್ಯಾರ್ಥಿ 'ಬಡಿತಗಳ ನಡುವೆ ಹೃದಯ ವಿಶ್ರಾಂತಿ ಪಡೆಯುತ್ತದೆ' ಎನ್ನುತ್ತಾನೆ. "
            "ಎರಡು ಬಡಿತಗಳ ನಡುವೆ ಹೃದಯದಲ್ಲಿ ನಿಜವಾಗಿ ಏನಾಗುತ್ತದೆ ಎಂದು ವಿವರಿಸಿ."
        ),
        answer_en=(
            "Between beats the heart chambers relax and fill with blood. The atria fill first, then "
            "the ventricles fill as the valves open, ready for the next contraction."
        ),
        answer_kn=(
            "ಬಡಿತಗಳ ನಡುವೆ ಹೃದಯದ ಕೋಣೆಗಳು ಸಡಿಲಗೊಂಡು ರಕ್ತದಿಂದ ತುಂಬುತ್ತವೆ. ಮೊದಲು "
            "ಹೃತ್ಕರ್ಣಗಳು ತುಂಬುತ್ತವೆ, ನಂತರ ಕವಾಟಗಳು ತೆರೆದಾಗ ಹೃತ್ಕುಕ್ಷಿಗಳು ತುಂಬಿ "
            "ಮುಂದಿನ ಸಂಕೋಚನಕ್ಕೆ ಸಿದ್ಧವಾಗುತ್ತವೆ."
        ),
        explain_en=(
            "Filling is an active part of the cycle, not a pause. That is why a very fast heart "
            "rate can reduce how much blood each beat can pump."
        ),
        explain_kn=(
            "ತುಂಬುವಿಕೆ ಚಕ್ರದ ಸಕ್ರಿಯ ಭಾಗ, ವಿರಾಮವಲ್ಲ. ಆದ್ದರಿಂದ ಅತಿ ವೇಗದ ಹೃದಯಬಡಿತದಲ್ಲಿ "
            "ಪ್ರತಿ ಬಡಿತಕ್ಕೆ ಪಂಪ್ ಆಗುವ ರಕ್ತದ ಪ್ರಮಾಣ ಕಡಿಮೆಯಾಗಬಹುದು."
        ),
    ),
)

# --- 102: Human brain ----------------------------------------------------------------

_BRAIN: tuple[dict[str, Any], ...] = (
    _q(
        "very_short",
        1,
        1,
        en="Which part of the brain controls thinking and memory?",
        kn="ಯೋಚನೆ ಮತ್ತು ನೆನಪನ್ನು ನಿಯಂತ್ರಿಸುವ ಮಿದುಳಿನ ಭಾಗ ಯಾವುದು?",
        answer_en="The cerebrum.",
        answer_kn="ಸೆರೆಬ್ರಮ್.",
        explain_en="The folded outer cerebrum handles thinking, memory, language and the senses.",
        explain_kn="ಮಡಿಕೆಗಳಿರುವ ಹೊರಗಿನ ಸೆರೆಬ್ರಮ್ ಯೋಚನೆ, ನೆನಪು, ಭಾಷೆ ಮತ್ತು ಇಂದ್ರಿಯಗಳನ್ನು ನೋಡಿಕೊಳ್ಳುತ್ತದೆ.",
    ),
    _q(
        "short",
        2,
        2,
        en="What does the brainstem do, and why is damage to it dangerous?",
        kn="ಮಿದುಳು ಕಾಂಡ ಏನು ಮಾಡುತ್ತದೆ ಮತ್ತು ಅದಕ್ಕೆ ಹಾನಿಯಾದರೆ ಏಕೆ ಅಪಾಯ?",
        answer_en=(
            "The brainstem connects the brain to the spinal cord and controls automatic actions "
            "such as breathing and heartbeat. Damage can stop these actions, which is why it is "
            "dangerous."
        ),
        answer_kn=(
            "ಮಿದುಳು ಕಾಂಡ ಮಿದುಳನ್ನು ಬೆನ್ನುಹುರಿಗೆ ಜೋಡಿಸಿ ಉಸಿರಾಟ ಮತ್ತು ಹೃದಯಬಡಿತದಂತಹ "
            "ಸ್ವಯಂಚಾಲಿತ ಕ್ರಿಯೆಗಳನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಅದಕ್ಕೆ ಹಾನಿಯಾದರೆ ಈ ಕ್ರಿಯೆಗಳು "
            "ನಿಲ್ಲಬಹುದು; ಆದ್ದರಿಂದ ಇದು ಅಪಾಯಕಾರಿ."
        ),
        explain_en="Automatic functions are life-sustaining, so the brainstem is a vital structure.",
        explain_kn="ಸ್ವಯಂಚಾಲಿತ ಕ್ರಿಯೆಗಳು ಜೀವ ಉಳಿಸುವಂಥವು; ಆದ್ದರಿಂದ ಮಿದುಳು ಕಾಂಡ ಅತ್ಯಗತ್ಯ ರಚನೆ.",
    ),
    _q(
        "mcq",
        1,
        2,
        en="Which structure protects the brain by acting as a shock absorber?",
        kn="ಆಘಾತ ತಡೆಯುವ ಮೂಲಕ ಮಿದುಳನ್ನು ರಕ್ಷಿಸುವ ರಚನೆ ಯಾವುದು?",
        answer_en="Cerebrospinal fluid.",
        answer_kn="ಮಿದುಳು ಬೆನ್ನುಹುರಿ ದ್ರವ.",
        explain_en="Cerebrospinal fluid cushions the brain inside the skull.",
        explain_kn="ಮಿದುಳು ಬೆನ್ನುಹುರಿ ದ್ರವವು ತಲೆಬುರುಡೆಯೊಳಗೆ ಮಿದುಳಿಗೆ ಮೆತ್ತೆಯಂತೆ ರಕ್ಷಣೆ ನೀಡುತ್ತದೆ.",
        options_en=["Cerebrospinal fluid", "The skull only", "The cerebellum", "The spinal cord"],
        options_kn=["ಮಿದುಳು ಬೆನ್ನುಹುರಿ ದ್ರವ", "ತಲೆಬುರುಡೆ ಮಾತ್ರ", "ಸೆರೆಬೆಲ್ಲಮ್", "ಬೆನ್ನುಹುರಿ"],
        correct_index=0,
    ),
    _q(
        "concept",
        3,
        3,
        en="Why does a footballer feel dizzy for a moment after a sudden stop?",
        kn="ಇದ್ದಕ್ಕಿದ್ದಂತೆ ನಿಂತ ನಂತರ ಫುಟ್‌ಬಾಲ್ ಆಟಗಾರನಿಗೆ ಕ್ಷಣಕಾಲ ತಲೆಸುತ್ತು ಏಕೆ?",
        answer_en=(
            "The cerebellum uses signals from the inner ear and muscles to keep balance. A sudden "
            "stop gives conflicting signals, so balance is briefly lost."
        ),
        answer_kn=(
            "ಸೆರೆಬೆಲ್ಲಮ್ ಒಳಗಿನ ಕಿವಿ ಮತ್ತು ಸ್ನಾಯುಗಳಿಂದ ಬರುವ ಸಂಕೇತಗಳನ್ನು ಬಳಸಿ "
            "ಸಮತೋಲನ ಕಾಪಾಡುತ್ತದೆ. ಇದ್ದಕ್ಕಿದ್ದಂತೆ ನಿಂತಾಗ ಸಂಕೇತಗಳು ವಿರೋಧಾಭಾಸವಾಗಿ "
            "ಸ್ವಲ್ಪ ಸಮಯ ಸಮತೋಲನ ತಪ್ಪುತ್ತದೆ."
        ),
        explain_en="Balance is a continuous calculation, not a fixed setting.",
        explain_kn="ಸಮತೋಲನವು ನಿರಂತರ ಲೆಕ್ಕಾಚಾರ, ಸ್ಥಿರ ಸೆಟ್ಟಿಂಗ್ ಅಲ್ಲ.",
    ),
)

# --- 101: Photosynthesis -------------------------------------------------------------

_PHOTOSYNTHESIS: tuple[dict[str, Any], ...] = (
    _q(
        "very_short",
        1,
        1,
        en="Write the word equation for photosynthesis.",
        kn="ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯ ಪದ ಸಮೀಕರಣ ಬರೆಯಿರಿ.",
        answer_en="Carbon dioxide + water, in sunlight and with chlorophyll, gives glucose + oxygen.",
        answer_kn="ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ + ನೀರು, ಸೂರ್ಯನ ಬೆಳಕು ಮತ್ತು ಕ್ಲೋರೊಫಿಲ್ ಇರುವಾಗ, ಗ್ಲೂಕೋಸ್ + ಆಮ್ಲಜನಕ.",
        explain_en="Light energy is stored in the chemical bonds of glucose.",
        explain_kn="ಬೆಳಕಿನ ಶಕ್ತಿ ಗ್ಲೂಕೋಸ್‌ನ ರಾಸಾಯನಿಕ ಬಂಧಗಳಲ್ಲಿ ಸಂಗ್ರಹವಾಗುತ್ತದೆ.",
    ),
    _q(
        "short",
        2,
        2,
        en="Why does a leaf that has been kept in the dark show no starch?",
        kn="ಕತ್ತಲೆಯಲ್ಲಿ ಇಟ್ಟ ಎಲೆಯಲ್ಲಿ ಪಿಷ್ಟ ಏಕೆ ಕಾಣುವುದಿಲ್ಲ?",
        answer_en=(
            "Without light, the light-dependent step cannot run, so no glucose is made and no "
            "starch is stored."
        ),
        answer_kn=(
            "ಬೆಳಕಿಲ್ಲದೆ ಬೆಳಕು ಅವಲಂಬಿತ ಹಂತ ನಡೆಯದು; ಹಾಗಾಗಿ ಗ್ಲೂಕೋಸ್ ಉತ್ಪತ್ತಿಯಾಗದೆ "
            "ಪಿಷ್ಟ ಸಂಗ್ರಹವಾಗುವುದಿಲ್ಲ."
        ),
        explain_en="Starch is the storage form of the glucose made in photosynthesis.",
        explain_kn="ಪಿಷ್ಟವು ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಲ್ಲಿ ತಯಾರಾದ ಗ್ಲೂಕೋಸ್‌ನ ಸಂಗ್ರಹ ರೂಪ.",
    ),
    _q(
        "fill_blank",
        1,
        1,
        en="Tiny pores on a leaf that allow gas exchange are called ________.",
        kn="ಎಲೆಯ ಮೇಲೆ ಅನಿಲ ವಿನಿಮಯಕ್ಕೆ ಸಹಾಯ ಮಾಡುವ ಸಣ್ಣ ರಂಧ್ರಗಳನ್ನು ________ ಎನ್ನುತ್ತಾರೆ.",
        answer_en="stomata",
        answer_kn="ಸ್ಟೊಮ್ಯಾಟ",
        explain_en="Guard cells open and close each stoma to control water loss and gas exchange.",
        explain_kn="ರಕ್ಷಕ ಕಣಗಳು ಪ್ರತಿ ಸ್ಟೊಮ್ಯಾಟವನ್ನು ತೆರೆದು ಮುಚ್ಚಿ ನೀರಿನ ನಷ್ಟ ಮತ್ತು ಅನಿಲ ವಿನಿಮಯವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತವೆ.",
    ),
    _q(
        "concept",
        2,
        2,
        en="Why are most leaves broad and flat?",
        kn="ಹೆಚ್ಚಿನ ಎಲೆಗಳು ಅಗಲ ಮತ್ತು ಚಪ್ಪಟೆಯಾಗಿರುವುದೇಕೆ?",
        answer_en="A broad flat shape exposes a large surface to sunlight and lets in more carbon dioxide.",
        answer_kn="ಅಗಲ ಚಪ್ಪಟೆ ಆಕಾರವು ಸೂರ್ಯನ ಬೆಳಕಿಗೆ ಹೆಚ್ಚು ಮೇಲ್ಮೈ ಒಡ್ಡಿ ಹೆಚ್ಚು ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಒಳಗೆ ಬರಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.",
        explain_en="More light and gas captured means more food made.",
        explain_kn="ಹೆಚ್ಚು ಬೆಳಕು ಮತ್ತು ಅನಿಲ ಸೆರೆಹಿಡಿದರೆ ಹೆಚ್ಚು ಆಹಾರ ತಯಾರಾಗುತ್ತದೆ.",
    ),
)

# --- 1 and 2: biology units ----------------------------------------------------------

_LIVING_WORLD: tuple[dict[str, Any], ...] = (
    _q(
        "very_short",
        1,
        1,
        en="Name one useful and one harmful microorganism.",
        kn="ಒಂದು ಉಪಯುಕ್ತ ಮತ್ತು ಒಂದು ಹಾನಿಕಾರಕ ಸೂಕ್ಷ್ಮಜೀವಿಯನ್ನು ಹೆಸರಿಸಿ.",
        answer_en="Useful: curd-forming Lactobacillus. Harmful: the malaria parasite Plasmodium.",
        answer_kn="ಉಪಯುಕ್ತ: ಮೊಸರು ತಯಾರಿಸುವ ಲ್ಯಾಕ್ಟೋಬೆಸಿಲಸ್. ಹಾನಿಕಾರಕ: ಮಲೇರಿಯಾ ಉಂಟುಮಾಡುವ ಪ್ಲಾಸ್ಮೋಡಿಯಂ.",
        explain_en="Microorganisms are not all bad; their effect depends on the species and where it grows.",
        explain_kn="ಸೂಕ್ಷ್ಮಜೀವಿಗಳೆಲ್ಲವೂ ಕೆಟ್ಟವಲ್ಲ; ಪರಿಣಾಮ ಅವುಗಳ ಪ್ರಭೇದ ಮತ್ತು ಬೆಳೆಯುವ ಸ್ಥಳವನ್ನು ಅವಲಂಬಿಸಿದೆ.",
    ),
    _q(
        "short",
        2,
        2,
        en="Why does milk turn into curd faster in summer?",
        kn="ಬೇಸಿಗೆಯಲ್ಲಿ ಹಾಲು ಬೇಗ ಮೊಸರಾಗುವುದೇಕೆ?",
        answer_en="The bacteria that turn milk into curd grow faster at warm temperatures.",
        answer_kn="ಹಾಲನ್ನು ಮೊಸರಾಗಿ ಪರಿವರ್ತಿಸುವ ಬ್ಯಾಕ್ಟೀರಿಯಾ ಬೆಚ್ಚನೆಯ ಉಷ್ಣಾಂಶದಲ್ಲಿ ವೇಗವಾಗಿ ಬೆಳೆಯುತ್ತವೆ.",
        explain_en="Warmth speeds up microbial growth, which is also why food spoils faster in heat.",
        explain_kn="ಬಿಸಿ ಸೂಕ್ಷ್ಮಜೀವಿ ಬೆಳವಣಿಗೆಯನ್ನು ವೇಗಗೊಳಿಸುತ್ತದೆ; ಆದ್ದರಿಂದಲೇ ಬಿಸಿಯಲ್ಲಿ ಆಹಾರ ಬೇಗ ಕೆಡುತ್ತದೆ.",
    ),
    _q(
        "mcq",
        1,
        2,
        en="Which group of microorganisms is used to make antibiotics?",
        kn="ಆಂಟಿಬಯಾಟಿಕ್ ತಯಾರಿಸಲು ಯಾವ ಸೂಕ್ಷ್ಮಜೀವಿ ಗುಂಪು ಬಳಕೆಯಾಗುತ್ತದೆ?",
        answer_en="Fungi and bacteria.",
        answer_kn="ಶಿಲೀಂಧ್ರಗಳು ಮತ್ತು ಬ್ಯಾಕ್ಟೀರಿಯಾ.",
        explain_en="Penicillin, for example, comes from a fungus.",
        explain_kn="ಉದಾಹರಣೆಗೆ ಪೆನಿಸಿಲಿನ್ ಒಂದು ಶಿಲೀಂಧ್ರದಿಂದ ಬರುತ್ತದೆ.",
        options_en=["Fungi and bacteria", "Protozoa only", "Algae only", "Viruses only"],
        options_kn=["ಶಿಲೀಂಧ್ರಗಳು ಮತ್ತು ಬ್ಯಾಕ್ಟೀರಿಯಾ", "ಪ್ರೊಟೊಜೋವಾ ಮಾತ್ರ", "ಆಲ್ಗೆ ಮಾತ್ರ", "ವೈರಸ್ ಮಾತ್ರ"],
        correct_index=0,
    ),
)

_HEALTH: tuple[dict[str, Any], ...] = (
    _q(
        "very_short",
        1,
        1,
        en="What does a balanced diet mean?",
        kn="ಸಮತೋಲಿತ ಆಹಾರ ಎಂದರೇನು?",
        answer_en="A diet that supplies all nutrients in the right amounts for the body's needs.",
        answer_kn="ದೇಹದ ಅಗತ್ಯಕ್ಕೆ ತಕ್ಕ ಪ್ರಮಾಣದಲ್ಲಿ ಎಲ್ಲ ಪೋಷಕಾಂಶಗಳನ್ನು ಒದಗಿಸುವ ಆಹಾರ.",
        explain_en="Balanced means the right combination, not simply eating a lot.",
        explain_kn="ಸಮತೋಲನ ಎಂದರೆ ಸರಿಯಾದ ಸಂಯೋಜನೆ, ಹೆಚ್ಚು ತಿನ್ನುವುದಲ್ಲ.",
    ),
    _q(
        "short",
        2,
        2,
        en="Why is vaccination done before a disease is caught rather than after?",
        kn="ರೋಗ ಬರುವ ಮೊದಲೇ ಲಸಿಕೆ ಏಕೆ ನೀಡಲಾಗುತ್ತದೆ?",
        answer_en=(
            "A vaccine trains the immune system to recognise the germ in advance, so the body can "
            "fight it quickly if it enters later."
        ),
        answer_kn=(
            "ಲಸಿಕೆಯು ರೋಗಾಣುವನ್ನು ಮೊದಲೇ ಗುರುತಿಸಲು ರೋಗನಿರೋಧಕ ವ್ಯವಸ್ಥೆಗೆ ತರಬೇತಿ "
            "ನೀಡುತ್ತದೆ; ಹಾಗಾಗಿ ಆಣು ನಂತರ ದೇಹ ಸೇರಿದರೆ ಬೇಗ ಹೋರಾಡಬಲ್ಲದು."
        ),
        explain_en="Immunity is memory: the body remembers the germ's surface and responds faster.",
        explain_kn="ರೋಗನಿರೋಧಕ ಶಕ್ತಿ ಎಂದರೆ ನೆನಪು: ದೇಹ ಆಣುವಿನ ಮೇಲ್ಮೈಯನ್ನು ನೆನಪಿಟ್ಟುಕೊಂಡು ವೇಗವಾಗಿ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ.",
    ),
)


_BANKS: dict[int, tuple[dict[str, Any], ...]] = {
    1: _LIVING_WORLD,
    2: _HEALTH,
    101: _PHOTOSYNTHESIS,
    102: _BRAIN,
    103: _HUMAN_BODY,
}


def bank_for(chapter_number: int) -> tuple[dict[str, Any], ...]:
    """Authored exam questions for a chapter, or an empty tuple when none are written."""
    return _BANKS.get(chapter_number, ())


def questions_from_quiz(rows: Iterable[Any]) -> list[dict[str, Any]]:
    """Turn a chapter's own practice quiz into multiple-choice exam practice.

    This keeps chapters without an authored bank chapter-specific instead of borrowing another
    chapter's questions.
    """
    items: list[dict[str, Any]] = []
    for row in rows:
        options_en = list(getattr(row, "options_en", None) or [])
        options_kn = list(getattr(row, "options_kn", None) or [])
        correct = getattr(row, "correct_index", None)
        if correct is None or not options_en:
            continue
        answer_en = options_en[correct] if 0 <= correct < len(options_en) else ""
        answer_kn = options_kn[correct] if 0 <= correct < len(options_kn) else answer_en
        items.append(
            _q(
                "mcq",
                getattr(row, "marks", 1) or 1,
                getattr(row, "difficulty", 1) or 1,
                en=getattr(row, "question_en", "") or "",
                kn=getattr(row, "question_kn", "") or "",
                answer_en=answer_en,
                answer_kn=answer_kn,
                explain_en=getattr(row, "explanation_en", "") or "",
                explain_kn=getattr(row, "explanation_kn", "") or "",
                options_en=options_en,
                options_kn=options_kn,
                correct_index=correct,
            )
        )
    return items


def summarise(items: Iterable[dict[str, Any]]) -> dict[str, int]:
    """Count questions per type, used by the UI filter chips."""
    counts: dict[str, int] = {}
    for item in items:
        counts[item["type"]] = counts.get(item["type"], 0) + 1
    return counts


__all__ = [
    "DIFFICULTY_LABELS",
    "EXAM_TYPE_LABELS",
    "bank_for",
    "questions_from_quiz",
    "summarise",
]
