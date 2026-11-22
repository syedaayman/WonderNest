/**
 * Original inline SVG artwork for the WonderNest learning experience.
 *
 * Everything here is hand-built SVG so it stays crisp at any size, inherits the theme
 * colours and costs no extra network request. Motion is applied by CSS classes defined in
 * styles.css and disabled for students who prefer reduced motion.
 */

export function HeroScene({ label }: { label: string }) {
  return (
    <svg className="hero-scene" viewBox="0 0 460 360" role="img" aria-label={label}>
      <defs>
        <linearGradient id="wnHeroBg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#e7f7ef" />
          <stop offset="55%" stopColor="#eef2fd" />
          <stop offset="100%" stopColor="#f8effb" />
        </linearGradient>
        <linearGradient id="wnLiquid" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#8fe0cb" />
          <stop offset="100%" stopColor="#35a98e" />
        </linearGradient>
        <linearGradient id="wnTube" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#cdbdf7" />
          <stop offset="100%" stopColor="#9d86e8" />
        </linearGradient>
      </defs>

      <rect x="18" y="18" width="424" height="324" rx="42" fill="url(#wnHeroBg)" />
      <circle cx="374" cy="84" r="40" fill="#fff6dd" opacity="0.85" />
      <ellipse cx="104" cy="294" rx="74" ry="26" fill="#dceafc" opacity="0.7" />

      {/* floating atom */}
      <g className="wn-float-slow" transform="translate(98 94)">
        <ellipse rx="46" ry="17" fill="none" stroke="#3fb59b" strokeWidth="2.4" opacity="0.7" />
        <ellipse
          rx="46"
          ry="17"
          fill="none"
          stroke="#7c6bd6"
          strokeWidth="2.4"
          opacity="0.5"
          transform="rotate(60)"
        />
        <ellipse
          rx="46"
          ry="17"
          fill="none"
          stroke="#4d94e0"
          strokeWidth="2.4"
          opacity="0.45"
          transform="rotate(-60)"
        />
        <circle r="8" fill="#0f766e" />
        <circle cx="46" r="3.4" fill="#ff9b7a" />
      </g>

      {/* floating molecule */}
      <g className="wn-float" transform="translate(352 116)">
        <line x1="0" y1="0" x2="26" y2="16" stroke="#9d86e8" strokeWidth="3" strokeLinecap="round" />
        <line x1="0" y1="0" x2="-24" y2="20" stroke="#9d86e8" strokeWidth="3" strokeLinecap="round" />
        <line x1="-24" y1="20" x2="-14" y2="42" stroke="#7fd1c0" strokeWidth="3" strokeLinecap="round" />
        <circle r="10" fill="#9d86e8" />
        <circle cx="26" cy="16" r="7" fill="#7fd1c0" />
        <circle cx="-24" cy="20" r="7" fill="#8bbcf0" />
        <circle cx="-14" cy="42" r="6" fill="#ffc078" />
      </g>

      {/* bench */}
      <rect x="64" y="266" width="332" height="13" rx="6.5" fill="#e6ddcd" />
      <rect x="98" y="279" width="10" height="32" rx="5" fill="#efe7d9" />
      <rect x="352" y="279" width="10" height="32" rx="5" fill="#efe7d9" />

      {/* conical flask with bubbling liquid */}
      <g>
        <rect x="158" y="142" width="16" height="10" rx="4" fill="#e7f7ef" stroke="#0f766e" strokeWidth="3" />
        <rect x="152" y="150" width="28" height="30" rx="6" fill="#ffffff" stroke="#0f766e" strokeWidth="3" />
        <path
          d="M153 178 L132 234 Q126 252 146 252 L186 252 Q206 252 200 234 L179 178 Z"
          fill="#ffffff"
          stroke="#0f766e"
          strokeWidth="3"
          strokeLinejoin="round"
        />
        <path
          d="M141 218 L132 234 Q126 252 146 252 L186 252 Q206 252 200 234 L191 218 Z"
          fill="url(#wnLiquid)"
        />
        <circle className="wn-bubble" cx="158" cy="240" r="4.5" fill="#ffffff" opacity="0.85" />
        <circle
          className="wn-bubble wn-bubble-2"
          cx="176"
          cy="236"
          r="3.4"
          fill="#ffffff"
          opacity="0.85"
        />
        <circle
          className="wn-bubble wn-bubble-3"
          cx="167"
          cy="244"
          r="2.6"
          fill="#ffffff"
          opacity="0.85"
        />
      </g>

      {/* test tube */}
      <g transform="translate(272 192)">
        <rect x="0" y="0" width="20" height="70" rx="10" fill="#ffffff" stroke="#7c6bd6" strokeWidth="3" />
        <rect x="3" y="36" width="14" height="30" rx="7" fill="url(#wnTube)" />
      </g>

      {/* beaker */}
      <g transform="translate(306 212)">
        <path
          d="M0 0 h34 v32 a10 10 0 0 1 -10 10 h-14 a10 10 0 0 1 -10 -10 Z"
          fill="#ffffff"
          stroke="#4d94e0"
          strokeWidth="3"
          strokeLinejoin="round"
        />
        <path d="M1 18 h32 v14 a10 10 0 0 1 -10 10 h-12 a10 10 0 0 1 -10 -10 Z" fill="#bfe0fb" />
      </g>

      {/* plant on the bench */}
      <g transform="translate(88 200)">
        <path d="M18 62 V32" stroke="#3f9d6a" strokeWidth="4" strokeLinecap="round" />
        <path d="M18 40 C2 38 0 24 2 16 C14 16 20 26 18 40 Z" fill="#8fd6a8" />
        <path d="M18 48 C34 46 38 32 36 24 C24 24 18 34 18 48 Z" fill="#5fbd85" />
        <path d="M4 62 h28 l-4 22 a8 8 0 0 1 -8 6 h-4 a8 8 0 0 1 -8 -6 Z" fill="#ffb59a" />
      </g>

      {/* sparkles and floating dots */}
      <g className="wn-float" fill="#ffc078">
        <path d="M320 54 l4 10 10 4 -10 4 -4 10 -4 -10 -10 -4 10 -4 Z" />
      </g>
      <g className="wn-float-slow" fill="#7fd1c0">
        <path d="M62 172 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3 Z" />
      </g>
      <circle className="wn-float" cx="404" cy="208" r="5" fill="#ffb59a" />
      <circle className="wn-float-slow" cx="142" cy="112" r="4" fill="#8bbcf0" />
    </svg>
  );
}

