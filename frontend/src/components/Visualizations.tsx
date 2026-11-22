/**
 * Hand-built, dependency-free science diagrams.
 *
 * Every diagram is a real interactive SVG or CSS scene with Kannada and English labels: nothing
 * here is a static picture pretending to be interactive, and no external image is loaded. Each
 * export is registered in VISUALIZATIONS so a chapter can name the diagrams it needs.
 */

import { useMemo, useState } from "react";

import { pick, useLanguage, type Lang } from "../lib/i18n";
import type { ReactElement } from "react";

interface DiagramProps {
  lang: Lang;
}

/* ------------------------------------------------------------------ photosynthesis */

const PHOTO_STEPS: { en: string; kn: string }[] = [
  {
    en: "Sunlight falls on the leaf and is trapped by the green pigment chlorophyll.",
    kn: "ಸೂರ್ಯನ ಬೆಳಕು ಎಲೆಯ ಮೇಲೆ ಬೀಳುತ್ತದೆ ಮತ್ತು ಹಸಿರು ಬಣ್ಣದ ಕ್ಲೋರೋಫಿಲ್ ಅದನ್ನು ಹಿಡಿದಿಡುತ್ತದೆ.",
  },
  {
    en: "Roots absorb water from the soil and it travels up to the leaf.",
    kn: "ಬೇರುಗಳು ಮಣ್ಣಿನಿಂದ ನೀರನ್ನು ಹೀರಿಕೊಳ್ಳುತ್ತವೆ ಮತ್ತು ಅದು ಎಲೆಗೆ ತಲುಪುತ್ತದೆ.",
  },
  {
    en: "Carbon dioxide enters the leaf through tiny pores called stomata.",
    kn: "ಕಾರ್ಬನ್ ಡೈಆಕ್ಸೈಡ್ ಸ್ಟೊಮಾಟಾ ಎಂಬ ಸಣ್ಣ ರಂಧ್ರಗಳ ಮೂಲಕ ಎಲೆಯನ್ನು ಪ್ರವೇಶಿಸುತ್ತದೆ.",
  },
  {
    en: "Water and carbon dioxide are joined using light energy to make glucose, the plant's food.",
    kn: "ಬೆಳಕಿನ ಶಕ್ತಿಯನ್ನು ಬಳಸಿ ನೀರು ಮತ್ತು ಕಾರ್ಬನ್ ಡೈಆಕ್ಸೈಡ್ ಸೇರಿ ಗ್ಲೂಕೋಸ್ — ಸಸ್ಯದ ಆಹಾರ — ತಯಾರಾಗುತ್ತದೆ.",
  },
  {
    en: "Oxygen is released into the air as a by-product. That is the air we breathe.",
    kn: "ಆಮ್ಲಜನಕ ಉಪ-ಉತ್ಪನ್ನವಾಗಿ ಗಾಳಿಗೆ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ. ಅದೇ ನಾವು ಉಸಿರಾಡುವ ಗಾಳಿ.",
  },
];

