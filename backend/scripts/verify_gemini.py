"""Verify a real Gemini request against the live Google API.

Run from the backend folder with a real key:

    GEMINI_API_KEY=... python -m scripts.verify_gemini "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?"

The script exits non-zero when the call fails, so it can gate a deployment check. It prints
the model that answered and the first characters of the reply, never the key.
"""

from __future__ import annotations

import asyncio
import sys

from app.core.config import get_settings
from app.services import ai_tutor_service


async def main() -> int:
    settings = get_settings()
    if not ai_tutor_service.is_configured():
        print("FAIL: GEMINI_API_KEY is not set, so no real request could be made.")
        return 2

    message = sys.argv[1] if len(sys.argv) > 1 else "What is force? Give one everyday example."
    language = "kn" if any("\u0c80" <= ch <= "\u0cff" for ch in message) else "en"

    try:
        reply = await ai_tutor_service.generate_tutor_reply(
            message=message,
            language=language,
            level="class8",
            context=ai_tutor_service.TutorContext(
                chapter_title_kn="ಬಲ ಮತ್ತು ಚಲನೆ",
                chapter_title_en="Force and Motion",
                topic_title_kn="ಬಲ",
                topic_title_en="Force",
                lesson_body="ಬಲವು ವಸ್ತುವಿನ ಚಲನೆಯನ್ನು ಬದಲಾಯಿಸಬಹುದು.",
                key_terms=["ಬಲ / force"],
                objectives=["ಬಲದ ಉದಾಹರಣೆಗಳನ್ನು ಹೇಳುವುದು"],
            ),
            history=[],
        )
    except ai_tutor_service.TutorError as exc:
        print(f"FAIL: {exc.code} ({exc.status_code}) - {exc.message}")
        return 1

    print(f"OK provider=google-gemini model={reply.model} language={language}")
    print(f"configured_model={settings.GEMINI_MODEL} latency_ms={reply.latency_ms}")
    print(f"usage={reply.usage}")
    print(f"reply_chars={len(reply.text)}")
    print(f"reply_preview={reply.text[:220]!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
