/**
 * Typed API client for the WonderNest FastAPI backend.
 *
 * The browser only ever talks to our own /api routes: the Gemini key lives on the server.
 * Set VITE_API_BASE_URL when the SPA is hosted separately from the backend.
 */

const RAW_BASE = import.meta.env.VITE_API_BASE_URL ?? "";
export const API_BASE = RAW_BASE.replace(/\/$/, "");

const ACCESS_TOKEN_KEY = "wondernest.access_token";
const REFRESH_TOKEN_KEY = "wondernest.refresh_token";

export function getAccessToken(): string | null {
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

export function setTokens(access: string, refresh: string): void {
  localStorage.setItem(ACCESS_TOKEN_KEY, access);
  localStorage.setItem(REFRESH_TOKEN_KEY, refresh);
}

export function clearTokens(): void {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
}

export class ApiError extends Error {
  status: number;
  code?: string;
  retryAfter?: number;

  constructor(message: string, status: number, code?: string, retryAfter?: number) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.code = code;
    this.retryAfter = retryAfter;
  }
}

type Detail = string | { code?: string; message?: string } | undefined;

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const headers = new Headers(init.headers);
  if (init.body && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }
  const token = getAccessToken();
  if (token) headers.set("Authorization", `Bearer ${token}`);

  let response: Response;
  try {
    response = await fetch(`${API_BASE}${path}`, { ...init, headers });
  } catch {
    throw new ApiError(
      "Cannot reach the WonderNest server. Check your connection and try again.",
      0,
      "network_error",
    );
  }

  if (response.status === 204) return undefined as T;

  const text = await response.text();
  let payload: unknown = null;
  if (text) {
    try {
      payload = JSON.parse(text);
    } catch {
      payload = null;
    }
  }

  if (!response.ok) {
    const detail = (payload as { detail?: Detail } | null)?.detail;
    const message =
      typeof detail === "string"
        ? detail
        : detail?.message ??
          (Array.isArray(detail)
            ? "Please check the details you entered."
            : "Something went wrong. Please try again.");
    const code = typeof detail === "object" && detail ? detail.code : undefined;
    const retryAfter = Number(response.headers.get("Retry-After") ?? "") || undefined;
    throw new ApiError(message, response.status, code, retryAfter);
  }

  return payload as T;
}

// --- Types -----------------------------------------------------------------------
export interface User {
  id: number;
  username: string;
  display_name: string;
  role: string;
  preferred_language: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
  user: User;
}

export interface StudentProfile {
  id: number;
  username: string;
  display_name: string;
  role: string;
  preferred_language: string;
  class_id: number | null;
  class_label: string | null;
  board_id: number | null;
  board_name_kn: string | null;
  language_code: string | null;
  daily_goal_minutes: number | null;
}

export interface Board {
  id: number;
  code: string;
  name_en: string;
  name_kn: string;
}

export interface ClassLevel {
  id: number;
  board_id: number;
  level_number: number;
  label: string;
}

export interface Subject {
  id: number;
  class_id: number;
  code: string;
  title_en: string;
  title_kn: string;
}

export interface Chapter {
  id: number;
  subject_id: number;
  number: number;
  title_en: string;
  title_kn: string;
  summary_kn: string | null;
  summary_en: string | null;
  category: string;
  is_enrichment: boolean;
  visualizations: string[];
  estimated_minutes: number;
  is_sample: boolean;
  source_note: string | null;
}

export interface Category {
  key: string;
  label_en: string;
  label_kn: string;
}

export interface VideoItem {
  title: string;
  language: string;
  topic: string;
  search_query: string;
  video_id: string | null;
}

export interface TopicDetail {
  id: number;
  order: number;
  title_en: string;
  title_kn: string;
  objectives: Objective[];
  lesson: Lesson | null;
}

export interface ChapterContent {
  chapter: Chapter;
  topics: TopicDetail[];
  notes_kn: string[];
  notes_en: string[];
  videos: VideoItem[];
  visualizations: string[];
  question_count: number;
}

export interface Topic {
  id: number;
  chapter_id: number;
  order: number;
  title_en: string;
  title_kn: string;
}

export interface KeyTerm {
  kn: string;
  en: string;
  meaning_kn: string;
  meaning_en: string | null;
}

export interface Lesson {
  id: number;
  topic_id: number;
  body_kn: string;
  body_en: string | null;
  key_terms: KeyTerm[];
  example_kn: string | null;
  example_en: string | null;
  is_sample: boolean;
  source_note: string | null;
}

export interface Objective {
  id: number;
  lesson_id: number;
  position: number;
  text_kn: string;
  text_en: string | null;
}

export interface LessonProgressRow {
  lesson_id: number;
  status: string;
  opened_at: string;
  completed_at: string | null;
  time_spent_seconds: number;
}

export interface Progress {
  lessons_opened: number;
  lessons_completed: number;
  quiz_attempts: number;
  lesson_progress: LessonProgressRow[];
  quiz_attempts_list: {
    id: number;
    chapter_id: number;
    score: number;
    total: number;
    created_at: string;
  }[];
}

export interface QuizQuestion {
  id: number;
  question_type: string;
  question_kn: string;
  question_en: string | null;
  options_kn: string[];
  options_en: string[];
  difficulty: number;
}

export interface Quiz {
  chapter_id: number;
  chapter_title_kn: string;
  chapter_title_en: string;
  category: string;
  total: number;
  questions: QuizQuestion[];
}

export interface QuizAnswerResult {
  question_id: number;
  selected_index: number | null;
  correct_index: number;
  is_correct: boolean;
  explanation_kn: string | null;
  explanation_en: string | null;
  question_kn: string;
  question_en: string | null;
  options_kn: string[];
  options_en: string[];
}