function PhotosynthesisDiagram({ lang }: DiagramProps) {
  const [step, setStep] = useState(0);
  const active = (index: number) => (step >= index ? "ps-on" : "ps-off");

  return (
    <div className="viz">
      <svg viewBox="0 0 520 330" role="img" aria-label="Photosynthesis diagram" className="viz-svg">
        <defs>
          <linearGradient id="leafGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="#34d399" />
            <stop offset="100%" stopColor="#0f766e" />
          </linearGradient>
          <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#fef9c3" />
            <stop offset="100%" stopColor="#f4f7f4" />
          </linearGradient>
        </defs>

        <rect x="0" y="0" width="520" height="330" rx="16" fill="url(#skyGrad)" />

        {/* sun */}
        <g className={active(0)}>
          <circle cx="70" cy="58" r="26" fill="#fbbf24" />
          {[0, 45, 90, 135, 180, 225, 270, 315].map((deg) => (
            <line
              key={deg}
              x1={70 + 30 * Math.cos((deg * Math.PI) / 180)}
              y1={58 + 30 * Math.sin((deg * Math.PI) / 180)}
              x2={70 + 40 * Math.cos((deg * Math.PI) / 180)}
              y2={58 + 40 * Math.sin((deg * Math.PI) / 180)}
              stroke="#f59e0b"
              strokeWidth="3"
              strokeLinecap="round"
            />
          ))}
          <text x="70" y="106" textAnchor="middle" className="viz-label">
            {pick(lang, "Sunlight", "ಸೂರ್ಯನ ಬೆಳಕು")}
          </text>
          <path
            d="M104 74 L214 128"
            stroke="#f59e0b"
            strokeWidth="2.5"
            strokeDasharray="7 5"
            markerEnd="url(#arrowAmber)"
          />
        </g>
        <defs>
          <marker id="arrowAmber" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#f59e0b" />
          </marker>
          <marker id="arrowTeal" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#0f766e" />
          </marker>
          <marker id="arrowBlue" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#2563eb" />
          </marker>
        </defs>

        {/* leaf */}
        <g className={active(3)}>
          <path
            d="M250 92 C336 84 402 128 404 186 C404 236 336 262 258 244 C222 236 196 206 196 172 C196 130 216 96 250 92 Z"
            fill="url(#leafGrad)"
            stroke="#0b5a54"
            strokeWidth="2"
          />
          <path d="M250 96 C252 150 256 206 262 244" stroke="#e7f6ec" strokeWidth="2.5" fill="none" />
          {[118, 146, 174, 202].map((y, index) => (
            <path
              key={y}
              d={`M252 ${y} C${292 - index * 4} ${y - 12} ${330 - index * 6} ${y - 16} ${352 - index * 8} ${y - 8}`}
              stroke="#d1fae5"
              strokeWidth="1.8"
              fill="none"
            />
          ))}
          <text x="300" y="290" textAnchor="middle" className="viz-label">
            {pick(lang, "Leaf with chlorophyll", "ಕ್ಲೋರೋಫಿಲ್ ಇರುವ ಎಲೆ")}
          </text>
        </g>

        {/* roots and water */}
        <g className={active(1)}>
          <path
            d="M232 300 C232 268 244 250 250 244"
            stroke="#2563eb"
            strokeWidth="3"
            fill="none"
            markerEnd="url(#arrowBlue)"
          />
          <ellipse cx="232" cy="312" rx="46" ry="10" fill="#dbeafe" stroke="#93c5fd" />
          <text x="120" y="316" className="viz-label">
            {pick(lang, "Water + minerals", "ನೀರು + ಖನಿಜಗಳು")}
          </text>
        </g>

        {/* CO2 in */}
        <g className={active(2)}>
          <path
            d="M470 150 L418 168"
            stroke="#0f766e"
            strokeWidth="2.5"
            markerEnd="url(#arrowTeal)"
          />
          <text x="440" y="138" textAnchor="middle" className="viz-label">
            CO₂
          </text>
        </g>

        {/* O2 and glucose out */}
        <g className={active(4)}>
          <path d="M410 100 L466 76" stroke="#0f766e" strokeWidth="2.5" markerEnd="url(#arrowTeal)" />
          <text x="472" y="64" textAnchor="middle" className="viz-label">
            O₂
          </text>
          <path d="M400 230 L462 250" stroke="#f59e0b" strokeWidth="2.5" markerEnd="url(#arrowAmber)" />
          <text x="466" y="272" textAnchor="middle" className="viz-label">
            {pick(lang, "Glucose", "ಗ್ಲೂಕೋಸ್")}
          </text>
        </g>
      </svg>

      <div className="viz-controls">
        <button
          type="button"
          className="btn btn-ghost btn-sm"
          onClick={() => setStep((s) => Math.max(0, s - 1))}
          disabled={step === 0}
        >
          ← {pick(lang, "Previous", "ಹಿಂದೆ")}
        </button>
        <span className="badge">
          {step + 1}/{PHOTO_STEPS.length}
        </span>
        <button
          type="button"
          className="btn btn-primary btn-sm"
          onClick={() => setStep((s) => Math.min(PHOTO_STEPS.length - 1, s + 1))}
          disabled={step === PHOTO_STEPS.length - 1}
        >
          {pick(lang, "Next step", "ಮುಂದಿನ ಹಂತ")} →
        </button>
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        {lang === "kn" ? PHOTO_STEPS[step].kn : PHOTO_STEPS[step].en}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ brain */

const BRAIN_REGIONS = [
  {
    id: "cerebrum",
    en: "Cerebrum",
    kn: "ಸೆರೆಬ್ರಮ್",
    fnEn: "Thinking, memory, language, and the senses. The large folded outer part.",
    fnKn: "ಯೋಚನೆ, ನೆನಪು, ಭಾಷೆ ಮತ್ತು ಇಂದ್ರಿಯಗಳು. ಇದು ಮೇಲ್ಭಾಗದ ದೊಡ್ಡ ಸುಕ್ಕುಗಟ್ಟಿದ ಭಾಗ.",
    color: "#f9a8d4",
  },
  {
    id: "cerebellum",
    en: "Cerebellum",
    kn: "ಸೆರೆಬೆಲ್ಲಮ್",
    fnEn: "Balance and smooth body movements, like cycling or writing.",
    fnKn: "ಸಮತೋಲನ ಮತ್ತು ನಯವಾದ ದೇಹ ಚಲನೆ — ಸೈಕಲ್ ತಳ್ಳುವುದು, ಬರೆಯುವುದು.",
    color: "#93c5fd",
  },
  {
    id: "brainstem",
    en: "Brainstem",
    kn: "ಬ್ರೇನ್‌ಸ್ಟೆಮ್",
    fnEn: "Controls breathing, heartbeat and blood pressure without you thinking about it.",
    fnKn: "ಉಸಿರಾಟ, ಹೃದಯ ಬಡಿತ ಮತ್ತು ರಕ್ತದೊತ್ತಡವನ್ನು ನೀವು ಯೋಚಿಸದೆಯೇ ನಿಯಂತ್ರಿಸುತ್ತದೆ.",
    color: "#fcd34d",
  },
];

function BrainDiagram({ lang }: DiagramProps) {
  const [selected, setSelected] = useState(BRAIN_REGIONS[0].id);
  const region = BRAIN_REGIONS.find((item) => item.id === selected) ?? BRAIN_REGIONS[0];

  return (
    <div className="viz">
      <svg viewBox="0 0 460 300" role="img" aria-label="Human brain regions" className="viz-svg">
        <ellipse cx="230" cy="150" rx="196" ry="128" fill="#fdf2f8" />
        {/* cerebrum */}
        <path
          d="M92 128 C96 66 168 40 236 44 C308 48 362 84 366 132 C368 164 344 184 308 190 C260 198 168 198 124 186 C96 178 90 156 92 128 Z"
          fill={selected === "cerebrum" ? "#ec4899" : "#f9a8d4"}
          stroke="#9d174d"
          strokeWidth="2"
          className="viz-clickable"
          onClick={() => setSelected("cerebrum")}
          role="button"
          tabIndex={0}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") setSelected("cerebrum");
          }}
        />
        {[130, 170, 210, 250, 290].map((x, index) => (
          <path
            key={x}
            d={`M${x} ${92 + (index % 2) * 8} q18 22 0 44`}
            stroke="#be185d"
            strokeWidth="1.6"
            fill="none"
            opacity="0.7"
            pointerEvents="none"
          />
        ))}
        {/* cerebellum */}
        <path
          d="M300 196 C336 190 362 202 366 224 C368 246 344 258 316 254 C292 250 280 232 284 212 C286 202 292 198 300 196 Z"
          fill={selected === "cerebellum" ? "#3b82f6" : "#93c5fd"}
          stroke="#1d4ed8"
          strokeWidth="2"
          className="viz-clickable"
          onClick={() => setSelected("cerebellum")}
          role="button"
          tabIndex={0}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") setSelected("cerebellum");
          }}
        />
        {[206, 216, 226, 236].map((y) => (
          <line
            key={y}
            x1="292"
            y1={y}
            x2="358"
            y2={y}
            stroke="#1e40af"
            strokeWidth="1.2"
            opacity="0.55"
            pointerEvents="none"
          />
        ))}
        {/* brainstem */}
        <path
          d="M214 192 C224 192 232 198 232 210 L232 252 C232 264 224 270 212 270 C200 270 194 262 194 252 L194 208 C194 198 202 192 214 192 Z"
          fill={selected === "brainstem" ? "#f59e0b" : "#fcd34d"}
          stroke="#b45309"
          strokeWidth="2"
          className="viz-clickable"
          onClick={() => setSelected("brainstem")}
          role="button"
          tabIndex={0}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") setSelected("brainstem");
          }}
        />
        <text x="228" y="26" textAnchor="middle" className="viz-label">
          {pick(lang, "Tap a region", "ಭಾಗವನ್ನು ಒತ್ತಿರಿ")}
        </text>
      </svg>

      <div className="viz-controls">
        {BRAIN_REGIONS.map((item) => (
          <button
            key={item.id}
            type="button"
            className={selected === item.id ? "chip chip-active" : "chip"}
            onClick={() => setSelected(item.id)}
            aria-pressed={selected === item.id}
          >
            {lang === "kn" ? item.kn : item.en}
          </button>
        ))}
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        <strong>{lang === "kn" ? region.kn : region.en}: </strong>
        {lang === "kn" ? region.fnKn : region.fnEn}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ microorganisms */

