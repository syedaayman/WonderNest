"""AI tutor tests.

These tests never call Google: they exercise the endpoint contract, authentication, the
configuration error path, provider error translation, rate limiting and prompt building by
replacing the single ``_call_model`` seam inside the service. A real Gemini request is
verified separately (see ``scripts/verify_gemini.py``) because it needs a live API key.
"""

import asyncio
from types import SimpleNamespace

import httpx
import pytest
from google.genai import errors as genai_errors
from sqlalchemy import select

from app.core.config import get_settings
from app.core.database import SessionLocal
from app.models import AIConversation, AIMessage, Chapter, Lesson, Topic
from app.services import ai_tutor_service
from app.services.ai_tutor_service import TutorReply

BASE = "/api/ai/tutor"
FAKE_KEY = "test-key-never-logged-0123456789"


class FakeResponse:
    """Minimal stand-in for ``GenerateContentResponse`` (text + candidates + usage)."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.candidates = [
            SimpleNamespace(
                content=SimpleNamespace(parts=[SimpleNamespace(text=text)]),
                finish_reason="STOP",
            )
        ]
        self.usage_metadata = SimpleNamespace(
            prompt_token_count=11,
            candidates_token_count=22,
            total_token_count=33,
        )


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(autouse=True)
def clean_ai_state():
    ai_tutor_service.rate_limiter.reset()
    ai_tutor_service.reset_caches()
    yield
    ai_tutor_service.rate_limiter.reset()
    ai_tutor_service.reset_caches()


@pytest.fixture
def gemini_key(monkeypatch):
    settings = get_settings()
    monkeypatch.setattr(settings, "GEMINI_API_KEY", FAKE_KEY)
    return settings


def _configured(monkeypatch):
    monkeypatch.setattr(get_settings(), "GEMINI_API_KEY", FAKE_KEY)


def _lesson_context() -> dict[str, int]:
    db = SessionLocal()
    try:
        row = db.execute(
            select(Lesson.id, Lesson.topic_id)
            .where(Lesson.body_kn.is_not(None))
            .order_by(Lesson.id)
            .limit(1)
        ).first()
        assert row is not None, "seed data must contain a lesson with a Kannada body"
        chapter_id = db.scalar(
            select(Chapter.id)
            .join(Topic, Topic.chapter_id == Chapter.id)
            .where(Topic.id == row.topic_id)
        )
        return {"lesson_id": row.id, "topic_id": row.topic_id, "chapter_id": chapter_id}
    finally:
        db.close()


def _lesson_body(lesson_id: int) -> str:
    db = SessionLocal()
    try:
        body = db.scalar(select(Lesson.body_kn).where(Lesson.id == lesson_id))
    finally:
        db.close()
    assert body
    return body


def _contents_text(contents) -> str:
    chunks: list[str] = []
    for content in contents:
        for part in content.parts or []:
            if part.text:
                chunks.append(part.text)
    return "\n".join(chunks)


def _system_text(config) -> str:
    instruction = config.system_instruction
    if instruction is None:
        return ""
    if isinstance(instruction, str):
        return instruction
    if isinstance(instruction, list):
        return _contents_text(instruction)
    return _contents_text([instruction])


# ---------------------------------------------------------------------------------------
# Authentication and configuration
# ---------------------------------------------------------------------------------------


def test_chat_requires_authentication(client):
    resp = client.post(f"{BASE}/chat", json={"message": "ನಮಸ್ಕಾರ"})
    assert resp.status_code == 401


def test_status_requires_authentication(client):
    assert client.get(f"{BASE}/status").status_code == 401


def test_suggestions_require_authentication(client):
    assert client.get(f"{BASE}/suggestions").status_code == 401


def test_suggested_prompts_cover_the_brief(client, demo_token):
    resp = client.get(f"{BASE}/suggestions", headers=_auth(demo_token))
    assert resp.status_code == 200, resp.text
    prompts = resp.json()["prompts"]
    joined = " ".join(p["prompt"] for p in prompts).lower()
    assert len(prompts) >= 6
    for expected in (
        "photosynthesis",
        "water cycle",
        "what is force",
        "friction",
        "practice questions",
        "13 years old",
    ):
        assert expected in joined, expected
    # Every chip declares the language the tutor should answer in.
    assert {p["language"] for p in prompts} <= {"kn", "en"}


def test_status_reports_missing_key_without_leaking_secrets(client, demo_token, monkeypatch):
    monkeypatch.setattr(get_settings(), "GEMINI_API_KEY", "")
    resp = client.get(f"{BASE}/status", headers=_auth(demo_token))
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["configured"] is False
    assert "GEMINI_API_KEY" in body["message"]
    assert body["provider"] == "google-gemini"
    assert body["rate_limit_requests"] >= 1
    assert "api_key" not in resp.text.lower().replace("gemini_api_key", "")


def test_status_reports_configured_model(client, demo_token, gemini_key):
    resp = client.get(f"{BASE}/status", headers=_auth(demo_token))
    body = resp.json()
    assert body["configured"] is True
    assert body["model"] == gemini_key.GEMINI_MODEL


def test_missing_key_returns_clear_configuration_error(client, demo_token, monkeypatch):
    monkeypatch.setattr(get_settings(), "GEMINI_API_KEY", "")
    resp = client.post(f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಸಸ್ಯ"})
    assert resp.status_code == 503, resp.text
    detail = resp.json()["detail"]
    assert detail["code"] == "ai_not_configured"
    assert "GEMINI_API_KEY" in detail["message"]


def test_invalid_api_key_is_reported(client, demo_token, gemini_key, monkeypatch):
    def boom(*args, **kwargs):
        raise genai_errors.ClientError(
            400,
            {"error": {"message": "API key not valid. Please pass a valid API key.",
                       "status": "INVALID_ARGUMENT"}},
        )

    monkeypatch.setattr(ai_tutor_service, "_call_model", boom)
    resp = client.post(f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಸಸ್ಯ"})
    assert resp.status_code == 503, resp.text
    detail = resp.json()["detail"]
    assert detail["code"] == "ai_invalid_key"
    assert FAKE_KEY not in resp.text


def test_quota_errors_are_reported_with_retry_hint(client, demo_token, gemini_key, monkeypatch):
    def boom(*args, **kwargs):
        raise genai_errors.ClientError(
            429,
            {"error": {"message": "Resource has been exhausted (e.g. check quota).",
                       "status": "RESOURCE_EXHAUSTED"}},
        )

    monkeypatch.setattr(ai_tutor_service, "_call_model", boom)
    resp = client.post(f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಸಸ್ಯ"})
    assert resp.status_code == 429, resp.text
    assert resp.json()["detail"]["code"] in {"ai_quota_exceeded", "ai_rate_limited"}
    assert resp.headers.get("Retry-After")


def test_timeouts_are_reported(client, demo_token, gemini_key, monkeypatch):
    def boom(*args, **kwargs):
        raise asyncio.TimeoutError()

    monkeypatch.setattr(ai_tutor_service, "_call_model", boom)
    resp = client.post(f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಸಸ್ಯ"})
    assert resp.status_code == 504, resp.text
    assert resp.json()["detail"]["code"] == "ai_timeout"


def test_network_errors_are_reported(client, demo_token, gemini_key, monkeypatch):
    def boom(*args, **kwargs):
        raise httpx.ConnectError("connection refused")

    monkeypatch.setattr(ai_tutor_service, "_call_model", boom)
    resp = client.post(f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಸಸ್ಯ"})
    assert resp.status_code in (502, 503), resp.text
    assert resp.json()["detail"]["code"].startswith("ai_")


def test_over_long_message_is_rejected(client, demo_token, gemini_key):
    resp = client.post(
        f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಅ" * 4000}
    )
    assert resp.status_code in (413, 422), resp.text


def test_empty_message_is_rejected(client, demo_token, gemini_key):
    resp = client.post(f"{BASE}/chat", headers=_auth(demo_token), json={"message": "   "})
    assert resp.status_code in (413, 422), resp.text


# ---------------------------------------------------------------------------------------
# Rate limiting
# ---------------------------------------------------------------------------------------


def test_rate_limit_blocks_a_burst(client, demo_token, gemini_key, monkeypatch):
    settings = get_settings()
    monkeypatch.setattr(settings, "AI_RATE_LIMIT_REQUESTS", 2)

    async def fake_reply(**kwargs):
        return TutorReply(text="ಉತ್ತರ", model="gemini-3.8-flash", latency_ms=5, usage=None)

    monkeypatch.setattr(ai_tutor_service, "generate_tutor_reply", fake_reply)

    payload = {"message": "ಬಲ ಎಂದರೇನು?", "language": "kn"}
    first = client.post(f"{BASE}/chat", headers=_auth(demo_token), json=payload)
    second = client.post(f"{BASE}/chat", headers=_auth(demo_token), json=payload)
    third = client.post(f"{BASE}/chat", headers=_auth(demo_token), json=payload)

    assert first.status_code == 200, first.text
    assert second.status_code == 200, second.text
    assert third.status_code == 429, third.text
    assert third.json()["detail"]["code"] == "ai_rate_limited"
    assert int(third.headers["Retry-After"]) >= 1


# ---------------------------------------------------------------------------------------
# Prompt construction, language and lesson context
# ---------------------------------------------------------------------------------------


def _capture_calls(monkeypatch, reply_text: str = "ಉತ್ತರ"):
    captured: list[dict] = []

    async def fake_call(client, model, contents, config, timeout_seconds):
        captured.append({"model": model, "contents": contents, "config": config})
        return FakeResponse(reply_text)

    monkeypatch.setattr(ai_tutor_service, "_call_model", fake_call)
    return captured


def test_kannada_request_gets_kannada_instruction(client, demo_token, gemini_key, monkeypatch):
    captured = _capture_calls(monkeypatch)
    resp = client.post(
        f"{BASE}/chat",
        headers=_auth(demo_token),
        json={"message": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?", "language": "kn"},
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["provider"] == "google-gemini"
    assert body["language"] == "kn"
    assert body["reply"] == "ಉತ್ತರ"
    assert body["model"] == gemini_key.GEMINI_MODEL
    assert body["usage"]["total_tokens"] == 33

    system = _system_text(captured[0]["config"])
    assert "Kannada" in system
    assert "Class 8" in system or "class 8" in system
    # The tutor must not claim to be official textbook material.
    assert "official" in system.lower()


def test_english_request_gets_english_instruction(client, demo_token, gemini_key, monkeypatch):
    captured = _capture_calls(monkeypatch)
    resp = client.post(
        f"{BASE}/chat",
        headers=_auth(demo_token),
        json={"message": "What is force?", "language": "en", "level": "beginner"},
    )
    assert resp.status_code == 200, resp.text
    system = _system_text(captured[0]["config"])
    assert "English" in system


def test_lesson_context_reaches_the_prompt(client, demo_token, gemini_key, monkeypatch):
    context = _lesson_context()
    body_snippet = _lesson_body(context["lesson_id"])[:60]
    captured = _capture_calls(monkeypatch)

    resp = client.post(
        f"{BASE}/chat",
        headers=_auth(demo_token),
        json={
            "message": "ಈ ಪಾಠವನ್ನು ವಿವರಿಸಿ",
            "language": "kn",
            "lesson_id": context["lesson_id"],
        },
    )
    assert resp.status_code == 200, resp.text
    prompt = _contents_text(captured[0]["contents"])
    assert body_snippet in prompt
    assert "ಈ ಪಾಠವನ್ನು ವಿವರಿಸಿ" in prompt


def test_unknown_lesson_is_rejected(client, demo_token, gemini_key):
    resp = client.post(
        f"{BASE}/chat", headers=_auth(demo_token), json={"message": "hi", "lesson_id": 999999}
    )
    assert resp.status_code == 404, resp.text


def test_conversation_history_is_stored_and_replayed(
    client, demo_token, gemini_key, monkeypatch
):
    captured = _capture_calls(monkeypatch, reply_text="ಮೊದಲ ಉತ್ತರ")

    first = client.post(
        f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಮೊದಲ ಪ್ರಶ್ನೆ"}
    )
    assert first.status_code == 200, first.text
    conversation_id = first.json()["conversation_id"]

    second = client.post(
        f"{BASE}/chat",
        headers=_auth(demo_token),
        json={"message": "ಎರಡನೇ ಪ್ರಶ್ನೆ", "conversation_id": conversation_id},
    )
    assert second.status_code == 200, second.text
    assert second.json()["conversation_id"] == conversation_id

    replayed = _contents_text(captured[1]["contents"])
    assert "ಮೊದಲ ಪ್ರಶ್ನೆ" in replayed
    assert "ಮೊದಲ ಉತ್ತರ" in replayed

    db = SessionLocal()
    try:
        roles = [
            row.role
            for row in db.scalars(
                select(AIMessage)
                .where(AIMessage.conversation_id == conversation_id)
                .order_by(AIMessage.id)
            ).all()
        ]
        owner = db.scalar(
            select(AIConversation.user_id).where(AIConversation.id == conversation_id)
        )
    finally:
        db.close()
    assert roles == ["user", "assistant", "user", "assistant"]
    assert owner is not None


def test_other_students_conversation_is_not_reachable(
    client, demo_token, token_for, isolation_users, gemini_key, monkeypatch
):
    _capture_calls(monkeypatch)
    first = client.post(
        f"{BASE}/chat", headers=_auth(demo_token), json={"message": "ಖಾಸಗಿ ಪ್ರಶ್ನೆ"}
    )
    assert first.status_code == 200, first.text
    conversation_id = first.json()["conversation_id"]

    other = token_for("iso_student_b")
    resp = client.post(
        f"{BASE}/chat",
        headers=_auth(other),
        json={"message": "ನಾನು ಯಾರು?", "conversation_id": conversation_id},
    )
    assert resp.status_code == 404, resp.text


def test_client_history_is_accepted_for_a_new_conversation(
    client, demo_token, gemini_key, monkeypatch
):
    captured = _capture_calls(monkeypatch)
    resp = client.post(
        f"{BASE}/chat",
        headers=_auth(demo_token),
        json={
            "message": "ಮುಂದುವರಿಸೋಣ",
            "history": [
                {"role": "user", "content": "ನೀರಿನ ಚಕ್ರ ಏನು?"},
                {"role": "assistant", "content": "ನೀರಿನ ಚಕ್ರವು..."},
            ],
        },
    )
    assert resp.status_code == 200, resp.text
    prompt = _contents_text(captured[0]["contents"])
    assert "ನೀರಿನ ಚಕ್ರ ಏನು?" in prompt
    assert "ನೀರಿನ ಚಕ್ರವು..." in prompt
