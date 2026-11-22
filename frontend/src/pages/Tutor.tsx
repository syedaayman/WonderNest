import { useEffect, useRef, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";

import { RichText } from "../components/RichText";
import {
  ApiError,
  api,
  type SuggestedPrompt,
  type TutorLanguage,
  type TutorLevel,
  type TutorStatus,
} from "../lib/api";
import { useAuth } from "../lib/auth";

interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  text: string;
  at: Date;
  model?: string;
  latencyMs?: number;
}

const LEVELS: { id: TutorLevel; label: string; hint: string }[] = [
  { id: "beginner", label: "Beginner", hint: "Very simple words" },
  { id: "class8", label: "Class 8", hint: "Standard level" },
  { id: "advanced", label: "Advanced", hint: "Deeper detail" },
];

function timeLabel(date: Date): string {
  return date.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" });
}

export default function Tutor() {
  const { user } = useAuth();
  const [searchParams, setSearchParams] = useSearchParams();

  const chapterParam = searchParams.get("chapter");
  const topicParam = searchParams.get("topic");
  const lessonParam = searchParams.get("lesson");
  const titleParam = searchParams.get("title");
  const initialQuestion = searchParams.get("q") ?? "";

  const [status, setStatus] = useState<TutorStatus | null>(null);
  const [suggestions, setSuggestions] = useState<SuggestedPrompt[]>([]);
  const [language, setLanguage] = useState<TutorLanguage>("kn");
  const [level, setLevel] = useState<TutorLevel>("class8");
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState(initialQuestion);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<{ message: string; code?: string; retryAfter?: number } | null>(
    null,
  );
  const [conversationId, setConversationId] = useState<number | undefined>(undefined);
  const [copiedId, setCopiedId] = useState<string | null>(null);

  const endRef = useRef<HTMLDivElement | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

  const hasContext = Boolean(chapterParam || topicParam || lessonParam);
  const maxChars = status?.max_message_chars ?? 1200;
  const configured = status?.configured ?? false;

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const [statusData, suggestionData] = await Promise.all([
          api.tutorStatus(),
          api.tutorSuggestions(),
        ]);
        if (!active) return;
        setStatus(statusData);
        setSuggestions(suggestionData.prompts);
      } catch (err) {
        if (!active) return;
        setError({
          message:
            err instanceof ApiError
              ? err.message
              : "Could not reach the tutor service. Please refresh.",
        });
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [messages, sending]);

  async function send(rawText: string, overrideLanguage?: TutorLanguage) {
    const text = rawText.trim();
    if (!text || sending) return;
    if (text.length > maxChars) {
      setError({ message: `Please keep your question under ${maxChars} characters.` });
      return;
    }

    setError(null);
    setMessages((current) => [
      ...current,
      { id: `u-${Date.now()}`, role: "user", text, at: new Date() },
    ]);
    setInput("");
    setSending(true);

    try {
      const reply = await api.tutorChat({
        message: text,
        language: overrideLanguage ?? language,
        level,
        chapter_id: chapterParam ? Number(chapterParam) : undefined,
        topic_id: topicParam ? Number(topicParam) : undefined,
        lesson_id: lessonParam ? Number(lessonParam) : undefined,
        conversation_id: conversationId,
      });
      setConversationId(reply.conversation_id);
      setMessages((current) => [
        ...current,
        {
          id: `a-${Date.now()}`,
          role: "assistant",
          text: reply.reply,
          at: new Date(),
          model: reply.model,
          latencyMs: reply.latency_ms,
        },
      ]);
    } catch (err) {
      if (err instanceof ApiError) {
        setError({ message: err.message, code: err.code, retryAfter: err.retryAfter });
      } else {
        setError({ message: "The tutor could not answer just now. Please try again." });
      }
    } finally {
      setSending(false);
      textareaRef.current?.focus();
    }
  }

  function clearConversation() {
    setMessages([]);
    setConversationId(undefined);
    setError(null);
    textareaRef.current?.focus();
  }

  async function copyMessage(message: ChatMessage) {
    try {
      await navigator.clipboard.writeText(message.text);
      setCopiedId(message.id);
      window.setTimeout(() => setCopiedId(null), 1600);
    } catch {
      setError({ message: "Your browser blocked copying. Select the text and copy manually." });
    }
  }

  function clearContext() {
    setSearchParams({});
  }

  return (
    <div className="container tutor-shell">
      <header className="tutor-header card card-tight">
        <div className="row-between">
          <div className="row">
            <span className="tutor-avatar" aria-hidden="true">
              ✦
            </span>
            <div>
              <h1 style={{ fontSize: "1.25rem", marginBottom: 0 }}>WonderNest AI Tutor</h1>
              <small className="muted">
                Powered by Google Gemini
                {status?.model ? ` · ${status.model}` : ""}
                {configured ? " · live" : ""}
              </small>
            </div>
          </div>
          <div className="row" style={{ gap: "0.5rem" }}>
            <span className={configured ? "badge badge-ok" : "badge badge-warn"}>
              {configured ? "AI online" : "AI not configured"}
            </span>
            <button
              type="button"
              className="btn btn-ghost btn-sm"
              onClick={clearConversation}
              disabled={!messages.length}
            >
              Clear conversation
            </button>
          </div>
        </div>

        <div className="tutor-controls">
          <div className="segmented" role="group" aria-label="Answer language">
            <button
              type="button"
              className={language === "kn" ? "segmented-item active" : "segmented-item"}
              onClick={() => setLanguage("kn")}
              aria-pressed={language === "kn"}
            >
              ಕನ್ನಡ
            </button>
            <button
              type="button"
              className={language === "en" ? "segmented-item active" : "segmented-item"}
              onClick={() => setLanguage("en")}
              aria-pressed={language === "en"}
            >
              English
            </button>
          </div>

          <label className="inline-field">
            <span className="label" style={{ marginBottom: 0 }}>
              Level
            </span>
            <select
              className="select select-sm"
              value={level}
              onChange={(event) => setLevel(event.target.value as TutorLevel)}
              aria-label="Explanation level"
            >
              {LEVELS.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.label} — {option.hint}
                </option>
              ))}
            </select>
          </label>

          {hasContext ? (
            <span className="badge badge-context">
              Lesson context: {titleParam ?? "selected chapter"}
              <button
                type="button"
                className="badge-clear"
                onClick={clearContext}
                aria-label="Remove lesson context"
              >
                ×
              </button>
            </span>
          ) : null}
        </div>
      </header>

      {!configured && status ? (
        <div className="alert alert-warn" role="alert">
          <strong>AI tutor is not configured.</strong>
          <p style={{ margin: "0.35rem 0 0" }}>
            The backend is missing a valid <code>GEMINI_API_KEY</code>. Add it to the server
            environment (Settings → Environment variables) and restart the backend. The tutor
            never returns placeholder answers, so it stays disabled until the key is present.
          </p>
          <p style={{ margin: "0.35rem 0 0", fontSize: "0.85rem" }}>
            {status.message}
          </p>
        </div>
      ) : null}

      <div className="chat-log card" ref={undefined}>
        {messages.length === 0 ? (
          <div className="chat-empty">
            <span className="tutor-avatar large" aria-hidden="true">
              ✦
            </span>
            <h2 style={{ marginBottom: "0.3rem" }}>
              ನಮಸ್ಕಾರ {user?.display_name ?? "friend"}! Ask me anything about Class 8 Science.
            </h2>
            <p className="muted" style={{ maxWidth: 520 }}>
              I explain concepts in Kannada or English, use everyday examples, give hints for quiz
              questions and ask you questions back. I am an AI study helper — not an official
              textbook.
            </p>
            <div className="chips" style={{ justifyContent: "center" }}>
              {suggestions.map((prompt) => (
                <button
                  key={prompt.id}
                  type="button"
                  className="chip"
                  onClick={() => {
                    setLanguage(prompt.language);
                    void send(prompt.prompt, prompt.language);
                  }}
                  disabled={sending}
                >
                  {language === "kn" ? prompt.label_kn : prompt.label}
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((message) => (
            <div key={message.id} className={`msg msg-${message.role}`}>
              <div className="msg-bubble">
                <div className="msg-meta">
                  <strong>{message.role === "user" ? "You" : "AI Tutor"}</strong>
                  <span>{timeLabel(message.at)}</span>
                  {message.model ? <span className="msg-model">Gemini</span> : null}
                </div>
                {message.role === "assistant" ? (
                  <div className="msg-text">
                    <RichText text={message.text} />
                  </div>
                ) : (
                  <p className="msg-text kan" lang="kn">
                    {message.text}
                  </p>
                )}
                {message.role === "assistant" ? (
                  <div className="msg-actions">
                    <button
                      type="button"
                      className="link-button"
                      onClick={() => copyMessage(message)}
                    >
                      {copiedId === message.id ? "Copied ✓" : "Copy"}
                    </button>
                    {message.latencyMs ? (
                      <span className="muted" style={{ fontSize: "0.72rem" }}>
                        {(message.latencyMs / 1000).toFixed(1)}s
                      </span>
                    ) : null}
                  </div>
                ) : null}
              </div>
            </div>
          ))
        )}

        {sending ? (
          <div className="msg msg-assistant">
            <div className="msg-bubble">
              <div className="msg-meta">
                <strong>AI Tutor</strong>
                <span>{timeLabel(new Date())}</span>
              </div>
              <div className="typing" aria-label="Tutor is thinking">
                <span />
                <span />
                <span />
              </div>
            </div>
          </div>
        ) : null}

        <div ref={endRef} />
      </div>

      {error ? (
        <div className="alert alert-danger" role="alert">
          <strong>{error.code === "rate_limited" ? "Slow down a little." : "Tutor error"}</strong>
          <p style={{ margin: "0.3rem 0 0" }}>{error.message}</p>
          {error.retryAfter ? (
            <p style={{ margin: "0.3rem 0 0", fontSize: "0.85rem" }}>
              Try again in about {error.retryAfter} seconds.
            </p>
          ) : null}
        </div>
      ) : null}

      <form
        className="composer card"
        onSubmit={(event) => {
          event.preventDefault();
          void send(input);
        }}
      >
        <label className="sr-only" htmlFor="tutor-input">
          Your question for the AI tutor
        </label>
        <textarea
          id="tutor-input"
          ref={textareaRef}
          className="textarea"
          rows={2}
          placeholder={
            language === "kn"
              ? "ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಇಲ್ಲಿ ಬರೆಯಿರಿ… (ಉದಾ: ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?)"
              : "Ask your question here… (e.g. What is friction?)"
          }
          value={input}
          maxLength={maxChars}
          onChange={(event) => setInput(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) {
              event.preventDefault();
              void send(input);
            }
          }}
          disabled={sending || !configured}
        />
        <div className="composer-bar">
          <span className="muted" style={{ fontSize: "0.76rem" }}>
            {input.length}/{maxChars} · Enter to send, Shift+Enter for a new line
          </span>
          <div className="row" style={{ gap: "0.4rem" }}>
            {status ? (
              <span className="muted" style={{ fontSize: "0.76rem" }}>
                {status.rate_limit_requests} questions / {status.rate_limit_window_seconds}s
              </span>
            ) : null}
            <button
              type="submit"
              className="btn btn-primary"
              disabled={sending || !configured || !input.trim()}
            >
              {sending ? "Thinking…" : "Ask tutor"}
            </button>
          </div>
        </div>
      </form>

      {suggestions.length && messages.length ? (
        <div className="chips">
          {suggestions.slice(0, 4).map((prompt) => (
            <button
              key={prompt.id}
              type="button"
              className="chip"
              onClick={() => {
                setLanguage(prompt.language);
                void send(prompt.prompt, prompt.language);
              }}
              disabled={sending || !configured}
            >
              {language === "kn" ? prompt.label_kn : prompt.label}
            </button>
          ))}
        </div>
      ) : null}

      <p className="muted" style={{ fontSize: "0.78rem" }}>
        Responses are generated by Google Gemini for learning support. They are not official
        Karnataka State Board material — always check your textbook.{" "}
        <Link to="/curriculum">Browse curriculum</Link>
      </p>
    </div>
  );
}