const MICROBES = [
  {
    id: "bacteria",
    en: "Bacteria",
    kn: "ಬ್ಯಾಕ್ಟೀರಿಯಾ",
    roleEn: "Single-celled. Some cause disease, many help us — curd and idli batter are made with them.",
    roleKn: "ಏಕಕೋಶ ಜೀವಿಗಳು. ಕೆಲವು ರೋಗ ಉಂಟುಮಾಡುತ್ತವೆ, ಅನೇಕ ಸಹಾಯ ಮಾಡುತ್ತವೆ — ಮೊಸರು ಮತ್ತು ಇಡ್ಲಿ ಹಿಟ್ಟು ಇವುಗಳಿಂದ ತಯಾರಾಗುತ್ತದೆ.",
  },
  {
    id: "fungi",
    en: "Fungi",
    kn: "ಶಿಲೀಂಧ್ರಗಳು",
    roleEn: "Yeast makes bread rise; mould spoils food. They feed on dead material.",
    roleKn: "ಯೀಸ್ಟ್ ಬ್ರೆಡ್ ಉಬ್ಬಿಸುತ್ತದೆ; ಬೂಷ್ಟು ಆಹಾರ ಹಾಳು ಮಾಡುತ್ತದೆ. ಇವು ಸತ್ತ ವಸ್ತುವಿನ ಮೇಲೆ ಬದುಕುತ್ತವೆ.",
  },
  {
    id: "protozoa",
    en: "Protozoa",
    kn: "ಪ್ರೊಟೊಜೋವಾ",
    roleEn: "Single-celled swimmers. Some live in pond water, some cause malaria.",
    roleKn: "ಏಕಕೋಶ ಈಜುವ ಜೀವಿಗಳು. ಕೆಲವು ಕೆರೆ ನೀರಿನಲ್ಲಿ ವಾಸಿಸುತ್ತವೆ, ಕೆಲವು ಮಲೇರಿಯಾ ಉಂಟುಮಾಡುತ್ತವೆ.",
  },
  {
    id: "algae",
    en: "Algae",
    kn: "ಆಲ್ಗೆ",
    roleEn: "Green and plant-like. Pond scum is algae; they release oxygen into water.",
    roleKn: "ಹಸಿರು, ಸಸ್ಯದಂತಹ ಜೀವಿಗಳು. ಕೆರೆಯ ಹಸಿರು ಪದರ ಆಲ್ಗೆ; ಅವು ನೀರಿಗೆ ಆಮ್ಲಜನಕ ಬಿಡುಗಡೆ ಮಾಡುತ್ತವೆ.",
  },
];