export function Mascot({
  label,
  className = "companion-mascot",
}: {
  label: string;
  className?: string;
}) {
  return (
    <svg className={className} viewBox="0 0 120 132" role="img" aria-label={label}>
      <defs>
        <linearGradient id="wnMascotBody" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#d9f2e6" />
          <stop offset="100%" stopColor="#a8e3cd" />
        </linearGradient>
      </defs>
      <line x1="60" y1="30" x2="60" y2="18" stroke="#0f766e" strokeWidth="3" strokeLinecap="round" />
      <circle cx="60" cy="13" r="6.5" fill="#7c6bd6" />
      <circle cx="60" cy="13" r="2.6" fill="#ffffff" opacity="0.9" />
      <rect
        x="16"
        y="30"
        width="88"
        height="78"
        rx="34"
        fill="url(#wnMascotBody)"
        stroke="#0f766e"
        strokeWidth="3"
      />
      <ellipse cx="60" cy="64" rx="33" ry="27" fill="#ffffff" opacity="0.92" />
      <g className="mascot-eye">
        <circle cx="48" cy="62" r="6.2" fill="#0b2b26" />
        <circle cx="72" cy="62" r="6.2" fill="#0b2b26" />
        <circle cx="50" cy="59.5" r="2" fill="#ffffff" />
        <circle cx="74" cy="59.5" r="2" fill="#ffffff" />
      </g>
      <path
        d="M50 74 Q60 83 70 74"
        fill="none"
        stroke="#0b2b26"
        strokeWidth="3"
        strokeLinecap="round"
      />
      <circle cx="37" cy="72" r="5" fill="#ffb59a" opacity="0.75" />
      <circle cx="83" cy="72" r="5" fill="#ffb59a" opacity="0.75" />
      <path
        className="mascot-arm"
        d="M18 74 q-11 4 -8 15"
        fill="none"
        stroke="#0f766e"
        strokeWidth="6"
        strokeLinecap="round"
      />
      <path
        d="M102 74 q11 4 8 15"
        fill="none"
        stroke="#0f766e"
        strokeWidth="6"
        strokeLinecap="round"
      />
      <circle cx="60" cy="97" r="6" fill="#ffd166" stroke="#0f766e" strokeWidth="2" />
      <rect x="34" y="108" width="20" height="9" rx="4.5" fill="#0f766e" opacity="0.85" />
      <rect x="66" y="108" width="20" height="9" rx="4.5" fill="#0f766e" opacity="0.85" />
    </svg>
  );
}

