from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


st.set_page_config(
    page_title="LoadedBites GLA",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Page styling ---
show_html(
    """
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Syne:wght@500;600;700;800&family=Manrope:wght@400;500;600;700&display=swap");

      :root {
        --ft-serif: "Instrument Serif", Georgia, serif;
        --ft-display: "Syne", sans-serif;
        --ft-sans: "Manrope", sans-serif;
        --ft-ink: #1c140e;
        --ft-muted: #6b5748;
        --ft-line: rgba(28, 20, 14, 0.12);
        --ft-paper: #fbf3e4;
        --ft-orange: #e86a17;
        --ft-yellow: #f0b429;
        --ft-amber: #ff9f1c;
      }

      html, body, .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"],
      [data-testid="stCaption"], [data-testid="stAlert"],
      div[data-testid="stButton"] button, .stLinkButton a {
        font-family: var(--ft-sans) !important;
      }

      html, body, .stApp {
        font-size: 17px;
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
        color: var(--ft-ink);
      }

      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stHeader"],
      section.main {
        background: var(--ft-paper) !important;
      }
      /* Soft Bath blur behind the luxury paper — deepens on scroll */
      .ft-sky {
        position: fixed;
        inset: -6%;
        z-index: 0;
        pointer-events: none;
        background:
          url("https://images.unsplash.com/photo-1729232766572-6e3ec9650311?auto=format&fit=crop&w=2400&q=80")
          center center / cover no-repeat;
        transform: scale(1.1);
        filter: blur(var(--ft-sky-blur, 18px)) saturate(1.05) brightness(1.08) sepia(0.18) hue-rotate(-8deg);
        opacity: 0.28;
        will-change: filter, opacity;
      }
      .ft-sky-tint {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background:
          linear-gradient(180deg, rgba(251,243,228,0.7) 0%, rgba(251,243,228,0.9) 55%, #fbf3e4 100%),
          radial-gradient(900px 480px at 85% 8%, rgba(240,180,41,0.22), transparent 55%),
          radial-gradient(700px 420px at 10% 40%, rgba(232,106,23,0.12), transparent 50%);
      }
      ::selection {
        background: var(--ft-orange);
        color: #fff;
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        position: relative;
        z-index: 1;
        padding-top: 1.25rem !important;
        padding-bottom: 4rem !important;
        padding-left: clamp(1.25rem, 4vw, 3.5rem) !important;
        padding-right: clamp(1.25rem, 4vw, 3.5rem) !important;
        max-width: 100% !important;
      }

      @keyframes ftHeroIn {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
      }
      @keyframes ftShine {
        0% { transform: translateX(-130%) rotate(14deg); }
        100% { transform: translateX(230%) rotate(14deg); }
      }
      @keyframes ftBob {
        0%, 100% { transform: translateY(-2px); }
        50% { transform: translateY(5px); }
      }

      .ft-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 1.6rem;
        animation: ftHeroIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
      }
      .ft-logo {
        font-family: var(--ft-serif) !important;
        font-style: italic;
        font-size: 1.55rem;
        font-weight: 400;
        letter-spacing: -0.02em;
        color: var(--ft-orange);
        margin: 0;
      }
      .ft-nav {
        display: flex;
        gap: 1.5rem;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: var(--ft-muted);
      }
      .ft-nav span { color: var(--ft-ink); }

      .ft-headline-row {
        display: grid;
        grid-template-columns: 1fr minmax(12rem, 18rem);
        gap: 1.5rem 2rem;
        align-items: end;
        margin: 0 0 1.4rem;
        animation: ftHeroIn 0.85s cubic-bezier(0.22, 1, 0.36, 1) 0.05s both;
      }
      .ft-headline {
        font-family: var(--ft-display) !important;
        font-size: clamp(3.2rem, 9.2vw, 7.2rem);
        font-weight: 800;
        line-height: 0.86;
        letter-spacing: -0.055em;
        text-transform: uppercase;
        color: var(--ft-ink);
        margin: 0;
        max-width: 12ch;
      }
      .ft-headline-aside {
        font-size: 0.95rem;
        line-height: 1.55;
        color: var(--ft-muted);
        font-weight: 500;
        margin: 0 0 0.4rem;
        max-width: 18rem;
      }

      /* Only the title panel is glass — sits on the Bath photo */
      .ft-hero {
        position: relative;
        overflow: hidden;
        isolation: isolate;
        min-height: min(62vh, 640px);
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        border-radius: 36px;
        padding: clamp(1.6rem, 3.5vw, 2.8rem);
        margin: 0 0 1.15rem 0;
        width: 100%;
        box-sizing: border-box;
        background:
          linear-gradient(180deg, rgba(232,106,23,0.12) 0%, rgba(28,20,14,0.5) 100%),
          url("https://images.unsplash.com/photo-1729232766572-6e3ec9650311?auto=format&fit=crop&w=2400&q=80")
          center 40% / cover no-repeat;
        border: 0;
        box-shadow: 0 30px 70px rgba(120, 55, 10, 0.16);
        animation: ftHeroIn 0.9s cubic-bezier(0.22, 1, 0.36, 1) 0.1s both;
      }
      .ft-hero-glass {
        position: relative;
        z-index: 1;
        max-width: min(100%, 34rem);
        border-radius: 22px;
        padding: 1.35rem 1.4rem 1.3rem;
        background: linear-gradient(165deg, rgba(255,236,190,0.5), rgba(255,180,80,0.16));
        border: 1px solid rgba(255, 220, 150, 0.55);
        box-shadow:
          0 18px 40px rgba(120, 55, 10, 0.18),
          inset 0 1px 0 rgba(255, 245, 210, 0.75);
        backdrop-filter: blur(28px) saturate(1.35);
        -webkit-backdrop-filter: blur(28px) saturate(1.35);
        overflow: hidden;
      }
      .ft-hero-glass::before {
        content: "";
        position: absolute;
        inset: -45% auto auto -25%;
        width: 50%;
        height: 150%;
        background: linear-gradient(90deg, transparent, rgba(255,240,180,0.55), transparent);
        animation: ftShine 6.5s ease-in-out infinite;
        pointer-events: none;
      }
      .ft-tag {
        position: relative;
        z-index: 1;
        display: inline-block;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: rgba(255, 230, 170, 0.95);
        margin-bottom: 0.55rem;
      }
      .ft-brand {
        position: relative;
        z-index: 1;
        font-family: var(--ft-serif) !important;
        font-size: clamp(1.9rem, 3.5vw, 2.6rem);
        font-weight: 400;
        font-style: italic;
        margin: 0 0 0.45rem 0;
        line-height: 1;
        letter-spacing: -0.02em;
        color: #fff8e8;
      }
      .ft-sub {
        position: relative;
        z-index: 1;
        margin: 0;
        font-size: 0.95rem;
        max-width: 28rem;
        line-height: 1.5;
        color: rgba(255,255,255,0.88);
        font-weight: 500;
      }
      .ft-points {
        position: relative;
        z-index: 1;
        display: flex;
        flex-wrap: wrap;
        gap: 1.1rem;
        margin-top: 1rem;
      }
      .ft-points span {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: rgba(255,255,255,0.85);
        padding: 0;
        border: 0;
        background: none;
        box-shadow: none;
      }

      .ft-scroll-hint {
        text-align: left;
        color: var(--ft-muted);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin: 0.2rem 0 1rem;
        background: none;
        border: 0;
        padding: 0;
        box-shadow: none;
      }
      .ft-arrow {
        display: inline-block;
        margin-right: 0.35rem;
        animation: ftBob 1.5s ease-in-out infinite;
      }

      /* Body copy: clean luxury text, no bubbles */
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(1.8rem, 3.5vw, 2.6rem);
        font-weight: 700;
        margin: 2.8rem 0 0.75rem;
        color: var(--ft-ink);
        letter-spacing: -0.04em;
        line-height: 1.05;
        text-transform: uppercase;
        display: block;
        padding: 0;
        border: 0;
        background: none;
        box-shadow: none;
        backdrop-filter: none;
      }
      .ft-section::after {
        content: "";
        display: block;
        width: 40px;
        height: 2px;
        background: linear-gradient(90deg, var(--ft-orange), var(--ft-yellow));
        margin-top: 0.7rem;
      }
      .ft-lead, .ft-body {
        padding: 0;
        border-radius: 0;
        background: none;
        border: 0;
        backdrop-filter: none;
        box-shadow: none;
      }
      .ft-lead {
        font-size: 1.12rem;
        line-height: 1.65;
        color: var(--ft-ink);
        font-weight: 500;
        letter-spacing: -0.015em;
        max-width: 44rem;
        margin: 0 0 0.85rem 0;
      }
      .ft-body {
        font-size: 1.02rem;
        line-height: 1.7;
        color: var(--ft-muted);
        letter-spacing: -0.01em;
        max-width: 44rem;
        margin: 0 0 0.75rem 0;
      }

      .ft-serve {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1.5rem;
        align-items: start;
        margin: 0.2rem 0 0.5rem;
      }
      .ft-serve .ft-card {
        height: 100%;
        margin: 0;
      }
      .ft-serve .ft-card h3 {
        min-height: 2.6rem;
        line-height: 1.15;
      }
      @media (max-width: 800px) {
        .ft-serve { grid-template-columns: 1fr; }
        .ft-serve .ft-card h3 { min-height: 0; }
      }
      .ft-card {
        position: relative;
        overflow: hidden;
        background: transparent;
        border: 0;
        border-bottom: 1px solid var(--ft-line);
        border-radius: 0;
        padding: 1.25rem 0 1.15rem;
        margin-bottom: 0;
        box-shadow: none;
        backdrop-filter: none;
        transition: transform 0.25s ease;
      }
      .ft-card::before { display: none; }
      .ft-card:hover {
        transform: translateX(4px);
        box-shadow: none;
      }
      .ft-card h3 {
        font-family: var(--ft-display) !important;
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0 0 0.35rem 0;
        padding: 0;
        color: var(--ft-ink);
        letter-spacing: -0.03em;
        text-transform: uppercase;
      }
      .ft-card p {
        font-size: 0.98rem;
        line-height: 1.6;
        color: var(--ft-muted);
        margin: 0;
        letter-spacing: -0.01em;
      }

      .ft-footer {
        text-align: left;
        color: var(--ft-muted);
        font-size: 0.95rem;
        margin-top: 3.2rem;
        padding: 1.5rem 0 0;
        border: 0;
        border-top: 1px solid var(--ft-line);
        border-radius: 0;
        background: none;
        backdrop-filter: none;
        box-shadow: none;
        font-weight: 500;
        line-height: 1.65;
      }
      .ft-footer strong {
        font-family: var(--ft-serif);
        font-size: 1.35rem;
        font-style: italic;
        font-weight: 400;
        letter-spacing: -0.02em;
        color: var(--ft-ink);
      }

      div[data-testid="stButton"] button,
      .stLinkButton a {
        border-radius: 999px !important;
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        padding: 0.85rem 1.45rem !important;
        letter-spacing: 0.06em !important;
        text-transform: uppercase !important;
        background: linear-gradient(135deg, var(--ft-orange), #f08c2b) !important;
        color: #ffffff !important;
        border: 1px solid var(--ft-orange) !important;
        box-shadow: 0 10px 24px rgba(232, 106, 23, 0.28) !important;
        backdrop-filter: none !important;
        transition: transform 0.25s ease, background 0.25s ease, color 0.25s ease, box-shadow 0.25s ease !important;
      }
      div[data-testid="stButton"] button p,
      .stLinkButton a p {
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        letter-spacing: 0.06em !important;
      }
      div[data-testid="stButton"] button:hover,
      .stLinkButton a:hover {
        background: var(--ft-yellow) !important;
        color: #1c140e !important;
        border-color: var(--ft-yellow) !important;
        box-shadow: 0 12px 28px rgba(240, 180, 41, 0.35) !important;
        transform: translateY(-2px) !important;
      }
      div[data-testid="stButton"] button:hover p,
      .stLinkButton a:hover p {
        color: #1c140e !important;
      }

      .ft-reveal:not(.ft-in) { opacity: 0; }
      .ft-in { animation: ftRise 0.75s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .ft-section.ft-in { animation-name: ftSlideIn; }
      .ft-card.ft-in { animation-name: ftPop; }
      @keyframes ftRise {
        from { opacity: 0; transform: translateY(28px); }
      }
      @keyframes ftSlideIn {
        from { opacity: 0; transform: translateY(24px); }
      }
      @keyframes ftPop {
        from { opacity: 0; transform: translateY(20px); }
      }
      @media (prefers-reduced-motion: reduce) {
        .ft-reveal:not(.ft-in) { opacity: 1; }
        .ft-in, .ft-arrow, .ft-hero-glass::before { animation: none; }
      }
      @media (max-width: 800px) {
        .ft-headline-row { grid-template-columns: 1fr; }
        .ft-nav { display: none; }
        .ft-hero { min-height: 54vh; border-radius: 26px; }
      }
    </style>
    """
)

# --- Estato-style hero: big type + rounded Bath photo with glass title ---
show_html(
    """
    <div class="ft-sky" aria-hidden="true"></div>
    <div class="ft-sky-tint" aria-hidden="true"></div>
    <div class="ft-top">
      <p class="ft-logo">LoadedBites</p>
      <div class="ft-nav">
        <span>Home</span>
        <span>Menu</span>
        <span>Bath</span>
        <span>Contact</span>
      </div>
    </div>
    <div class="ft-headline-row">
      <h1 class="ft-headline">Future of<br>street<br>dining</h1>
      <p class="ft-headline-aside">
        We craft generous, carefully prepared bites that bring lively energy to Bath’s streets.
      </p>
    </div>
    <div class="ft-hero">
      <div class="ft-hero-glass">
        <div class="ft-tag">Bath · United Kingdom</div>
        <p class="ft-brand">LoadedBites GLA</p>
        <p class="ft-sub">
          Refined street dining — cooked to order, properly loaded, served fresh across Bath.
        </p>
        <div class="ft-points">
          <span>Cooked to order</span>
          <span>Generous portions</span>
          <span>Across Bath</span>
        </div>
      </div>
    </div>
    <p class="ft-scroll-hint"><span class="ft-arrow">↓</span> Explore</p>
    """
)

# --- Three glass feature boxes ---
components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Syne:wght@700;800&family=Manrope:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
      html, body {
        margin: 0;
        background: transparent;
        font-family: "Manrope", sans-serif;
        color: #111;
        width: 100%;
        overflow: hidden;
      }
      .track {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        padding: 0.15rem 2px 1rem;
        width: 100%;
        box-sizing: border-box;
      }
      .bit { width: 100%; min-width: 0; }
      .bit-inner {
        width: 100%;
        height: 100%;
        box-sizing: border-box;
        border-radius: 24px;
        padding: 1.65rem 1.45rem 1.45rem;
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
        justify-content: flex-end;
        min-height: 200px;
        border: 1px solid rgba(255, 210, 140, 0.55);
        background:
          linear-gradient(165deg, rgba(255,230,170,0.55), rgba(232,106,23,0.18)),
          url("https://images.unsplash.com/photo-1729232766572-6e3ec9650311?auto=format&fit=crop&w=1200&q=70")
          center / cover no-repeat;
        box-shadow:
          0 16px 36px rgba(120, 55, 10, 0.12),
          inset 0 1px 0 rgba(255, 240, 200, 0.75);
        backdrop-filter: blur(22px) saturate(1.3);
        -webkit-backdrop-filter: blur(22px) saturate(1.3);
        position: relative;
        overflow: hidden;
        cursor: default;
        transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.35s ease;
      }
      .bit-2 .bit-inner {
        background:
          linear-gradient(165deg, rgba(255,230,170,0.55), rgba(232,106,23,0.18)),
          url("https://images.pexels.com/photos/14494034/pexels-photo-14494034.jpeg?auto=compress&cs=tinysrgb&w=1200")
          center 40% / cover no-repeat;
      }
      .bit-3 .bit-inner {
        background:
          linear-gradient(165deg, rgba(255,230,170,0.55), rgba(232,106,23,0.18)),
          url("https://images.pexels.com/photos/14494033/pexels-photo-14494033.jpeg?auto=compress&cs=tinysrgb&w=1200")
          center 35% / cover no-repeat;
      }
      .bit-inner::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(232,106,23,0.08), rgba(28,20,14,0.48));
        pointer-events: none;
      }
      .bit-inner > * { position: relative; z-index: 1; }
      .bit-inner::after {
        content: "01";
        position: absolute;
        top: 1.05rem;
        right: 1.1rem;
        z-index: 1;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        color: rgba(255,255,255,0.8);
      }
      .bit-2 .bit-inner::after { content: "02"; }
      .bit-3 .bit-inner::after { content: "03"; }
      .bit-inner:hover {
        transform: translateY(-5px);
        box-shadow: 0 24px 48px rgba(0, 0, 0, 0.16), inset 0 1px 0 rgba(255, 255, 255, 0.8);
      }
      .bit-kicker {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: rgba(255, 230, 170, 0.92);
      }
      .bit-words {
        font-family: "Syne", sans-serif;
        font-size: clamp(1.35rem, 2vw, 1.75rem);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.05;
        text-transform: uppercase;
        color: #ffffff;
        margin: 0;
      }
      .bit-sub {
        margin: 0;
        font-size: 0.9rem;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.85);
        letter-spacing: -0.01em;
        max-width: 22rem;
      }
      .bit:not(.in) .bit-inner { opacity: 0; }
      .bit.in .bit-inner { animation: rise 0.85s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .bit-2.in .bit-inner { animation-delay: 0.08s; }
      .bit-3.in .bit-inner { animation-delay: 0.16s; }
      @keyframes rise {
        from { opacity: 0; transform: translateY(28px); filter: blur(6px); }
      }
      @media (max-width: 900px) {
        .track { grid-template-columns: 1fr; }
        .bit-inner { min-height: 150px; }
      }
      @media (prefers-reduced-motion: reduce) {
        .bit:not(.in) .bit-inner { opacity: 1; }
        .bit.in .bit-inner { animation: none; }
      }
    </style>

    <div class="track" id="track">
      <div class="bit bit-1">
        <div class="bit-inner">
          <div class="bit-kicker">LoadedBites GLA</div>
          <p class="bit-words">Fresh Hot Bites</p>
          <p class="bit-sub">Prepared to order by our Bath food vendor.</p>
        </div>
      </div>
      <div class="bit bit-2">
        <div class="bit-inner">
          <div class="bit-kicker">Serving Bath</div>
          <p class="bit-words">Properly Loaded</p>
          <p class="bit-sub">Generous portions, considered seasoning, consistent quality.</p>
        </div>
      </div>
      <div class="bit bit-3">
        <div class="bit-inner">
          <div class="bit-kicker">Find our vendor</div>
          <p class="bit-words">Bath Food Vendor</p>
          <p class="bit-sub">Follow updates for today’s location and hours.</p>
        </div>
      </div>
    </div>

    <script>
      const track = document.getElementById("track");
      const fit = () => {
        try {
          window.frameElement.style.height = Math.ceil(track.getBoundingClientRect().height) + "px";
        } catch (err) {}
      };
      new ResizeObserver(fit).observe(track);
      fit();

      const bits = document.querySelectorAll(".bit");
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) entry.target.classList.add("in");
          });
        },
        { threshold: 0.25 }
      );
      bits.forEach((bit) => io.observe(bit));

      try {
        const page = window.parent;
        const doc = page.document;
        const targets = ".ft-section, .ft-lead, .ft-body, .ft-card, .ft-footer, .stLinkButton";
        if (page.__ftReveal) page.__ftReveal.forEach((o) => o.disconnect());
        const reveal = new page.IntersectionObserver(
          (entries) => {
            let order = 0;
            entries.forEach((entry) => {
              if (!entry.isIntersecting) return;
              entry.target.style.animationDelay = order * 80 + "ms";
              entry.target.classList.add("ft-in");
              reveal.unobserve(entry.target);
              order += 1;
            });
          },
          { threshold: 0.15, rootMargin: "0px 0px -6% 0px" }
        );
        const tag = () => {
          doc.querySelectorAll(targets).forEach((el) => {
            if (el.classList.contains("ft-in")) return;
            el.classList.add("ft-reveal");
            reveal.observe(el);
          });
        };
        const watcher = new page.MutationObserver(tag);
        watcher.observe(doc.body, { childList: true, subtree: true });
        page.__ftReveal = [reveal, watcher];
        tag();

        const sky = () => doc.querySelector(".ft-sky");
        const scrollTop = () => {
          const nodes = [
            doc.scrollingElement,
            doc.documentElement,
            doc.body,
            doc.querySelector(".stApp"),
            doc.querySelector('[data-testid="stAppViewContainer"]'),
            doc.querySelector("section.main"),
          ].filter(Boolean);
          let top = 0, max = 1;
          nodes.forEach((n) => {
            top = Math.max(top, n.scrollTop || 0);
            max = Math.max(max, (n.scrollHeight || 0) - (n.clientHeight || 0));
          });
          return { top, max: Math.max(1, max) };
        };
        const onScroll = () => {
          const el = sky();
          if (!el) return;
          const { top, max } = scrollTop();
          const t = Math.min(1, Math.max(0, top / max));
          el.style.setProperty("--ft-sky-blur", (18 + t * 22).toFixed(2) + "px");
          el.style.opacity = (0.22 + t * 0.18).toFixed(3);
        };
        if (!page.__ftSkyBlur) {
          ["scroll", "wheel", "touchmove"].forEach((evt) => {
            page.addEventListener(evt, onScroll, { passive: true });
            doc.addEventListener(evt, onScroll, { passive: true });
          });
          page.__ftSkyBlur = true;
          onScroll();
          setInterval(onScroll, 250);
        }
      } catch (err) {
        console.warn("Scroll effects unavailable:", err);
      }
    </script>
    """,
    height=260,
    scrolling=False,
)

# --- Full writing ---
show_html('<p class="ft-section">Welcome to Bath</p>')
show_html(
    """
    <p class="ft-lead">
      LoadedBites GLA is a Bath food vendor offering thoughtfully prepared street dining for
      customers who value quality, generosity, and consistency. Each order is seasoned with care,
      finished with considered toppings, and served with professionalism.
    </p>
    <p class="ft-body">
      Whether you join us at lunch, after work, or over the weekend, our commitment remains the same:
      honest cooking, made to order, rich in flavour, and ready when you are.
      We provide an efficient outdoor service — a trusted vendor, a well-run kitchen, and food
      prepared to a high standard.
    </p>
    """
)

show_html('<p class="ft-section">Why LoadedBites GLA</p>')
left, right = st.columns(2, gap="large")
with left:
    show_html(
        """
        <div class="ft-card">
          <h3>Generously prepared</h3>
          <p>
            Every serving is assembled with care — balanced sauces, quality toppings,
            and portions designed to satisfy without compromise.
          </p>
        </div>
        <div class="ft-card">
          <h3>Cooked to order</h3>
          <p>
            Your meal begins when you place your order. Dishes are served hot from our vendor,
            never held under heat lamps for extended periods.
          </p>
        </div>
        """
    )
with right:
    show_html(
        """
        <div class="ft-card">
          <h3>Rooted in Bath</h3>
          <p>
            Built for this city — efficient enough for a lunch appointment,
            refined enough for an evening out, and welcoming enough for return visits.
          </p>
        </div>
        <div class="ft-card">
          <h3>Clear value</h3>
          <p>
            Street dining should feel worthwhile. We offer substantial portions,
            confident flavour, and pricing suited to individuals and groups alike.
          </p>
        </div>
        """
    )

show_html('<p class="ft-section">Our food</p>')
show_html(
    """
    <p class="ft-lead">
      LoadedBites GLA specialises in generous, well-seasoned comfort dishes —
      crisp bases, rich fillings, melted cheese, house sauces, and carefully chosen toppings
      finished to a satisfying standard.
    </p>
    <p class="ft-body">
      Our offering includes warm wraps with seasoned protein and fresh contrast, cheese-led plates
      with depth and texture, and gently spiced options for those who prefer more heat.
      Everything is cooked to order at our food vendor and served ready to enjoy.
    </p>
    <p class="ft-body">
      Daily specials may vary by location and season — sometimes smoked, sometimes sweet —
      while our principles remain constant: generous portions, assured flavour, and a polished
      takeaway experience. Please speak with our team if you have a particular request.
    </p>
    """
)

show_html('<p class="ft-section">Find our food vendor</p>')
show_html(
    """
    <p class="ft-lead">
      LoadedBites GLA operates across Bath — city-centre lunch service, local venues, events,
      and selected weekend locations. We publish our position so you can plan your visit with ease.
    </p>
    <p class="ft-body">
      Standard hours focus on lunch through early evening, with extended service when demand requires.
      We remain committed to reliable quality regardless of weather or schedule.
    </p>
    <p class="ft-body">
      <strong>Recommendation:</strong> review our Instagram updates before travelling for today’s
      location, opening time, and availability notices.
    </p>
    """
)

show_html('<p class="ft-section">Who we serve</p>')
show_html(
    """
    <div class="ft-serve">
      <div class="ft-card">
        <h3>Business lunch</h3>
        <p>Efficient service for a limited break, without sacrificing quality.</p>
      </div>
      <div class="ft-card">
        <h3>Evening dining</h3>
        <p>A substantial, well-prepared option before or after your evening plans.</p>
      </div>
      <div class="ft-card">
        <h3>Groups &amp; families</h3>
        <p>Straightforward ordering for shared meals, with options to suit a range of tastes.</p>
      </div>
    </div>
    """
)

show_html('<p class="ft-section">Get in touch</p>')
show_html(
    """
    <p class="ft-lead">
      For today’s location, private bookings, or current specials, please contact us.
      We are pleased to serve Bath and surrounding guests.
    </p>
    <p class="ft-body">
      Reach us via Instagram or WhatsApp for location updates, catering enquiries,
      and event arrangements. For birthdays, workplace lunches, or market days,
      LoadedBites GLA can provide a dependable on-site food service.
    </p>
    """
)

col_a, col_b = st.columns(2, gap="large")
with col_a:
    st.link_button(
        "Instagram — @loadedbitesgla",
        "https://instagram.com/loadedbitesgla",
        use_container_width=True,
    )
with col_b:
    st.link_button(
        "WhatsApp enquiry",
        "https://wa.me/",
        use_container_width=True,
    )

show_html(
    """
    <div class="ft-footer">
      <strong>LoadedBites GLA</strong> · Bath food vendor<br>
      Freshly prepared · Generously served · Professionally run
    </div>
    """
)