function MicroorganismsDiagram({ lang }: DiagramProps) {
  const [selected, setSelected] = useState(MICROBES[0].id);
  const microbe = MICROBES.find((item) => item.id === selected) ?? MICROBES[0];

  return (
    <div className="viz">
      <div className="microbe-grid">
        {MICROBES.map((item) => (
          <button
            key={item.id}
            type="button"
            className={selected === item.id ? "microbe-card active" : "microbe-card"}
            onClick={() => setSelected(item.id)}
            aria-pressed={selected === item.id}
          >
            <svg viewBox="0 0 100 70" aria-hidden="true">
              {item.id === "bacteria" ? (
                <g stroke="#0f766e" strokeWidth="3" fill="#d1fae5">
                  <ellipse cx="36" cy="34" rx="20" ry="12" />
                  <ellipse cx="68" cy="44" rx="14" ry="9" />
                  <line x1="16" y1="34" x2="4" y2="34" />
                  <line x1="82" y1="44" x2="96" y2="44" />
                </g>
              ) : null}
              {item.id === "fungi" ? (
                <g stroke="#b45309" strokeWidth="3" fill="#fef3c7">
                  <path d="M28 34 C28 18 58 18 58 34 Z" />
                  <line x1="43" y1="34" x2="43" y2="52" />
                  <path d="M62 44 C62 34 86 34 86 44 Z" />
                  <line x1="74" y1="44" x2="74" y2="56" />
                </g>
              ) : null}
              {item.id === "protozoa" ? (
                <g stroke="#2563eb" strokeWidth="3" fill="#dbeafe">
                  <ellipse cx="46" cy="36" rx="24" ry="14" />
                  <path d="M22 30 C12 22 8 30 14 38" fill="none" />
                  <path d="M70 30 C80 22 86 32 78 40" fill="none" />
                  <circle cx="56" cy="34" r="3" fill="#1e40af" />
                </g>
              ) : null}
              {item.id === "algae" ? (
                <g stroke="#15803d" strokeWidth="3" fill="#dcfce7">
                  <path d="M24 46 C32 22 44 22 50 40 C56 22 70 24 76 46 Z" />
                  <line x1="50" y1="40" x2="50" y2="58" />
                </g>
              ) : null}
            </svg>
            <span className={lang === "kn" ? "kan" : ""}>{lang === "kn" ? item.kn : item.en}</span>
          </button>
        ))}
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        <strong>{lang === "kn" ? microbe.kn : microbe.en}: </strong>
        {lang === "kn" ? microbe.roleKn : microbe.roleEn}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ circuit */

function CircuitDiagram({ lang }: DiagramProps) {
  const [on, setOn] = useState(false);

  return (
    <div className="viz">
      <svg viewBox="0 0 460 280" role="img" aria-label="Simple electric circuit" className="viz-svg">
        <rect x="0" y="0" width="460" height="280" rx="16" fill="#f8fafc" />
        <rect x="60" y="60" width="340" height="160" rx="18" fill="none" stroke="#94a3b8" strokeWidth="3" />
        {/* battery */}
        <g>
          <rect x="34" y="112" width="26" height="46" rx="4" fill="#0f172a" />
          <rect x="60" y="120" width="8" height="30" rx="2" fill="#f59e0b" />
          <text x="24" y="176" className="viz-label">
            {pick(lang, "Battery", "ಬ್ಯಾಟರಿ")}
          </text>
        </g>
        {/* switch */}
        <g
          className="viz-clickable"
          onClick={() => setOn((value) => !value)}
          role="button"
          tabIndex={0}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") setOn((value) => !value);
          }}
        >
          <circle cx="150" cy="60" r="7" fill="#334155" />
          <circle cx="230" cy="60" r="7" fill="#334155" />
          <line
            x1="150"
            y1="60"
            x2={on ? 228 : 216}
            y2={on ? 60 : 22}
            stroke={on ? "#16a34a" : "#b91c1c"}
            strokeWidth="6"
            strokeLinecap="round"
          />
          <text x="190" y="14" textAnchor="middle" className="viz-label">
            {on ? pick(lang, "Switch ON", "ಸ್ವಿಚ್ ಆನ್") : pick(lang, "Switch OFF", "ಸ್ವಿಚ್ ಆಫ್")}
          </text>
        </g>
        {/* bulb */}
        <g>
          <circle
            cx="370"
            cy="140"
            r="30"
            fill={on ? "#fde68a" : "#e2e8f0"}
            stroke={on ? "#f59e0b" : "#94a3b8"}
            strokeWidth="3"
          />
          {on ? (
            <>
              <circle cx="370" cy="140" r="44" fill="#fbbf24" opacity="0.25" className="viz-glow" />
              {[0, 60, 120, 180, 240, 300].map((deg) => (
                <line
                  key={deg}
                  x1={370 + 34 * Math.cos((deg * Math.PI) / 180)}
                  y1={140 + 34 * Math.sin((deg * Math.PI) / 180)}
                  x2={370 + 46 * Math.cos((deg * Math.PI) / 180)}
                  y2={140 + 46 * Math.sin((deg * Math.PI) / 180)}
                  stroke="#f59e0b"
                  strokeWidth="3"
                  strokeLinecap="round"
                />
              ))}
            </>
          ) : null}
          <path d="M358 128 q12 16 24 0" stroke="#475569" strokeWidth="2" fill="none" />
          <text x="370" y="196" textAnchor="middle" className="viz-label">
            {pick(lang, "Bulb", "ಬಲ್ಬ್")}
          </text>
        </g>
        {/* current */}
        {on ? (
          <g className="viz-flow">
            <circle r="5" fill="#f59e0b">
              <animateMotion dur="2.4s" repeatCount="indefinite" path="M60 60 H400 V220 H60 Z" />
            </circle>
            <circle r="5" fill="#f59e0b">
              <animateMotion dur="2.4s" begin="1.2s" repeatCount="indefinite" path="M60 60 H400 V220 H60 Z" />
            </circle>
          </g>
        ) : null}
      </svg>
      <div className="viz-controls">
        <button
          type="button"
          className={on ? "btn btn-ghost btn-sm" : "btn btn-primary btn-sm"}
          onClick={() => setOn((value) => !value)}
        >
          {on ? pick(lang, "Switch off", "ಆಫ್ ಮಾಡಿ") : pick(lang, "Switch on", "ಆನ್ ಮಾಡಿ")}
        </button>
        <span className={on ? "badge badge-ok" : "badge"}>
          {on ? pick(lang, "Circuit complete", "ಮಂಡಲ ಪೂರ್ಣ") : pick(lang, "Circuit open", "ಮಂಡಲ ತೆರೆದಿದೆ")}
        </span>
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        {on
          ? lang === "kn"
            ? "ಸ್ವಿಚ್ ಮುಚ್ಚಿದಾಗ ಮಂಡಲ ಪೂರ್ಣವಾಗುತ್ತದೆ. ವಿದ್ಯುತ್ ಹರಿಯುತ್ತದೆ ಮತ್ತು ಬಲ್ಬ್ ಬೆಳಗುತ್ತದೆ."
            : "With the switch closed the circuit is complete: current flows and the bulb lights up."
          : lang === "kn"
            ? "ಸ್ವಿಚ್ ತೆರೆದಿದ್ದಾಗ ಮಂಡಲ ಅಪೂರ್ಣ. ವಿದ್ಯುತ್ ಹರಿಯಲು ದಾರಿ ಇಲ್ಲ, ಬಲ್ಬ್ ಬೆಳಗುವುದಿಲ್ಲ."
            : "With the switch open the circuit is broken. There is no path for current, so the bulb stays dark."}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ forces */

const FORCES = [
  {
    id: "push",
    en: "Push",
    kn: "ತಳ್ಳುವ ಬಲ",
    textEn: "You push a door, a cycle pedal or a shopping trolley away from you.",
    textKn: "ನೀವು ಬಾಗಿಲು, ಸೈಕಲ್ ಪೆಡಲ್ ಅಥವಾ ಟ್ರಾಲಿಯನ್ನು ನಿಮ್ಮಿಂದ ದೂರ ತಳ್ಳುತ್ತೀರಿ.",
  },
  {
    id: "pull",
    en: "Pull",
    kn: "ಎಳೆಯುವ ಬಲ",
    textEn: "You pull a bucket from a well or pull a rope in tug-of-war.",
    textKn: "ಬಾವಿಯಿಂದ ಬಕೆಟ್ ಎಳೆಯುತ್ತೀರಿ, ಅಥವಾ ಹಗ್ಗ ಎಳೆಯುವ ಆಟದಲ್ಲಿ ಹಗ್ಗ ಎಳೆಯುತ್ತೀರಿ.",
  },
  {
    id: "friction",
    en: "Friction",
    kn: "ಘರ್ಷಣೆ",
    textEn: "Rubbing acts against motion — that is why a ball slows down on the ground.",
    textKn: "ಉಜ್ಜುವಿಕೆ ಚಲನೆಗೆ ವಿರುದ್ಧವಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ — ಆದ್ದರಿಂದ ಚೆಂಡು ನೆಲದಲ್ಲಿ ನಿಧಾನವಾಗುತ್ತದೆ.",
  },
  {
    id: "gravity",
    en: "Gravity",
    kn: "ಗುರುತ್ವ",
    textEn: "Earth pulls every object towards its centre — a dropped book falls down.",
    textKn: "ಭೂಮಿ ಪ್ರತಿ ವಸ್ತುವನ್ನು ತನ್ನ ಕೇಂದ್ರದ ಕಡೆ ಎಳೆಯುತ್ತದೆ — ಬಿಟ್ಟ ಪುಸ್ತಕ ಕೆಳಗೆ ಬೀಳುತ್ತದೆ.",
  },
];

function ForcesDiagram({ lang }: DiagramProps) {
  const [active, setActive] = useState(FORCES[0].id);
  const force = FORCES.find((item) => item.id === active) ?? FORCES[0];

  return (
    <div className="viz">
      <svg viewBox="0 0 460 220" role="img" aria-label="Forces in everyday life" className="viz-svg">
        <rect x="0" y="0" width="460" height="220" rx="16" fill="#f8fafc" />
        <line x1="0" y1="176" x2="460" y2="176" stroke="#cbd5e1" strokeWidth="4" />

        {active === "push" ? (
          <g className="viz-arrow">
            <rect x="200" y="118" width="80" height="56" rx="8" fill="#bfdbfe" stroke="#1d4ed8" strokeWidth="2" />
            <text x="240" y="152" textAnchor="middle" className="viz-label">
              {pick(lang, "Box", "ಪೆಟ್ಟಿಗೆ")}
            </text>
            <line x1="90" y1="146" x2="186" y2="146" stroke="#b91c1c" strokeWidth="5" markerEnd="url(#arrowRed)" />
            <text x="130" y="132" textAnchor="middle" className="viz-label">
              {pick(lang, "Push", "ತಳ್ಳು")}
            </text>
          </g>
        ) : null}

        {active === "pull" ? (
          <g className="viz-arrow">
            <rect x="230" y="118" width="80" height="56" rx="8" fill="#fde68a" stroke="#b45309" strokeWidth="2" />
            <line x1="230" y1="146" x2="120" y2="146" stroke="#b91c1c" strokeWidth="5" markerEnd="url(#arrowRed)" />
            <text x="180" y="132" textAnchor="middle" className="viz-label">
              {pick(lang, "Pull", "ಎಳೆ")}
            </text>
          </g>
        ) : null}

        {active === "friction" ? (
          <g>
            <circle cx="150" cy="150" r="26" fill="#a7f3d0" stroke="#047857" strokeWidth="2" className="viz-roll" />
            <line x1="150" y1="184" x2="220" y2="184" stroke="#b91c1c" strokeWidth="4" markerEnd="url(#arrowRed)" />
            <text x="186" y="206" textAnchor="middle" className="viz-label">
              {pick(lang, "Friction opposes motion", "ಘರ್ಷಣೆ ಚಲನೆಗೆ ವಿರುದ್ಧ")}
            </text>
          </g>
        ) : null}

        {active === "gravity" ? (
          <g>
            <rect x="196" y="26" width="52" height="40" rx="6" fill="#fecaca" stroke="#b91c1c" strokeWidth="2" />
            <line x1="222" y1="74" x2="222" y2="164" stroke="#b91c1c" strokeWidth="5" markerEnd="url(#arrowRed)" />
            <text x="286" y="120" className="viz-label">
              {pick(lang, "Earth pulls down", "ಭೂಮಿ ಕೆಳಗೆ ಎಳೆಯುತ್ತದೆ")}
            </text>
          </g>
        ) : null}

        <defs>
          <marker id="arrowRed" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
            <path d="M0,0 L0,6 L8,3 z" fill="#b91c1c" />
          </marker>
        </defs>
      </svg>

      <div className="viz-controls">
        {FORCES.map((item) => (
          <button
            key={item.id}
            type="button"
            className={active === item.id ? "chip chip-active" : "chip"}
            onClick={() => setActive(item.id)}
            aria-pressed={active === item.id}
          >
            {lang === "kn" ? item.kn : item.en}
          </button>
        ))}
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        {lang === "kn" ? force.textKn : force.textEn}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ matter */

const STATES = [
  {
    id: "solid",
    en: "Solid",
    kn: "ಘನ",
    textEn: "Particles are packed tightly and only vibrate in place, so a solid keeps its shape.",
    textKn: "ಕಣಗಳು ಹತ್ತಿರ ಹತ್ತಿರ ಇರುತ್ತವೆ ಮತ್ತು ಸ್ಥಳದಲ್ಲೇ ಕಂಪಿಸುತ್ತವೆ, ಆದ್ದರಿಂದ ಘನ ತನ್ನ ಆಕಾರ ಉಳಿಸಿಕೊಳ್ಳುತ್ತದೆ.",
  },
  {
    id: "liquid",
    en: "Liquid",
    kn: "ದ್ರವ",
    textEn: "Particles are close but can slide past each other, so a liquid flows and takes the shape of its container.",
    textKn: "ಕಣಗಳು ಹತ್ತಿರ ಇದ್ದರೂ ಜಾರಿಕೊಳ್ಳಬಹುದು, ಆದ್ದರಿಂದ ದ್ರವ ಹರಿಯುತ್ತದೆ ಮತ್ತು ಪಾತ್ರೆಯ ಆಕಾರ ಪಡೆಯುತ್ತದೆ.",
  },
  {
    id: "gas",
    en: "Gas",
    kn: "ಅನಿಲ",
    textEn: "Particles are far apart and move fast in all directions, so a gas fills any container.",
    textKn: "ಕಣಗಳು ದೂರ ದೂರ ಇರುತ್ತವೆ ಮತ್ತು ಎಲ್ಲಾ ದಿಕ್ಕುಗಳಲ್ಲಿ ವೇಗವಾಗಿ ಚಲಿಸುತ್ತವೆ, ಆದ್ದರಿಂದ ಅನಿಲ ಪಾತ್ರೆಯನ್ನು ತುಂಬುತ್ತದೆ.",
  },
];

function MatterDiagram({ lang }: DiagramProps) {
  const [state, setState] = useState(STATES[0].id);
  const current = STATES.find((item) => item.id === state) ?? STATES[0];

  const particles = useMemo(() => {
    const count = state === "gas" ? 14 : state === "liquid" ? 20 : 24;
    return Array.from({ length: count }, (_, index) => {
      const row = Math.floor(index / 6);
      const col = index % 6;
      if (state === "solid") {
        return { x: 96 + col * 26, y: 92 + row * 26, r: 7, delay: index * 0.12 };
      }
      if (state === "liquid") {
        return {
          x: 88 + col * 27 + (row % 2 ? 8 : 0),
          y: 150 + row * 22,
          r: 8,
          delay: index * 0.16,
        };
      }
      return {
        x: 60 + ((index * 67) % 300),
        y: 60 + ((index * 53) % 130),
        r: 7,
        delay: index * 0.21,
      };
    });
  }, [state]);

  return (
    <div className="viz">
      <svg viewBox="0 0 420 240" role="img" aria-label="Particle arrangement" className="viz-svg">
        <rect x="0" y="0" width="420" height="240" rx="16" fill="#f8fafc" />
        <rect x="40" y="40" width="340" height="170" rx="12" fill="#eef4f1" stroke="#cbd5e1" strokeWidth="2" />
        {particles.map((particle, index) => (
          <circle
            key={index}
            cx={particle.x}
            cy={particle.y}
            r={particle.r}
            fill={state === "gas" ? "#f59e0b" : state === "liquid" ? "#2563eb" : "#0f766e"}
            className={state === "solid" ? "viz-vibrate" : "viz-drift"}
            style={{ animationDelay: `${particle.delay}s` }}
          />
        ))}
      </svg>

      <div className="viz-controls">
        {STATES.map((item) => (
          <button
            key={item.id}
            type="button"
            className={state === item.id ? "chip chip-active" : "chip"}
            onClick={() => setState(item.id)}
            aria-pressed={state === item.id}
          >
            {lang === "kn" ? item.kn : item.en}
          </button>
        ))}
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        {lang === "kn" ? current.textKn : current.textEn}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ light */

function LightDiagram({ lang }: DiagramProps) {
  const [angle, setAngle] = useState(35);
  const radians = (angle * Math.PI) / 180;
  const mirrorX = 300;
  const originY = 130;
  const length = 120;
  const incident = {
    x1: mirrorX - length * Math.sin(radians),
    y1: originY - length * Math.cos(radians),
  };
  const reflected = {
    x2: mirrorX + length * Math.sin(radians),
    y2: originY - length * Math.cos(radians),
  };

  return (
    <div className="viz">
      <svg viewBox="0 0 520 250" role="img" aria-label="Reflection from a plane mirror" className="viz-svg">
        <rect x="0" y="0" width="520" height="250" rx="16" fill="#f8fafc" />
        {/* mirror */}
        <rect x={mirrorX - 6} y="40" width="12" height="170" rx="4" fill="#93c5fd" stroke="#1d4ed8" strokeWidth="2" />
        {Array.from({ length: 10 }, (_, index) => (
          <line
            key={index}
            x1={mirrorX + 6}
            y1={48 + index * 17}
            x2={mirrorX + 16}
            y2={40 + index * 17}
            stroke="#1d4ed8"
            strokeWidth="1.4"
            opacity="0.6"
          />
        ))}
        {/* normal */}
        <line
          x1={mirrorX - 90}
          y1={originY}
          x2={mirrorX + 90}
          y2={originY}
          stroke="#64748b"
          strokeWidth="1.6"
          strokeDasharray="6 5"
        />
        <text x={mirrorX + 96} y={originY - 6} className="viz-label">
          {pick(lang, "Normal", "ಲಂಬರೇಖೆ")}
        </text>
        {/* rays */}
        <line
          x1={incident.x1}
          y1={incident.y1}
          x2={mirrorX}
          y2={originY}
          stroke="#dc2626"
          strokeWidth="3"
          markerEnd="url(#arrowRed2)"
        />
        <line
          x1={mirrorX}
          y1={originY}
          x2={reflected.x2}
          y2={reflected.y2}
          stroke="#0f766e"
          strokeWidth="3"
          markerEnd="url(#arrowTeal2)"
        />
        <text x={incident.x1 - 6} y={incident.y1 - 8} className="viz-label">
          {pick(lang, "Incident ray", "ಪತನ ಕಿರಣ")}
        </text>
        <text x={reflected.x2 - 40} y={reflected.y2 - 8} className="viz-label">
          {pick(lang, "Reflected ray", "ಪ್ರತಿಫಲಿತ ಕಿರಣ")}
        </text>
        <text x={mirrorX + 20} y={52} className="viz-label">
          {pick(lang, "Mirror", "ಕನ್ನಡಿ")}
        </text>
        <text x={mirrorX - 46} y={originY - 12} className="viz-label">
          {angle}°
        </text>
        <text x={mirrorX + 16} y={originY - 12} className="viz-label">
          {angle}°
        </text>
        <defs>
          <marker id="arrowRed2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#dc2626" />
          </marker>
          <marker id="arrowTeal2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#0f766e" />
          </marker>
        </defs>
      </svg>

      <div className="viz-controls">
        <label className="inline-field">
          <span className="label" style={{ marginBottom: 0 }}>
            {pick(lang, "Angle of incidence", "ಪತನ ಕೋನ")}
          </span>
          <input
            type="range"
            min={10}
            max={65}
            value={angle}
            onChange={(event) => setAngle(Number(event.target.value))}
            aria-label="Angle of incidence"
          />
        </label>
        <span className="badge">
          {angle}° = {angle}°
        </span>
      </div>
      <p className={lang === "kn" ? "viz-step kan" : "viz-step"} lang={lang}>
        {lang === "kn"
          ? `ಪತನ ಕೋನ ${angle}° ಮತ್ತು ಪ್ರತಿಫಲನ ಕೋನ ${angle}° — ಎರಡೂ ಸಮವಾಗಿರುತ್ತವೆ.`
          : `Angle of incidence ${angle}° equals angle of reflection ${angle}° — that is the law of reflection.`}
      </p>
    </div>
  );
}

/* ------------------------------------------------------------------ registry */

export interface VisualizationEntry {
  key: string;
  title_en: string;
  title_kn: string;
  caption_en: string;
  caption_kn: string;
  Component: (props: DiagramProps) => ReactElement;
}

export const VISUALIZATIONS: Record<string, VisualizationEntry> = {
  photosynthesis: {
    key: "photosynthesis",
    title_en: "Photosynthesis step by step",
    title_kn: "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಹಂತ ಹಂತವಾಗಿ",
    caption_en: "How a leaf turns sunlight, water and air into food.",
    caption_kn: "ಎಲೆ ಸೂರ್ಯನ ಬೆಳಕು, ನೀರು ಮತ್ತು ಗಾಳಿಯನ್ನು ಆಹಾರವಾಗಿ ಹೇಗೆ ಬದಲಿಸುತ್ತದೆ.",
    Component: PhotosynthesisDiagram,
  },
  brain: {
    key: "brain",
    title_en: "Regions of the human brain",
    title_kn: "ಮಾನವ ಮೆದುಳಿನ ಭಾಗಗಳು",
    caption_en: "Tap a region to see what it does.",
    caption_kn: "ಭಾಗ ಏನು ಮಾಡುತ್ತದೆ ಎಂದು ನೋಡಲು ಒತ್ತಿರಿ.",
    Component: BrainDiagram,
  },
  microorganisms: {
    key: "microorganisms",
    title_en: "Types of microorganisms",
    title_kn: "ಸೂಕ್ಷ್ಮಜೀವಿಗಳ ವಿಧಗಳು",
    caption_en: "Bacteria, fungi, protozoa and algae — the life you cannot see.",
    caption_kn: "ಬ್ಯಾಕ್ಟೀರಿಯಾ, ಶಿಲೀಂಧ್ರ, ಪ್ರೊಟೊಜೋವಾ ಮತ್ತು ಆಲ್ಗೆ — ಕಾಣದ ಜೀವಿಗಳು.",
    Component: MicroorganismsDiagram,
  },
  electricity: {
    key: "electricity",
    title_en: "A simple electric circuit",
    title_kn: "ಸರಳ ವಿದ್ಯುತ್ ಮಂಡಲ",
    caption_en: "Switch the circuit on and watch the current complete the loop.",
    caption_kn: "ಮಂಡಲವನ್ನು ಆನ್ ಮಾಡಿ, ವಿದ್ಯುತ್ ಹೇಗೆ ಸುತ್ತು ಬರುತ್ತದೆ ಎಂದು ನೋಡಿ.",
    Component: CircuitDiagram,
  },
  forces: {
    key: "forces",
    title_en: "Push, pull, friction and gravity",
    title_kn: "ತಳ್ಳು, ಎಳೆ, ಘರ್ಷಣೆ ಮತ್ತು ಗುರುತ್ವ",
    caption_en: "Everyday examples of the forces around you.",
    caption_kn: "ನಿಮ್ಮ ಸುತ್ತಲಿನ ಬಲಗಳ ದೈನಂದಿನ ಉದಾಹರಣೆಗಳು.",
    Component: ForcesDiagram,
  },
  matter: {
    key: "matter",
    title_en: "Particles in solids, liquids and gases",
    title_kn: "ಘನ, ದ್ರವ ಮತ್ತು ಅನಿಲದಲ್ಲಿನ ಕಣಗಳು",
    caption_en: "Compare how tightly particles are packed and how they move.",
    caption_kn: "ಕಣಗಳು ಎಷ್ಟು ಹತ್ತಿರ ಇವೆ ಮತ್ತು ಹೇಗೆ ಚಲಿಸುತ್ತವೆ ಎಂದು ಹೋಲಿಸಿ.",
    Component: MatterDiagram,
  },
  light: {
    key: "light",
    title_en: "Reflection from a plane mirror",
    title_kn: "ಸಮತಲ ಕನ್ನಡಿಯಿಂದ ಪ್ರತಿಫಲನ",
    caption_en: "Change the angle and see the law of reflection hold.",
    caption_kn: "ಕೋನ ಬದಲಿಸಿ, ಪ್ರತಿಫಲನ ನಿಯಮ ಸರಿಯಾಗಿದೆ ಎಂದು ನೋಡಿ.",
    Component: LightDiagram,
  },
};

export function Visualization({ vizKey }: { vizKey: string }) {
  const { lang } = useLanguage();
  const entry = VISUALIZATIONS[vizKey];
  if (!entry) return null;
  const { Component } = entry;

  return (
    <section className="viz-card">
      <div className="viz-head">
        <h3 className={lang === "kn" ? "kan" : ""}>{pick(lang, entry.title_en, entry.title_kn)}</h3>
        <span className="badge badge-soft">{pick(lang, "Interactive", "ಸಂವಾದಾತ್ಮಕ")}</span>
      </div>
      <Component lang={lang} />
      <p className={lang === "kn" ? "viz-caption kan" : "viz-caption"} lang={lang}>
        {pick(lang, entry.caption_en, entry.caption_kn)}
      </p>
    </section>
  );
}
