"""Google Gemini powered AI tutor service.

The service owns everything that talks to Google: client creation, prompt construction,
model fallback, error translation and safe logging. The API layer only supplies the
student's identity, the message and the optional curriculum context, so the API key can
never leak into a request body or a browser bundle.

Logging policy: student message text and the API key are never logged. Only the user id,
model name, latency, token counts and error codes are recorded.
"""

from __future__ import annotations

import asyncio
import inspect
import logging
import threading
import time
from collections import deque
from dataclasses import dataclass, field

from google import genai
from google.genai import errors as genai_errors
from google.genai import types as genai_types

from app.core.config import get_settings

logger = logging.getLogger("wondernest.ai")

PROVIDER = "google-gemini"

# Tried in order when the configured model is missing for this key or is temporarily
# overloaded (Gemini answers 503 UNAVAILABLE during demand spikes).
FALLBACK_FLASH_MODELS: tuple[str, ...] = (
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
)


# --------------------------------------------------------------------------------------
# Errors
# --------------------------------------------------------------------------------------
class TutorError(Exception):
    """Base class for tutor failures that map to a safe HTTP response."""

    status_code = 500
    code = "ai_error"
    default_message = "The AI tutor is unavailable right now. Please try again."
    default_retry_after: int | None = None

    def __init__(self, message: str | None = None, *, retry_after: int | None = None) -> None:
        super().__init__(message or self.default_message)
        self.message = message or self.default_message
        self.retry_after = retry_after if retry_after is not None else self.default_retry_after


class AINotConfiguredError(TutorError):
    status_code = 503
    code = "ai_not_configured"
    default_message = (
        "The AI tutor is not configured on this server yet. "
        "An administrator must set GEMINI_API_KEY before the tutor can answer questions."
    )


class AIInvalidKeyError(TutorError):
    status_code = 503
    code = "ai_invalid_key"
    default_message = (
        "The server's Gemini API key was rejected by Google. "
        "Please check GEMINI_API_KEY in the backend environment."
    )


class AIRateLimitedError(TutorError):
    status_code = 429
    code = "ai_rate_limited"
    default_message = "You are asking questions very quickly. Please wait a moment and try again."
    default_retry_after = 20


class AIQuotaExceededError(TutorError):
    status_code = 429
    code = "ai_quota_exceeded"
    default_message = "The AI tutor has reached its usage limit for now. Please try again later."
    default_retry_after = 60


class AITimeoutError(TutorError):
    status_code = 504
    code = "ai_timeout"
    default_message = "The AI tutor took too long to answer. Please try again."


class AIProviderError(TutorError):
    status_code = 502
    code = "ai_provider_error"
    default_message = "The AI service could not answer right now. Please try again."


class AIEmptyResponseError(TutorError):
    status_code = 502
    code = "ai_empty_response"
    default_message = "The AI tutor did not return an answer. Please rephrase your question."


class AIBlockedError(TutorError):
    status_code = 400
    code = "ai_blocked"
    default_message = (
        "That question could not be answered. Try asking about your Class 8 science lesson."
    )


# --------------------------------------------------------------------------------------
# Rate limiting (per authenticated student, in-process sliding window)
# --------------------------------------------------------------------------------------
class SlidingWindowRateLimiter:
    """Small in-memory limiter.

    Adequate for a single-process prototype; a multi-worker deployment should use a shared
    store such as Redis. ``check`` returns ``None`` when the call is allowed, otherwise the
    number of seconds until the oldest hit leaves the window.
    """

    def __init__(self) -> None:
        self._hits: dict[str, deque[float]] = {}
        self._lock = threading.Lock()

    def check(self, key: str, limit: int, window_seconds: int) -> float | None:
        now = time.monotonic()
        with self._lock:
            hits = self._hits.setdefault(key, deque())
            cutoff = now - window_seconds
            while hits and hits[0] <= cutoff:
                hits.popleft()
            if len(hits) >= limit:
                return max(0.1, hits[0] + window_seconds - now)
            hits.append(now)
            return None

    def reset(self, key: str | None = None) -> None:
        with self._lock:
            if key is None:
                self._hits.clear()
            else:
                self._hits.pop(key, None)


rate_limiter = SlidingWindowRateLimiter()


# --------------------------------------------------------------------------------------
# Prompt construction
# --------------------------------------------------------------------------------------
@dataclass
class TutorContext:
    """Curriculum context for one lesson. Everything here is sample WonderNest material."""

    chapter_title_kn: str | None = None
    chapter_title_en: str | None = None
    topic_title_kn: str | None = None
    topic_title_en: str | None = None
    lesson_body: str | None = None
    key_terms: list[str] = field(default_factory=list)
    objectives: list[str] = field(default_factory=list)