export interface QuizResult {
  attempt_id: number;
  chapter_id: number;
  chapter_title_kn: string;
  chapter_title_en: string;
  score: number;
  total: number;
  created_at: string;
  answers: QuizAnswerResult[];
}

export interface TranscribeResponse {
  text: string;
  model: string;
}

export interface NarrationStatus {
  available: boolean;
  model: string | null;
  reason: string | null;
  detail: string | null;
}

export interface NarrationAudio {
  audio_base64: string;
  mime_type: string;
  model: string;
  voice: string | null;
  language: string;
  cached: boolean;
}

export interface ExamQuestion {
  id: string;
  type: string;
  marks: number;
  difficulty: number;
  question_en: string;
  question_kn: string;
  answer_en: string;
  answer_kn: string;
  explanation_en: string;
  explanation_kn: string;
  options_en: string[];
  options_kn: string[];
  correct_index: number | null;
}

export interface ExamTypeCount {
  key: string;
  label_en: string;
  label_kn: string;
  count: number;
}

export interface ExamQuestions {
  chapter_id: number;
  chapter_number: number;
  source_note: string;
  total: number;
  types: ExamTypeCount[];
  questions: ExamQuestion[];
}

export interface TutorStatus {
  configured: boolean;
  provider: string;
  model: string;
  message: string;
  rate_limit_requests: number;
  rate_limit_window_seconds: number;
  max_message_chars: number;
}

export interface SuggestedPrompt {
  id: string;
  label: string;
  label_kn: string;
  prompt: string;
  language: "kn" | "en";
  topic: string;
}

export type TutorLanguage = "kn" | "en";
export type TutorLevel = "beginner" | "class8" | "advanced";

export interface TutorChatRequest {
  message: string;
  language: TutorLanguage;
  level: TutorLevel;
  chapter_id?: number;
  topic_id?: number;
  lesson_id?: number;
  conversation_id?: number;
}

export interface TutorChatResponse {
  reply: string;
  conversation_id: number;
  provider: string;
  model: string;
  language: TutorLanguage;
  latency_ms: number;
  usage: {
    prompt_tokens: number | null;
    response_tokens: number | null;
    total_tokens: number | null;
  } | null;
}

// --- Endpoints -------------------------------------------------------------------
export const api = {
  login: (username: string, password: string) =>
    request<TokenResponse>("/api/auth/login", {
      method: "POST",
      body: JSON.stringify({ username, password }),
    }),
  me: () => request<User>("/api/auth/me"),
  profile: () => request<StudentProfile>("/api/students/me"),
  progress: () => request<Progress>("/api/students/progress"),
  recordLessonProgress: (lessonId: number, status: "opened" | "completed", seconds = 0) =>
    request<LessonProgressRow>(`/api/students/lessons/${lessonId}/progress`, {
      method: "POST",
      body: JSON.stringify({ status, time_spent_seconds: seconds }),
    }),
  boards: () => request<Board[]>("/api/curriculum/boards"),
  classes: (boardId: number) => request<ClassLevel[]>(`/api/curriculum/boards/${boardId}/classes`),
  subjects: (classId: number) =>
    request<Subject[]>(`/api/curriculum/classes/${classId}/subjects`),
  chapters: (subjectId: number) =>
    request<Chapter[]>(`/api/curriculum/subjects/${subjectId}/chapters`),
  categories: () => request<Category[]>("/api/curriculum/categories"),
  chapterContent: (chapterId: number) =>
    request<ChapterContent>(`/api/curriculum/chapters/${chapterId}/content`),
  topics: (chapterId: number) => request<Topic[]>(`/api/curriculum/chapters/${chapterId}/topics`),
  lessons: (topicId: number) => request<Lesson[]>(`/api/curriculum/topics/${topicId}/lessons`),
  lesson: (lessonId: number) => request<Lesson>(`/api/curriculum/lessons/${lessonId}`),
  objectives: (lessonId: number) =>
    request<Objective[]>(`/api/curriculum/lessons/${lessonId}/objectives`),
  quiz: (chapterId: number) => request<Quiz>(`/api/quiz/chapters/${chapterId}`),
  submitQuiz: (chapterId: number, answers: { question_id: number; selected_index: number | null }[]) =>
    request<QuizResult>(`/api/quiz/chapters/${chapterId}/attempts`, {
      method: "POST",
      body: JSON.stringify({ answers }),
    }),
  attempt: (attemptId: number) => request<QuizResult>(`/api/quiz/attempts/${attemptId}`),
  tutorStatus: () => request<TutorStatus>("/api/ai/tutor/status"),
  tutorSuggestions: () =>
    request<{ prompts: SuggestedPrompt[] }>("/api/ai/tutor/suggestions"),
  tutorChat: (body: TutorChatRequest) =>
    request<TutorChatResponse>("/api/ai/tutor/chat", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  transcribeVoice: (body: { audio_base64: string; mime_type: string; language: "kn" | "en" }) =>
    request<TranscribeResponse>("/api/ai/tutor/transcribe", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  narrationStatus: () => request<NarrationStatus>("/api/narration/status"),
  narrationSpeak: (text: string, language: "kn" | "en") =>
    request<NarrationAudio>("/api/narration/speak", {
      method: "POST",
      body: JSON.stringify({ text, language }),
    }),
  chapterExam: (chapterId: number, type?: string) =>
    request<ExamQuestions>(
      `/api/curriculum/chapters/${chapterId}/exam${type ? `?type=${encodeURIComponent(type)}` : ""}`,
    ),
};