export function SubjectArt({
  kind,
  label,
}: {
  kind: "biology" | "physics" | "chemistry";
  label: string;
}) {
  if (kind === "biology") {
    return (
      <svg className="subject-art-svg" viewBox="0 0 200 120" role="img" aria-label={label}>
        <circle cx="62" cy="60" r="34" fill="#ffffff" stroke="#3f9d6a" strokeWidth="3" />
        <circle cx="62" cy="60" r="13" fill="#a8e3cd" stroke="#3f9d6a" strokeWidth="2.5" />
        <circle cx="62" cy="60" r="4.5" fill="#3f9d6a" />
        <ellipse cx="44" cy="46" rx="8" ry="4.5" fill="#5fbd85" transform="rotate(-25 44 46)" />
        <ellipse cx="80" cy="74" rx="8" ry="4.5" fill="#5fbd85" transform="rotate(-25 80 74)" />
        <ellipse cx="82" cy="44" rx="6" ry="3.5" fill="#8fd6a8" transform="rotate(20 82 44)" />
        <path
          d="M132 96 C110 76 118 44 154 28 C170 56 160 86 132 96 Z"
          fill="#8fd6a8"
          stroke="#3f9d6a"
          strokeWidth="3"
          strokeLinejoin="round"
        />
        <path d="M136 92 C144 72 150 56 156 40" fill="none" stroke="#3f9d6a" strokeWidth="2.5" strokeLinecap="round" />
        <circle cx="176" cy="62" r="4" fill="#ffc078" />
        <circle cx="22" cy="88" r="3.5" fill="#7fd1c0" />
      </svg>
    );
  }

  if (kind === "physics") {
    return (
      <svg className="subject-art-svg" viewBox="0 0 200 120" role="img" aria-label={label}>
        <circle cx="66" cy="50" r="24" fill="#ffffff" stroke="#4d94e0" strokeWidth="3" />
        <path
          d="M58 44 q4 8 8 0 q4 -8 8 0"
          fill="none"
          stroke="#ff9b7a"
          strokeWidth="2.6"
          strokeLinecap="round"
        />
        <path d="M60 74 h12 v8 h-12 Z" fill="#bfe0fb" stroke="#4d94e0" strokeWidth="2.5" />
        <line x1="66" y1="82" x2="66" y2="90" stroke="#4d94e0" strokeWidth="3" strokeLinecap="round" />
        <line x1="66" y1="18" x2="66" y2="8" stroke="#ffd166" strokeWidth="3" strokeLinecap="round" />
        <line x1="34" y1="34" x2="27" y2="27" stroke="#ffd166" strokeWidth="3" strokeLinecap="round" />
        <line x1="98" y1="34" x2="105" y2="27" stroke="#ffd166" strokeWidth="3" strokeLinecap="round" />
        <line x1="100" y1="50" x2="112" y2="50" stroke="#ffd166" strokeWidth="3" strokeLinecap="round" />
        <path d="M120 84 h34 a10 10 0 0 1 0 20 h-34" fill="none" stroke="#7c6bd6" strokeWidth="3" strokeLinecap="round" />
        <path d="M126 66 h24 a12 12 0 0 1 12 12" fill="none" stroke="#7fd1c0" strokeWidth="3" strokeLinecap="round" />
        <path d="M156 36 l10 14 h-7 v10 h-6 v-10 h-7 Z" fill="#ffd166" stroke="#e0a800" strokeWidth="1.5" />
        <circle cx="132" cy="96" r="3.5" fill="#ff9b7a" />
      </svg>
    );
  }

  return (
    <svg className="subject-art-svg" viewBox="0 0 200 120" role="img" aria-label={label}>
      <path
        d="M62 30 h18 v18 l16 32 q4 10 -7 10 h-52 q-11 0 -7 -10 l16 -32 Z"
        fill="#ffffff"
        stroke="#7c6bd6"
        strokeWidth="3"
        strokeLinejoin="round"
      />
      <path d="M44 76 l-7 14 q-4 10 7 10 h52 q11 0 7 -10 l-7 -14 Z" fill="#cdbdf7" />
      <circle cx="52" cy="88" r="4" fill="#ffffff" opacity="0.9" />
      <circle cx="70" cy="84" r="3" fill="#ffffff" opacity="0.9" />
      <circle cx="60" cy="92" r="2.4" fill="#ffffff" opacity="0.9" />
      <g transform="translate(140 44)">
        <line x1="0" y1="0" x2="20" y2="12" stroke="#9d86e8" strokeWidth="3" strokeLinecap="round" />
        <line x1="0" y1="0" x2="-16" y2="16" stroke="#9d86e8" strokeWidth="3" strokeLinecap="round" />
        <circle r="8" fill="#9d86e8" />
        <circle cx="20" cy="12" r="6" fill="#7fd1c0" />
        <circle cx="-16" cy="16" r="6" fill="#ffc078" />
      </g>
      <circle cx="150" cy="94" r="5" fill="#7fd1c0" />
      <circle cx="172" cy="70" r="3.5" fill="#ff9b7a" />
      <circle cx="118" cy="98" r="3" fill="#8bbcf0" />
    </svg>
  );
}