@dataclass
class TutorReply:
    text: str
    model: str
    latency_ms: int
    usage: dict[str, int | None] | None = None


_TUTOR_RULES = """\
You are the WonderNest AI Tutor, a patient science tutor for Karnataka State Board Class 8 students.
Your subject is Class 8 Science.

How you answer:
- Explain in the language the student chose. If the language is Kannada, write in Kannada script
  (ಕನ್ನಡ) and keep the technical English term in brackets the first time, e.g. ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ (photosynthesis).
- Use short sentences and short paragraphs. Aim for about 120-220 words unless the student asks for more.
- Start with a one-line direct answer, then explain step by step.
- Always give at least one everyday example from a student's life in Karnataka (a garden, a bicycle,
  a kitchen, a bus, rain, a cricket ball).
- Explain difficult terms in a short "key words" list at the end.
- Never give an answer that sounds like an official textbook quote. Never invent book names, page
  numbers, chapter numbers or citations. If you use the lesson notes provided, say "in this lesson"
  rather than claiming they are official curriculum material.
- When a student asks about a quiz or practice question, give a hint that helps them think first.
  Reveal the full answer only if the student asks again or says they are stuck.
- Be encouraging and specific ("you already know that plants need water, so..."). Never talk down
  to the student and never call a question silly.
- End with exactly one short follow-up question that checks understanding.
- If a question is outside Class 8 science, answer briefly and bring the conversation back to science.
- If you are not sure about a fact, say what you are unsure about instead of inventing it.
- Do not ask for or repeat personal details. Do not use markdown tables or code blocks.
"""

_LEVEL_RULES = {
    "beginner": (
        "The student is a beginner: use very simple words, at most 10-12 words per sentence, "
        "and one idea per line. Avoid formulas."
    ),
    "class8": (
        "The student is in Class 8 (about 13 years old): use clear everyday school language and "
        "introduce the correct scientific term once, in brackets."
    ),
    "advanced": (
        "The student is confident: keep the explanation tight, use the scientific terms, and add "
        "one short 'think deeper' challenge at the end before the checking question."
    ),
}


def build_system_instruction(language: str, level: str) -> str:
    language_rule = (
        "Reply in Kannada (ಕನ್ನಡ script) only. Keep English scientific terms in brackets."
        if language == "kn"
        else "Reply in simple English only, with a short Kannada term in brackets where it helps."
    )
    level_rule = _LEVEL_RULES.get(level, _LEVEL_RULES["class8"])
    return f"{_TUTOR_RULES}\nLanguage: {language_rule}\nLevel: {level_rule}"


def build_context_block(context: TutorContext | None) -> str:
    if context is None:
        return ""
    lines: list[str] = []
    if context.chapter_title_kn or context.chapter_title_en:
        lines.append(
            "Chapter: "
            + " / ".join(part for part in (context.chapter_title_kn, context.chapter_title_en) if part)
        )
    if context.topic_title_kn or context.topic_title_en:
        lines.append(
            "Topic: "
            + " / ".join(part for part in (context.topic_title_kn, context.topic_title_en) if part)
        )
    if context.lesson_body:
        body = context.lesson_body.strip()
        lines.append(f"Lesson notes: {body[:1800]}")
    if context.key_terms:
        lines.append("Key terms: " + "; ".join(context.key_terms[:10]))
    if context.objectives:
        lines.append("Learning objectives: " + "; ".join(context.objectives[:6]))
    if not lines:
        return ""
    return (
        "LESSON CONTEXT (WonderNest sample material, not an official textbook):\n"
        + "\n".join(lines)
        + "\n\nUse this context when it helps, but do not claim it is official curriculum text.\n"
    )


def build_user_prompt(message: str, context: TutorContext | None) -> str:
    block = build_context_block(context)
    if block:
        return f"{block}\nStudent question: {message}"
    return f"Student question: {message}"


def build_contents(
    *,
    message: str,
    context: TutorContext | None,
    history: list[dict[str, str]],
    max_history_messages: int,
) -> list[genai_types.Content]:
    contents: list[genai_types.Content] = []
    for turn in history[-max_history_messages:] if max_history_messages > 0 else []:
        text = (turn.get("content") or "").strip()
        if not text:
            continue
        role = "user" if turn.get("role") == "user" else "model"
        contents.append(
            genai_types.Content(role=role, parts=[genai_types.Part(text=text[:1200])])
        )
    contents.append(
        genai_types.Content(
            role="user", parts=[genai_types.Part(text=build_user_prompt(message, context))]
        )
    )
    return contents


# --------------------------------------------------------------------------------------
# Client and model resolution
# --------------------------------------------------------------------------------------
_client_lock = threading.Lock()
_client_cache: dict[str, genai.Client] = {}
# configured model name -> model that actually answered
_model_cache: dict[str, str] = {}


def is_configured() -> bool:
    return bool(get_settings().GEMINI_API_KEY.strip())


def _get_client(api_key: str) -> genai.Client:
    with _client_lock:
        client = _client_cache.get(api_key)
        if client is None:
            timeout_ms = int(get_settings().GEMINI_TIMEOUT_SECONDS * 1000)
            client = genai.Client(
                api_key=api_key, http_options=genai_types.HttpOptions(timeout=timeout_ms)
            )
            _client_cache[api_key] = client
        return client


def reset_caches() -> None:
    """Drop cached clients and resolved models. Used by tests after changing settings."""
    with _client_lock:
        _client_cache.clear()
        _model_cache.clear()


def configured_model() -> str:
    return get_settings().GEMINI_MODEL.strip() or "gemini-2.5-flash"


async def _available_flash_models(client: genai.Client) -> list[str]:
    """Ask Gemini which Flash models this key can use. Never raises."""
    try:
        listing = client.aio.models.list()
        if inspect.isawaitable(listing):
            listing = await listing
        names: list[str] = []
        async for model in listing:  # type: ignore[union-attr]
            name = (getattr(model, "name", "") or "").removeprefix("models/")
            if "flash" not in name:
                continue
            methods = getattr(model, "supported_actions", None) or getattr(
                model, "supported_generation_methods", None
            )
            if methods and "generateContent" not in methods:
                continue
            names.append(name)
        return names
    except Exception:  # pragma: no cover - discovery is best effort
        return []


def _error_code(exc: Exception) -> int:
    code = getattr(exc, "code", None)
    if isinstance(code, int):
        return code
    status = str(getattr(exc, "status", "") or "")
    mapping = {
        "INVALID_ARGUMENT": 400,
        "FAILED_PRECONDITION": 400,
        "UNAUTHENTICATED": 401,
        "PERMISSION_DENIED": 403,
        "NOT_FOUND": 404,
        "RESOURCE_EXHAUSTED": 429,
        "DEADLINE_EXCEEDED": 504,
        "INTERNAL": 500,
        "UNAVAILABLE": 503,
    }
    return mapping.get(status.upper(), 500)


def _error_text(exc: Exception) -> str:
    parts = [
        str(getattr(exc, "message", "") or ""),
        str(getattr(exc, "status", "") or ""),
    ]
    return " ".join(parts).lower()


def _is_model_not_found(exc: Exception) -> bool:
    return _error_code(exc) == 404


def _is_transient(exc: Exception) -> bool:
    """Provider-side failure that another model can probably serve right away."""
    return _error_code(exc) in (500, 502, 503, 504)


def fallback_models() -> list[str]:
    """Models to try after the configured one, from settings or the built-in chain."""
    raw = get_settings().GEMINI_FALLBACK_MODELS
    names = [part.strip() for part in raw.split(",") if part.strip()]
    return names or list(FALLBACK_FLASH_MODELS)


def translate_client_error(exc: Exception) -> TutorError:
    """Map a google-genai client error to a tutor error without leaking provider details."""
    code = _error_code(exc)
    text = _error_text(exc)
    if code in (401, 403) or "api key" in text or "api_key" in text or "unauthenticated" in text:
        return AIInvalidKeyError()
    if code == 429:
        if "quota" in text or "resource_exhausted" in text or "billing" in text:
            return AIQuotaExceededError()
        return AIRateLimitedError()
    if code in (408, 504) or "deadline" in text or "timeout" in text:
        return AITimeoutError()
    if code == 400 and ("safety" in text or "blocked" in text or "policy" in text):
        return AIBlockedError()
    if code == 400 and ("api key" in text or "invalid argument" in text and "model" in text):
        return AIProviderError()
    return AIProviderError()


async def _call_model(
    client: genai.Client,
    model: str,
    contents: list[genai_types.Content],
    config: genai_types.GenerateContentConfig,
    timeout_seconds: float,
) -> genai_types.GenerateContentResponse:
    return await asyncio.wait_for(
        client.aio.models.generate_content(model=model, contents=contents, config=config),
        timeout=timeout_seconds,
    )


async def _generate(
    client: genai.Client,
    contents: list[genai_types.Content],
    config: genai_types.GenerateContentConfig,
    *,
    timeout_seconds: float,
) -> tuple[genai_types.GenerateContentResponse, str]:
    """Generate a reply, falling back to an available Flash model when needed."""
    requested = configured_model()
    resolved = _model_cache.get(requested)
    candidates = [resolved or requested]
    for model in fallback_models():
        if model not in candidates:
            candidates.append(model)

    last_error: Exception | None = None
    for index, model in enumerate(candidates):
        try:
            response = await _call_model(client, model, contents, config, timeout_seconds)
        except genai_errors.ClientError as exc:
            if not _is_model_not_found(exc):
                raise translate_client_error(exc) from exc
            last_error = exc
            logger.warning(
                "Gemini model unavailable model=%s configured=%s", model, requested
            )
            if index == 0:
                discovered = await _available_flash_models(client)
                for name in discovered:
                    if name not in candidates:
                        candidates.append(name)
            continue
        except genai_errors.ServerError as exc:
            last_error = exc
            if not _is_transient(exc):
                raise AIProviderError() from exc
            logger.warning(
                "Gemini model busy, trying next candidate model=%s code=%s",
                model,
                _error_code(exc),
            )
            continue
        except (asyncio.TimeoutError, TimeoutError) as exc:
            raise AITimeoutError() from exc
        except Exception as exc:  # network/DNS/TLS failures surface here
            if "timeout" in type(exc).__name__.lower() or "timeout" in str(exc).lower():
                raise AITimeoutError() from exc
            raise AIProviderError() from exc

        if model != requested:
            _model_cache[requested] = model
            logger.warning("Using fallback Gemini model model=%s configured=%s", model, requested)
        return response, model

    raise AIProviderError() from last_error


def _extract_text(response: genai_types.GenerateContentResponse) -> str:
    try:
        text = response.text
    except Exception:
        text = None
    if text and text.strip():
        return text.strip()
    # A blocked or empty candidate has no text; distinguish it for a friendlier message.
    feedback = getattr(response, "prompt_feedback", None)
    reason = getattr(feedback, "block_reason", None) if feedback is not None else None
    if reason:
        raise AIBlockedError()
    raise AIEmptyResponseError()


def _usage(response: genai_types.GenerateContentResponse) -> dict[str, int | None] | None:
    metadata = getattr(response, "usage_metadata", None)
    if metadata is None:
        return None
    return {
        "prompt_tokens": getattr(metadata, "prompt_token_count", None),
        "response_tokens": getattr(metadata, "candidates_token_count", None),
        "total_tokens": getattr(metadata, "total_token_count", None),
    }


async def generate_tutor_reply(
    *,
    message: str,
    language: str,
    level: str,
    context: TutorContext | None,
    history: list[dict[str, str]] | None = None,
    user_id: int | None = None,
) -> TutorReply:
    """Ask Gemini for a tutor reply. Raises a ``TutorError`` subclass on any failure."""
    settings = get_settings()
    api_key = settings.GEMINI_API_KEY.strip()
    if not api_key:
        raise AINotConfiguredError()

    contents = build_contents(
        message=message,
        context=context,
        history=history or [],
        max_history_messages=settings.AI_MAX_HISTORY_MESSAGES,
    )
    config = genai_types.GenerateContentConfig(
        system_instruction=build_system_instruction(language, level),
        temperature=0.6,
        top_p=0.95,
        max_output_tokens=settings.GEMINI_MAX_OUTPUT_TOKENS,
    )

    client = _get_client(api_key)
    started = time.perf_counter()
    response, model = await _generate(
        client,
        contents,
        config,
        timeout_seconds=settings.GEMINI_TIMEOUT_SECONDS + 5,
    )
    text = _extract_text(response)
    latency_ms = int((time.perf_counter() - started) * 1000)
    usage = _usage(response)

    logger.info(
        "ai_tutor_reply user_id=%s model=%s language=%s level=%s latency_ms=%s "
        "prompt_tokens=%s response_tokens=%s history_turns=%s",
        user_id,
        model,
        language,
        level,
        latency_ms,
        (usage or {}).get("prompt_tokens"),
        (usage or {}).get("response_tokens"),
        len(history or []),
    )
    return TutorReply(text=text, model=model, latency_ms=latency_ms, usage=usage)
