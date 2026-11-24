from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


st.set_page_config(
    page_title="LoadedBites GLA",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Page styling ---
show_html(
    """
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap");

      :root {
        --ft-display: "Space Grotesk", sans-serif;
        --ft-sans: "Outfit", sans-serif;
        --ft-red: #9f1239;
        --ft-deep: #881337;
        --ft-night: #4c0519;
        --ft-gold: #fde047;
        --ft-cream: #fff1f2;
      }

      html, body, .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"],
      [data-testid="stCaption"], [data-testid="stAlert"],
      div[data-testid="stButton"] button, .stLinkButton a {
        font-family: var(--ft-sans) !important;
      }

      html, body, .stApp {
        font-size: 18px;
        line-height: 1.55;
        -webkit-font-smoothing: antialiased;
        color: #ffffff;
      }

      .stApp {
        background: var(--ft-red);
      }
      ::selection {
        background: var(--ft-gold);
        color: var(--ft-night);
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        padding-top: 1.6rem;
        padding-bottom: 3rem;
        padding-left: 1.4rem !important;
        padding-right: 1.4rem !important;
        max-width: 1180px;
      }

      @keyframes ftHeroIn {
        from { opacity: 0; transform: translateY(24px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
      }

      /* Hero */
      .ft-hero {
        position: relative;
        overflow: hidden;
        background: linear-gradient(120deg, #be123c 0%, #e11d48 38%, #fb7185 72%, #fde047 120%);
        border: 1px solid rgba(255, 255, 255, 0.28);
        border-radius: 28px;
        padding: 3.4rem 3rem 3.1rem;
        margin-bottom: 0.35rem;
        box-shadow: 0 24px 60px rgba(76, 5, 25, 0.45);
        animation: ftHeroIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        box-sizing: border-box;
      }
      .ft-hero::after {
        content: "";
        position: absolute;
        right: -90px;
        top: -120px;
        width: 360px;
        height: 360px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(253, 224, 71, 0.5), rgba(253, 224, 71, 0) 68%);
        pointer-events: none;
      }
      .ft-hero:hover {
        transform: scale(1.015);
        box-shadow: 0 28px 66px rgba(76, 5, 25, 0.55);
      }
      .ft-tag {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        background: var(--ft-deep);
        color: var(--ft-gold);
        padding: 0.45rem 0.85rem;
        border-radius: 999px;
        margin-bottom: 1rem;
        transition: transform 0.25s ease;
      }
      .ft-tag:hover { transform: scale(1.12); }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.7rem, 6vw, 4.2rem);
        font-weight: 700;
        margin: 0 0 0.7rem 0;
        line-height: 0.98;
        letter-spacing: -0.055em;
        color: #ffffff;
        display: block;
        width: fit-content;
        transform-origin: left center;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
      }
      .ft-brand:hover { transform: scale(1.06); }
      .ft-sub {
        margin: 0;
        font-size: 1.18rem;
        max-width: 38rem;
        line-height: 1.5;
        color: #ffffff;
        font-weight: 500;
        letter-spacing: -0.015em;
        transition: transform 0.28s ease;
        transform-origin: left center;
      }
      .ft-sub:hover { transform: scale(1.04); }
      .ft-points {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1.4rem;
      }
      .ft-points span {
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        padding: 0.4rem 0.85rem;
        border-radius: 999px;
        background: rgba(76, 5, 25, 0.34);
        border: 1px solid rgba(255, 255, 255, 0.38);
        color: #ffffff;
        transition: transform 0.25s ease, background 0.25s ease;
      }
      .ft-points span:hover {
        transform: scale(1.08);
        background: rgba(76, 5, 25, 0.55);
      }

      .ft-scroll-hint {
        text-align: center;
        color: #ffffff;
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: -0.01em;
        margin: 0.3rem 0 0.1rem;
        opacity: 0.85;
        transition: transform 0.25s ease, opacity 0.25s ease;
      }
      .ft-scroll-hint:hover {
        transform: scale(1.1);
        opacity: 1;
      }
      .ft-arrow {
        display: inline-block;
        color: var(--ft-gold);
        animation: ftBob 1.4s ease-in-out infinite;
      }
      @keyframes ftBob {
        0%, 100% { transform: translateY(-3px); }
        50% { transform: translateY(5px); }
      }

      /* Sections */
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(1.8rem, 3.2vw, 2.3rem);
        font-weight: 700;
        margin: 2.1rem 0 0.5rem;
        color: #ffffff;
        letter-spacing: -0.045em;
        line-height: 1.05;
        display: inline-block;
        transform-origin: left center;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
      }
      .ft-section::after {
        content: "";
        display: block;
        width: 56px;
        height: 4px;
        border-radius: 999px;
        background: var(--ft-gold);
        margin-top: 0.6rem;
      }
      .ft-section:hover { transform: scale(1.06); }
      .ft-lead {
        font-size: 1.18rem;
        line-height: 1.55;
        color: #ffffff;
        font-weight: 500;
        letter-spacing: -0.015em;
        max-width: 50rem;
        margin: 0 0 0.75rem 0;
        transition: transform 0.28s ease;
        transform-origin: left top;
      }
      .ft-lead:hover { transform: scale(1.035); }
      .ft-body {
        font-size: 1.05rem;
        line-height: 1.6;
        color: #ffffff;
        letter-spacing: -0.01em;
        max-width: 50rem;
        margin: 0 0 0.7rem 0;
        transition: transform 0.28s ease;
        transform-origin: left top;
      }
      .ft-body:hover { transform: scale(1.035); }

      /* Cards */
      .ft-card {
        position: relative;
        overflow: hidden;
        background: var(--ft-deep);
        border: 1px solid rgba(255, 255, 255, 0.28);
        border-radius: 18px;
        padding: 1.25rem 1.3rem 1.2rem 1.5rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 12px 30px rgba(76, 5, 25, 0.38);
        transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.3s ease, border-color 0.3s ease;
      }
      .ft-card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 5px;
        background: var(--ft-gold);
      }
      .ft-card:hover {
        transform: scale(1.04);
        border-color: rgba(253, 224, 71, 0.85);
        box-shadow: 0 18px 40px rgba(76, 5, 25, 0.55);
      }
      .ft-card h3 {
        font-family: var(--ft-display) !important;
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0 0 0.35rem 0;
        padding: 0;
        color: #ffffff;
        letter-spacing: -0.035em;
      }
      .ft-card p {
        font-size: 0.98rem;
        line-height: 1.55;
        color: #ffffff;
        margin: 0;
        letter-spacing: -0.01em;
      }

      .ft-footer {
        text-align: center;
        color: #ffffff;
        font-size: 0.92rem;
        margin-top: 2.4rem;
        padding-top: 1.4rem;
        border-top: 1px solid rgba(255, 255, 255, 0.35);
        font-weight: 500;
        line-height: 1.6;
        transition: transform 0.25s ease;
      }
      .ft-footer strong {
        font-family: var(--ft-display);
        font-size: 1.1rem;
        letter-spacing: -0.03em;
      }
      .ft-footer:hover { transform: scale(1.04); }

      /* Buttons */
      div[data-testid="stButton"] button,
      .stLinkButton a {
        border-radius: 999px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.8rem 1.3rem !important;
        letter-spacing: -0.01em !important;
        background: var(--ft-cream) !important;
        color: var(--ft-red) !important;
        border: 2px solid var(--ft-cream) !important;
        box-shadow: 0 10px 24px rgba(76, 5, 25, 0.38) !important;
        transition: transform 0.25s ease, background 0.25s ease,
                    border-color 0.25s ease !important;
      }
      div[data-testid="stButton"] button p,
      .stLinkButton a p {
        font-size: 1rem !important;
        font-weight: 700 !important;
      }
      div[data-testid="stButton"] button:hover,
      .stLinkButton a:hover {
        background: var(--ft-gold) !important;
        border-color: var(--ft-gold) !important;
        color: var(--ft-night) !important;
        transform: translateY(-2px) scale(1.03) !important;
      }

      /* Scroll reveal: the script in the advert block adds .ft-reveal to each
         section, then .ft-in once it scrolls into view. The keyframes only set
         a starting state, so hover effects still work afterwards. */
      .ft-reveal:not(.ft-in) { opacity: 0; }
      .ft-in { animation: ftRise 0.8s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .ft-section.ft-in { animation-name: ftSlideIn; }
      .ft-card.ft-in { animation-name: ftPop; }
      @keyframes ftRise {
        from { opacity: 0; transform: translateY(38px); filter: blur(6px); }
      }
      @keyframes ftSlideIn {
        from { opacity: 0; transform: translateX(-70px); }
      }
      @keyframes ftPop {
        from { opacity: 0; transform: translateY(54px) scale(0.9); }
      }
      @media (prefers-reduced-motion: reduce) {
        .ft-reveal:not(.ft-in) { opacity: 1; }
        .ft-in, .ft-arrow { animation: none; }
      }
      @media (max-width: 640px) {
        .ft-hero { padding: 2.2rem 1.5rem 2rem; border-radius: 22px; }
      }
    </style>
    """
)

# --- Hero ---
show_html(
    """
    <div class="ft-hero">
      <div class="ft-tag">Bath food vendor</div>
      <p class="ft-brand">LoadedBites GLA</p>
      <p class="ft-sub">
        Refined street dining in Bath — generous portions, carefully prepared dishes,
        and fresh service from our food vendor throughout the city.
      </p>
      <div class="ft-points">
        <span>Cooked to order</span>
        <span>Generous portions</span>
        <span>Across Bath</span>
      </div>
    </div>
    <p class="ft-scroll-hint"><span class="ft-arrow">↓</span> Explore the showcase below</p>
    """
)

# --- Scroll-triggered advert panels ---
components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <style>
      html, body {
        margin: 0;
        background: transparent;
        font-family: "Outfit", sans-serif;
        color: #ffffff;
        width: 100%;
        overflow: hidden;
      }
      .track {
        display: flex;
        flex-direction: column;
        gap: 1.1rem;
        padding: 0.3rem 2px 2rem;
        width: 100%;
        box-sizing: border-box;
      }
      .bit { width: 100%; }

      .bit-inner {
        width: 100%;
        box-sizing: border-box;
        border-radius: 20px;
        padding: 1.8rem 2rem 1.6rem;
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
        justify-content: center;
        min-height: 120px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 18px 30px -16px rgba(76, 5, 25, 0.8);
        transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.35s ease;
        cursor: default;
        position: relative;
        overflow: hidden;
        will-change: transform, opacity, filter;
      }
      .bit-inner::after {
        content: "FEATURED";
        position: absolute;
        top: 1rem;
        right: 1.1rem;
        font-size: 0.66rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        color: #ffffff;
        background: rgba(76, 5, 25, 0.55);
        padding: 0.3rem 0.65rem;
        border-radius: 999px;
      }
      .bit-1 .bit-inner {
        background: linear-gradient(115deg, #be123c 0%, #e11d48 55%, #fb7185 100%);
      }
      .bit-2 .bit-inner {
        background: linear-gradient(115deg, #881337 0%, #f43f5e 55%, #fde047 115%);
      }
      .bit-3 .bit-inner {
        background: linear-gradient(115deg, #4c0519 0%, #be123c 50%, #fb7185 100%);
      }
      .bit-inner:hover {
        transform: scale(1.02);
        box-shadow: 0 22px 34px -16px rgba(76, 5, 25, 0.95);
      }
      .bit-kicker {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #fde047;
      }
      .bit-words {
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(2rem, 5vw, 3.1rem);
        font-weight: 700;
        letter-spacing: -0.05em;
        line-height: 1.05;
        color: #ffffff;
        margin: 0;
        transition: transform 0.3s ease;
        transform-origin: left center;
      }
      .bit-inner:hover .bit-words {
        transform: scale(1.06);
      }
      .bit-sub {
        margin: 0;
        font-size: 1.05rem;
        font-weight: 500;
        color: #ffffff;
        letter-spacing: -0.015em;
        max-width: 36rem;
      }

      /* Each panel waits hidden, then sweeps in when its row scrolls into view.
         The row itself never moves, so the scroll check stays reliable. */
      .bit:not(.in) .bit-inner { opacity: 0; }
      .bit-1.in .bit-inner { animation: adSweepLeft 0.95s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .bit-2.in .bit-inner { animation: adSweepRight 0.95s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .bit-3.in .bit-inner { animation: adDropSpin 1.05s cubic-bezier(0.34, 1.3, 0.64, 1) backwards; }

      @keyframes adSweepLeft {
        0% { opacity: 0; filter: blur(12px); transform: translateX(-110%) rotate(-10deg); }
        70% { opacity: 1; filter: blur(0); transform: translateX(2%) rotate(2deg); }
      }
      @keyframes adSweepRight {
        0% { opacity: 0; filter: blur(12px); transform: translateX(110%) rotate(10deg); }
        70% { opacity: 1; filter: blur(0); transform: translateX(-2%) rotate(-2deg); }
      }
      @keyframes adDropSpin {
        0% { opacity: 0; filter: blur(14px); transform: translateY(90px) scale(0.9) rotate(-12deg); }
        60% { opacity: 1; filter: blur(0); transform: translateY(-10px) scale(1.03) rotate(3deg); }
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
          <p class="bit-words">Properly Loaded Food</p>
          <p class="bit-sub">Generous portions, considered seasoning, and consistent quality.</p>
        </div>
      </div>
      <div class="bit bit-3">
        <div class="bit-inner">
          <div class="bit-kicker">Find our vendor</div>
          <p class="bit-words">Bath Food Vendor</p>
          <p class="bit-sub">Follow our updates for today’s location and service hours.</p>
        </div>
      </div>
    </div>

    <script>
      // Keep this frame exactly as tall as its content.
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
        { threshold: 0.3 }
      );
      bits.forEach((bit) => io.observe(bit));

      // Scroll reveal for the rest of the page, which lives outside this frame.
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
              entry.target.style.animationDelay = order * 110 + "ms";
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

        // Streamlit adds sections as the script runs, so keep watching for new ones.
        const watcher = new page.MutationObserver(tag);
        watcher.observe(doc.body, { childList: true, subtree: true });
        page.__ftReveal = [reveal, watcher];
        tag();
      } catch (err) {
        console.warn("Scroll reveal unavailable:", err);
      }
    </script>
    """,
    height=560,
    scrolling=False,
)

# --- Interactive food truck ---
show_html('<p class="ft-section">Our food truck</p>')
show_html(
    """
    <p class="ft-lead">
      A closer look at how we serve. Select the hatch, the menu, the headlights,
      the cab or a wheel to see it at work.
    </p>
    """
)

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <style>
      html, body {
        margin: 0;
        background: transparent;
        font-family: "Outfit", sans-serif;
        color: #ffffff;
        overflow: hidden;
      }
      .wrap { padding: 2px 2px 8px; }
      .scene {
        border-radius: 24px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 18px 30px -16px rgba(0, 0, 0, 0.7);
        background: #2a0410;
      }
      svg {
        display: block;
        width: 100%;
        height: auto;
        user-select: none;
        -webkit-user-select: none;
        -webkit-tap-highlight-color: transparent;
      }
      svg text {
        font-family: "Space Grotesk", "Outfit", sans-serif;
        pointer-events: none;
      }

      /* Clickable parts */
      .hit { cursor: pointer; outline: none; transition: filter 0.2s ease; }
      .hit:hover, .hit:focus-visible {
        filter: drop-shadow(0 0 7px rgba(253, 224, 71, 0.95)) brightness(1.05);
      }
      .menu-item:hover, .menu-item:focus-visible { filter: none; }
      .menu-item .row-bg { fill: transparent; transition: fill 0.2s ease; }
      .menu-item:hover .row-bg, .menu-item:focus-visible .row-bg { fill: rgba(253, 224, 71, 0.2); }
      .menu-item.is-picked .row-bg { fill: rgba(253, 224, 71, 0.32); }

      /* Pulsing markers that show what can be clicked */
      .hot { pointer-events: none; }
      .hot-dot { fill: #fde047; stroke: #4c0519; stroke-width: 1.5; }
      .hot-ring {
        fill: none;
        stroke: #fde047;
        stroke-width: 2.5;
        animation: hotPulse 1.8s ease-out infinite;
      }
      @keyframes hotPulse {
        0% { transform: scale(0.6); opacity: 0.95; }
        100% { transform: scale(2.6); opacity: 0; }
      }

      /* Night sky */
      .star { fill: #fff1f2; animation: twinkle 3.2s ease-in-out infinite; }
      @keyframes twinkle {
        0%, 100% { opacity: 0.25; }
        50% { opacity: 1; }
      }
      .bulb { animation: bulbGlow 2.6s ease-in-out infinite; }
      @keyframes bulbGlow {
        0%, 100% { opacity: 0.55; }
        50% { opacity: 1; }
      }

      /* Hatch */
      .shutter { transition: transform 0.65s cubic-bezier(0.22, 1, 0.36, 1); }
      .is-open .shutter { transform: translateY(-116px); }
      .awning {
        transform: scaleY(0.3);
        transition: transform 0.55s cubic-bezier(0.34, 1.4, 0.64, 1);
      }
      .is-open .awning { transform: scaleY(1); }
      .glow { opacity: 0; transition: opacity 0.5s ease; }
      .is-open .glow { opacity: 1; }
      .neon { fill: #fde047; opacity: 0.25; transition: opacity 0.4s ease 0.3s; }
      .is-open .neon { opacity: 1; filter: drop-shadow(0 0 4px #fde047); }
      .vendor {
        transform: translateY(84px);
        transition: transform 0.5s cubic-bezier(0.34, 1.3, 0.64, 1);
      }
      .is-open .vendor { transform: none; transition-delay: 0.25s; }
      .is-waving .arm { animation: wave 0.95s ease-in-out; }
      @keyframes wave {
        0%, 100% { transform: rotate(0deg); }
        25%, 75% { transform: rotate(-18deg); }
        50% { transform: rotate(10deg); }
      }
      .vent-steam circle { fill: #ffffff; opacity: 0; }
      .is-open .vent-steam circle { animation: puff 2.6s ease-out infinite; }
      @keyframes puff {
        0% { opacity: 0; transform: translate(0, 0); }
        25% { opacity: 0.5; }
        100% { opacity: 0; transform: translate(-16px, -44px); }
      }

      /* Food on the counter */
      .food { display: none; }
      .food.is-on { display: block; animation: serve 0.55s cubic-bezier(0.34, 1.5, 0.64, 1); }
      @keyframes serve {
        from { opacity: 0; transform: translateY(18px) scale(0.4); }
      }
      .steam path {
        fill: none;
        stroke: #ffffff;
        stroke-width: 3;
        stroke-linecap: round;
        opacity: 0;
      }
      .has-dish .steam path { animation: steam 2s ease-out infinite; }
      @keyframes steam {
        0% { opacity: 0; transform: translateY(6px); }
        30% { opacity: 0.75; }
        100% { opacity: 0; transform: translateY(-16px); }
      }

      /* Lights */
      .beam { opacity: 0; transition: opacity 0.3s ease; }
      .is-lit .beam { opacity: 1; }
      .lamp-glass { fill: #fef9c3; transition: fill 0.2s ease; }
      .is-lit .lamp-glass { fill: #fde047; filter: drop-shadow(0 0 8px #fde047); }
      .marker { fill: #9a3412; transition: fill 0.2s ease; }
      .is-lit .marker { fill: #fb923c; filter: drop-shadow(0 0 5px #fb923c); }
      .tail { fill: #7f1d1d; transition: fill 0.2s ease; }
      .is-lit .tail { fill: #ef4444; filter: drop-shadow(0 0 6px #ef4444); }
      .is-lit .sign { filter: drop-shadow(0 0 9px rgba(253, 224, 71, 0.85)); }

      /* Horn */
      .honk { opacity: 0; }
      .is-honking .honk { animation: honk 0.95s ease-out; }
      @keyframes honk {
        0% { opacity: 0; transform: scale(0.4); }
        18% { opacity: 1; transform: scale(1.12); }
        30% { transform: scale(1); }
        80% { opacity: 1; transform: scale(1); }
        100% { opacity: 0; transform: scale(1); }
      }
      .is-honking #rig { animation: jolt 0.4s ease-in-out; }
      @keyframes jolt {
        0%, 100% { transform: translateY(0); }
        25%, 75% { transform: translateY(-5px); }
        50% { transform: translateY(1px); }
      }

      /* Driving a lap: off to the right, back in from the left */
      .is-driving #truck { animation: lap 4.4s linear; }
      @keyframes lap {
        0% { transform: translateX(0); animation-timing-function: cubic-bezier(0.5, 0, 0.9, 0.5); }
        46% { transform: translateX(1100px); animation-timing-function: step-end; }
        46.01% { transform: translateX(-1000px); animation-timing-function: cubic-bezier(0.1, 0.6, 0.3, 1); }
        100% { transform: translateX(0); }
      }
      .is-driving .wheel-spin { animation: spin 0.45s linear infinite; }
      @keyframes spin { to { transform: rotate(360deg); } }
      .exhaust circle { fill: #e7e5e4; opacity: 0; }
      .is-driving .exhaust circle { animation: exhaust 0.7s ease-out infinite; }
      @keyframes exhaust {
        0% { opacity: 0.7; transform: translate(0, 0); }
        100% { opacity: 0; transform: translate(-46px, -12px); }
      }

      /* Controls under the scene */
      .bar, .chips {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.6rem;
        margin-top: 1rem;
      }
      .chips { display: none; margin-top: 0.6rem; }
      button {
        font-family: "Outfit", sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        padding: 0.6rem 1.15rem;
        border-radius: 999px;
        border: 1.5px solid rgba(255, 255, 255, 0.6);
        background: rgba(76, 5, 25, 0.4);
        color: #ffffff;
        cursor: pointer;
        transition: transform 0.2s ease, background 0.2s ease, color 0.2s ease,
                    border-color 0.2s ease;
      }
      button:hover:not(:disabled), button:focus-visible {
        background: #fde047;
        border-color: #fde047;
        color: #4c0519;
        transform: scale(1.05);
        outline: none;
      }
      button[aria-pressed="true"] {
        background: #fff1f2;
        border-color: #fff1f2;
        color: #9f1239;
      }
      button:disabled { opacity: 0.45; cursor: default; }
      .chips button { font-size: 0.85rem; padding: 0.45rem 0.9rem; }
      .status {
        text-align: center;
        margin: 0.9rem 0 0;
        min-height: 1.6em;
        font-size: 1rem;
        font-weight: 500;
        line-height: 1.5;
        color: #ffffff;
      }
      @media (max-width: 640px) {
        .chips { display: flex; }
        .scene { border-radius: 18px; }
      }
      @media (prefers-reduced-motion: reduce) {
        .star, .bulb, .hot-ring { animation: none; }
      }
    </style>

    <div class="wrap" id="wrap">
      <div class="scene" id="scene">
        <svg id="art" viewBox="0 0 1000 450" role="group" aria-label="Interactive LoadedBites GLA food truck">
          <defs>
            <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#22030c"/>
              <stop offset="0.6" stop-color="#560a21"/>
              <stop offset="1" stop-color="#7f1232"/>
            </linearGradient>
            <linearGradient id="paint" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#fffaf3"/>
              <stop offset="1" stop-color="#ffe2d2"/>
            </linearGradient>
            <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#cdeefd"/>
              <stop offset="1" stop-color="#5b9fc4"/>
            </linearGradient>
            <linearGradient id="beamFill" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0" stop-color="#fde047" stop-opacity="0.8"/>
              <stop offset="1" stop-color="#fde047" stop-opacity="0"/>
            </linearGradient>
            <linearGradient id="steel" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#fafaf9"/>
              <stop offset="1" stop-color="#a8a29e"/>
            </linearGradient>
            <radialGradient id="warm" cx="0.5" cy="0.35" r="0.75">
              <stop offset="0" stop-color="#fbbf24" stop-opacity="0.6"/>
              <stop offset="1" stop-color="#fbbf24" stop-opacity="0"/>
            </radialGradient>
            <radialGradient id="moonGlow" cx="0.5" cy="0.5" r="0.5">
              <stop offset="0.4" stop-color="#fde68a" stop-opacity="0.35"/>
              <stop offset="1" stop-color="#fde68a" stop-opacity="0"/>
            </radialGradient>
            <clipPath id="hatchClip">
              <rect x="330" y="150" width="270" height="112" rx="8"/>
            </clipPath>
          </defs>

          <!-- Sky, moon, rooftops -->
          <rect x="0" y="0" width="1000" height="450" fill="url(#sky)"/>
          <g id="stars"></g>
          <circle cx="905" cy="112" r="62" fill="url(#moonGlow)"/>
          <circle cx="905" cy="112" r="27" fill="#fde68a"/>
          <circle cx="896" cy="104" r="5" fill="#f5d36b"/>
          <circle cx="914" cy="121" r="3.5" fill="#f5d36b"/>
          <path d="M0 392 V318 H60 V300 H74 V318 H150 V290 H170 V270 H186 V290 H260 V322 H330 V306 H420 V280 H436 V306 H520 V326 H600 V296 H660 V276 H676 V296 H760 V316 H840 V288 H858 V316 H940 V300 H1000 V392 Z" fill="#33071a"/>
          <g fill="#fde047" opacity="0.55">
            <rect x="20" y="334" width="9" height="12"/>
            <rect x="104" y="340" width="9" height="12"/>
            <rect x="200" y="308" width="9" height="12"/>
            <rect x="224" y="340" width="9" height="12"/>
            <rect x="870" y="334" width="9" height="12"/>
            <rect x="900" y="352" width="9" height="12"/>
            <rect x="962" y="322" width="9" height="12"/>
          </g>

          <!-- String lights -->
          <path id="wire" d="M-10 20 Q245 78 500 30 Q755 78 1010 20" fill="none" stroke="#14020a" stroke-width="2.5"/>
          <g id="bulbs"></g>

          <!-- Ground -->
          <rect x="0" y="388" width="1000" height="62" fill="#1b0309"/>
          <rect x="0" y="388" width="1000" height="5" fill="#4c0519"/>
          <g fill="#ffffff" opacity="0.2">
            <rect x="30" y="428" width="64" height="5" rx="2.5"/>
            <rect x="180" y="428" width="64" height="5" rx="2.5"/>
            <rect x="330" y="428" width="64" height="5" rx="2.5"/>
            <rect x="480" y="428" width="64" height="5" rx="2.5"/>
            <rect x="630" y="428" width="64" height="5" rx="2.5"/>
            <rect x="780" y="428" width="64" height="5" rx="2.5"/>
            <rect x="930" y="428" width="64" height="5" rx="2.5"/>
          </g>

          <!-- The truck -->
          <g id="truck">
            <g id="rig">
              <ellipse cx="528" cy="407" rx="308" ry="9" fill="#000000" opacity="0.4"/>

              <g class="exhaust">
                <circle cx="224" cy="354" r="7"/>
                <circle cx="224" cy="354" r="5" style="animation-delay: 0.25s"/>
                <circle cx="224" cy="354" r="9" style="animation-delay: 0.45s"/>
              </g>

              <polygon class="beam" points="802,339 1010,290 1010,404" fill="url(#beamFill)"/>

              <!-- Chassis and bumpers -->
              <rect x="246" y="342" width="556" height="18" rx="6" fill="#1b0309"/>
              <rect x="226" y="340" width="26" height="14" rx="4" fill="url(#steel)" stroke="#4c0519" stroke-width="2"/>
              <rect x="784" y="348" width="32" height="14" rx="5" fill="url(#steel)" stroke="#4c0519" stroke-width="2"/>

              <!-- Kitchen box and cab -->
              <rect x="240" y="120" width="404" height="230" rx="18" fill="url(#paint)" stroke="#4c0519" stroke-width="3"/>
              <path d="M640 182 H714 Q738 182 750 202 L790 264 Q800 280 800 298 V350 H640 Z" fill="url(#paint)" stroke="#4c0519" stroke-width="3" stroke-linejoin="round"/>

              <!-- Paintwork -->
              <rect x="241.5" y="292" width="557" height="30" fill="#e11d48"/>
              <rect x="241.5" y="326" width="557" height="4" fill="#fde047"/>
              <text x="480" y="312" text-anchor="middle" font-size="13" font-weight="700" letter-spacing="3" fill="#fff1f2">FRESH · HOT · LOADED</text>

              <!-- Roof: rail, vent, sign -->
              <rect x="248" y="108" width="388" height="13" rx="6.5" fill="#be123c" stroke="#4c0519" stroke-width="2"/>
              <circle class="marker" cx="262" cy="114.5" r="3.5"/>
              <circle class="marker" cx="622" cy="114.5" r="3.5"/>
              <rect x="282" y="86" width="30" height="24" rx="3" fill="url(#steel)" stroke="#4c0519" stroke-width="2"/>
              <rect x="276" y="79" width="42" height="9" rx="4.5" fill="#78716c" stroke="#4c0519" stroke-width="2"/>
              <g class="vent-steam">
                <circle cx="297" cy="70" r="7"/>
                <circle cx="303" cy="66" r="5" style="animation-delay: 0.8s"/>
                <circle cx="292" cy="68" r="9" style="animation-delay: 1.6s"/>
              </g>
              <rect x="394" y="98" width="6" height="12" fill="#4c0519"/>
              <rect x="550" y="98" width="6" height="12" fill="#4c0519"/>
              <g class="sign">
                <rect x="368" y="56" width="214" height="46" rx="11" fill="#881337" stroke="#fde047" stroke-width="3"/>
                <text x="475" y="86" text-anchor="middle" font-size="20" font-weight="700" letter-spacing="-0.5" fill="#fde047">LoadedBites GLA</text>
              </g>

              <!-- Badge and vents on the side panel -->
              <circle cx="286" cy="198" r="27" fill="#be123c" stroke="#fde047" stroke-width="3"/>
              <text x="286" y="206" text-anchor="middle" font-size="22" font-weight="700" fill="#fde047">LB</text>
              <g fill="#e9c4b4">
                <rect x="266" y="246" width="40" height="4" rx="2"/>
                <rect x="266" y="256" width="40" height="4" rx="2"/>
                <rect x="266" y="266" width="40" height="4" rx="2"/>
              </g>
              <rect class="tail" x="237" y="298" width="8" height="20" rx="2"/>

              <!-- Serving hatch -->
              <g id="hatch" class="hit" role="button" tabindex="0" aria-label="Serving hatch">
                <rect x="324" y="144" width="282" height="124" rx="12" fill="#4c0519"/>
                <g clip-path="url(#hatchClip)">
                  <rect x="330" y="150" width="270" height="112" fill="#2a0410"/>
                  <rect class="glow" x="330" y="150" width="270" height="112" fill="url(#warm)"/>
                  <rect x="330" y="188" width="270" height="4" fill="#7c2d12"/>
                  <rect x="344" y="168" width="12" height="20" rx="2" fill="#fde047"/>
                  <rect x="360" y="174" width="12" height="14" rx="2" fill="#fb7185"/>
                  <rect x="376" y="166" width="10" height="22" rx="2" fill="#a3e635"/>
                  <rect x="390" y="176" width="14" height="12" rx="2" fill="#fdba74"/>
                  <text class="neon" x="548" y="180" text-anchor="middle" font-size="17" font-weight="700" letter-spacing="2">OPEN</text>

                  <g class="vendor">
                    <g class="arm" style="transform-origin: 468px 238px">
                      <path d="M468 238 L496 208" stroke="#fffaf3" stroke-width="12" stroke-linecap="round"/>
                      <circle cx="499" cy="204" r="7.5" fill="#e0a77e" stroke="#4c0519" stroke-width="1.5"/>
                    </g>
                    <path d="M404 264 V246 Q404 226 424 226 H456 Q476 226 476 246 V264 Z" fill="#fffaf3" stroke="#4c0519" stroke-width="2"/>
                    <path d="M422 264 V240 H458 V264 Z" fill="#e11d48"/>
                    <path d="M427 240 L432 227 M453 240 L448 227" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
                    <rect x="434" y="214" width="12" height="14" fill="#e0a77e"/>
                    <circle cx="440" cy="202" r="19" fill="#e0a77e" stroke="#4c0519" stroke-width="2"/>
                    <path d="M421 190 Q417 171 431 173 Q440 160 449 173 Q463 171 459 190 Z" fill="#ffffff" stroke="#4c0519" stroke-width="2" stroke-linejoin="round"/>
                    <rect x="420" y="186" width="40" height="8" rx="3" fill="#ffffff" stroke="#4c0519" stroke-width="2"/>
                    <circle cx="433" cy="204" r="2.3" fill="#2a0410"/>
                    <circle cx="447" cy="204" r="2.3" fill="#2a0410"/>
                    <path d="M432 211 Q440 218 448 211" fill="none" stroke="#2a0410" stroke-width="2" stroke-linecap="round"/>
                  </g>

                  <g class="shutter">
                    <rect x="330" y="150" width="270" height="112" fill="#be123c"/>
                    <path d="M330 164 H600 M330 178 H600 M330 192 H600 M330 206 H600 M330 220 H600 M330 234 H600 M330 248 H600" stroke="#9f1239" stroke-width="2"/>
                    <rect x="398" y="194" width="134" height="26" rx="6" fill="#be123c"/>
                    <text x="465" y="212" text-anchor="middle" font-size="15" font-weight="700" letter-spacing="4" fill="#fecdd3">CLOSED</text>
                    <rect x="445" y="247" width="40" height="7" rx="3.5" fill="#fde047"/>
                  </g>
                </g>
                <rect x="330" y="150" width="270" height="112" rx="8" fill="none" stroke="#4c0519" stroke-width="3"/>
              </g>

              <!-- Counter and the dish served on it -->
              <path d="M338 275 V290 L353 275 Z M592 275 V290 L577 275 Z" fill="#4c0519"/>
              <rect x="316" y="262" width="298" height="13" rx="4" fill="#881337" stroke="#4c0519" stroke-width="2"/>
              <g transform="translate(552 262)">
                <g class="steam">
                  <path d="M-10 -54 q-5 -7 0 -14 q5 -7 0 -14"/>
                  <path d="M0 -58 q-5 -7 0 -14 q5 -7 0 -14" style="animation-delay: 0.5s"/>
                  <path d="M10 -54 q-5 -7 0 -14 q5 -7 0 -14" style="animation-delay: 1s"/>
                </g>
                <g class="food" data-dish="wrap">
                  <path d="M-15 0 L-11 -42 Q0 -52 11 -42 L15 0 Z" fill="#ecc98f" stroke="#8a5a22" stroke-width="2" stroke-linejoin="round"/>
                  <circle cx="-5" cy="-44" r="4.5" fill="#65a30d"/>
                  <circle cx="3" cy="-46" r="4.5" fill="#dc2626"/>
                  <circle cx="8" cy="-42" r="3.5" fill="#facc15"/>
                  <path d="M-15 0 L-13 -22 L13 -22 L15 0 Z" fill="#fafaf9" stroke="#a8a29e" stroke-width="1.5" stroke-linejoin="round"/>
                  <path d="M-12 -12 H12" stroke="#e11d48" stroke-width="3"/>
                </g>
                <g class="food" data-dish="cheese">
                  <ellipse cx="0" cy="-4" rx="32" ry="6" fill="#fafaf9" stroke="#a8a29e" stroke-width="1.5"/>
                  <path d="M-24 -6 Q-22 -30 0 -32 Q22 -30 24 -6 Z" fill="#f59e0b" stroke="#92400e" stroke-width="2" stroke-linejoin="round"/>
                  <path d="M-18 -18 Q-16 -30 0 -31 Q16 -30 18 -18 Q13 -10 8 -18 Q3 -8 -3 -18 Q-9 -9 -18 -18 Z" fill="#fde047" stroke="#ca8a04" stroke-width="1.5" stroke-linejoin="round"/>
                  <path d="M-10 -26 Q-4 -22 2 -27 Q8 -22 13 -25" fill="none" stroke="#e11d48" stroke-width="2.5" stroke-linecap="round"/>
                  <circle cx="-7" cy="-21" r="1.8" fill="#4d7c0f"/>
                  <circle cx="6" cy="-20" r="1.8" fill="#4d7c0f"/>
                </g>
                <g class="food" data-dish="spiced">
                  <circle cx="-15" cy="-20" r="9" fill="#c2410c" stroke="#7c2d12" stroke-width="1.5"/>
                  <circle cx="0" cy="-24" r="9" fill="#ea580c" stroke="#7c2d12" stroke-width="1.5"/>
                  <circle cx="15" cy="-20" r="9" fill="#c2410c" stroke="#7c2d12" stroke-width="1.5"/>
                  <path d="M-27 0 L-31 -17 H31 L27 0 Z" fill="#fafaf9" stroke="#a8a29e" stroke-width="1.5" stroke-linejoin="round"/>
                  <path d="M-19 -17 L-17 0 M-6 -17 L-5 0 M6 -17 L5 0 M19 -17 L17 0" stroke="#e11d48" stroke-width="3"/>
                  <path d="M-4 -36 Q8 -44 18 -34" fill="none" stroke="#dc2626" stroke-width="5" stroke-linecap="round"/>
                  <path d="M-4 -36 L-9 -40" stroke="#4d7c0f" stroke-width="3" stroke-linecap="round"/>
                </g>
                <g class="food" data-dish="special">
                  <ellipse cx="0" cy="-4" rx="32" ry="6" fill="#fafaf9" stroke="#a8a29e" stroke-width="1.5"/>
                  <path d="M-26 -6 A26 25 0 0 1 26 -6 Z" fill="url(#steel)" stroke="#57534e" stroke-width="2" stroke-linejoin="round"/>
                  <circle cx="0" cy="-34" r="4.5" fill="url(#steel)" stroke="#57534e" stroke-width="2"/>
                  <path d="M-14 -22 Q-8 -28 0 -29" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
                  <path d="M20 -40 l2.5 6 6 2.5 -6 2.5 -2.5 6 -2.5 -6 -6 -2.5 6 -2.5 Z" fill="#fde047"/>
                </g>
              </g>

              <!-- Awning -->
              <rect x="316" y="123" width="298" height="8" rx="4" fill="#4c0519"/>
              <g class="awning hit" id="awning" style="transform-origin: 465px 129px"></g>

              <!-- Cab: window, door, mirror -->
              <g id="cab" class="hit" role="button" tabindex="0" aria-label="Cab horn">
                <rect x="646" y="188" width="132" height="100" fill="transparent"/>
                <path d="M656 198 H712 Q727 198 735 211 L765 262 H656 Z" fill="url(#glass)" stroke="#4c0519" stroke-width="3" stroke-linejoin="round"/>
                <path d="M670 252 L700 208" stroke="#ffffff" stroke-opacity="0.6" stroke-width="5" stroke-linecap="round"/>
                <path d="M686 254 L708 222" stroke="#ffffff" stroke-opacity="0.4" stroke-width="3" stroke-linecap="round"/>
                <rect x="664" y="275" width="24" height="6" rx="3" fill="#4c0519"/>
              </g>
              <path d="M650 190 V288 M778 270 V288" stroke="#4c0519" stroke-opacity="0.3" stroke-width="2"/>
              <path d="M766 238 H780" stroke="#4c0519" stroke-width="3"/>
              <rect x="778" y="226" width="9" height="24" rx="3" fill="#4c0519"/>
              <rect x="789" y="300" width="9" height="13" rx="2" fill="#fb923c" stroke="#4c0519" stroke-width="1.5"/>

              <!-- Headlight -->
              <g id="lamp" class="hit" role="button" tabindex="0" aria-label="Headlights">
                <circle cx="794" cy="339" r="20" fill="transparent"/>
                <rect class="lamp-glass" x="785" y="331" width="18" height="16" rx="5" stroke="#4c0519" stroke-width="2.5"/>
              </g>

              <!-- Wheel arches and wheels -->
              <path d="M280 350 A50 50 0 0 1 380 350 Z M676 350 A50 50 0 0 1 776 350 Z" fill="#1b0309" stroke="#4c0519" stroke-width="2"/>
              <g id="wheels"></g>

              <!-- Horn bubble -->
              <g transform="translate(742 134)">
                <g class="honk">
                  <path d="M-16 16 L-24 34 L4 16 Z" fill="#fde047" stroke="#4c0519" stroke-width="3" stroke-linejoin="round"/>
                  <rect x="-64" y="-22" width="128" height="40" rx="20" fill="#fde047" stroke="#4c0519" stroke-width="3"/>
                  <path d="M-14 16 L2 16" stroke="#fde047" stroke-width="4"/>
                  <text x="0" y="4" text-anchor="middle" font-size="16" font-weight="700" fill="#4c0519">BEEP BEEP!</text>
                </g>
              </g>

              <g id="rig-hots"></g>
            </g>
          </g>

          <!-- Menu board, in front of the road so the truck passes behind it -->
          <g id="board">
            <path d="M64 196 L46 404 M186 196 L204 404" stroke="#7c2d12" stroke-width="8" stroke-linecap="round"/>
            <rect x="44" y="176" width="162" height="200" rx="10" fill="#b45309" stroke="#4c0519" stroke-width="2"/>
            <rect x="52" y="184" width="146" height="184" rx="6" fill="#1c1215"/>
            <text x="125" y="211" text-anchor="middle" font-size="19" font-weight="700" letter-spacing="4" fill="#fde047">MENU</text>
            <path d="M84 219 H166" stroke="#fde047" stroke-opacity="0.6" stroke-width="2" stroke-linecap="round"/>
            <g id="menu-rows"></g>
            <text x="125" y="361" text-anchor="middle" font-size="9.5" font-weight="600" letter-spacing="1.5" fill="#fecdd3" opacity="0.85">SELECT TO ORDER</text>
            <g id="board-hots"></g>
          </g>
        </svg>
      </div>

      <div class="bar" role="group" aria-label="Truck controls">
        <button type="button" data-act="hatch" aria-pressed="false">Open hatch</button>
        <button type="button" data-act="lights" aria-pressed="false">Lights on</button>
        <button type="button" data-act="horn">Sound horn</button>
        <button type="button" data-act="lap">Take a lap</button>
      </div>
      <div class="chips" id="chips" role="group" aria-label="Order from the menu"></div>
      <p class="status" id="status" role="status"></p>
    </div>

    <script>
      (() => {
        const NS = "http://www.w3.org/2000/svg";
        const scene = document.getElementById("scene");
        const art = document.getElementById("art");
        const wrap = document.getElementById("wrap");
        const statusEl = document.getElementById("status");
        const truck = document.getElementById("truck");
        const $ = (id) => document.getElementById(id);

        const el = (name, attrs, parent) => {
          const node = document.createElementNS(NS, name);
          for (const key in attrs) node.setAttribute(key, attrs[key]);
          parent.appendChild(node);
          return node;
        };

        // Placeholder dish names — rename these to match the real menu.
        const DISHES = [
          { key: "wrap", name: "Loaded Wrap", note: "Seasoned protein with fresh contrast, wrapped warm." },
          { key: "cheese", name: "Cheese Plate", note: "Melted cheese over a crisp base with house sauce." },
          { key: "spiced", name: "Spiced Bites", note: "Gently spiced, for those who prefer more heat." },
          { key: "special", name: "Daily Special", note: "Changes with the season: sometimes smoked, sometimes sweet." },
        ];

        const state = { open: false, lit: false, busy: false };
        const say = (text) => { statusEl.textContent = text; };

        // ---------- Build the repeated parts of the drawing ----------
        [[40, 70], [95, 130], [150, 96], [215, 150], [290, 104], [345, 46], [610, 60], [655, 128],
         [700, 84], [775, 150], [820, 70], [965, 160], [985, 78], [470, 132], [560, 160], [20, 190]]
          .forEach(([cx, cy], i) => {
            el("circle", { class: "star", cx, cy, r: i % 3 === 0 ? 2 : 1.3, style: "animation-delay:" + (i * 0.37) % 3 + "s" }, $("stars"));
          });

        const wire = $("wire");
        const wireLength = wire.getTotalLength();
        const bulbColours = ["#fde047", "#fb7185", "#fff1f2"];
        for (let i = 1; i < 18; i++) {
          const p = wire.getPointAtLength((wireLength * i) / 18);
          el("line", { x1: p.x, y1: p.y, x2: p.x, y2: p.y + 6, stroke: "#14020a", "stroke-width": 2 }, $("bulbs"));
          el("circle", { class: "bulb", cx: p.x, cy: p.y + 10, r: 5, fill: bulbColours[i % 3], style: "animation-delay:" + (i % 5) * 0.4 + "s" }, $("bulbs"));
        }

        const stripes = 11;
        for (let i = 0; i < stripes; i++) {
          const t0 = (322 + (286 * i) / stripes).toFixed(1);
          const t1 = (322 + (286 * (i + 1)) / stripes).toFixed(1);
          const b0 = 304 + (322 * i) / stripes;
          const b1 = 304 + (322 * (i + 1)) / stripes;
          el("path", {
            d: "M" + t0 + " 129 L" + t1 + " 129 L" + b1.toFixed(1) + " 150 A" + ((b1 - b0) / 2).toFixed(1) + " 6 0 0 1 " + b0.toFixed(1) + " 150 Z",
            fill: i % 2 ? "#fff1f2" : "#e11d48",
            stroke: "#4c0519",
            "stroke-width": 1.5,
            "stroke-linejoin": "round",
          }, $("awning"));
        }

        const wheels = [];
        [[330, 364, "Rear wheel"], [726, 364, "Front wheel"]].forEach(([cx, cy, label]) => {
          const g = el("g", { class: "hit wheel", role: "button", tabindex: "0", "aria-label": label }, $("wheels"));
          const spin = el("g", { class: "wheel-spin", style: "transform-origin:" + cx + "px " + cy + "px" }, g);
          el("circle", { cx, cy, r: 42, fill: "#16030a", stroke: "#000000", "stroke-width": 2 }, spin);
          el("circle", { cx, cy, r: 37, fill: "none", stroke: "#40202a", "stroke-width": 5, "stroke-dasharray": "7 9" }, spin);
          el("circle", { cx, cy, r: 26, fill: "url(#steel)", stroke: "#57534e", "stroke-width": 3 }, spin);
          for (let i = 0; i < 5; i++) {
            const a = (i / 5) * Math.PI * 2;
            el("circle", { cx: (cx + Math.cos(a) * 15).toFixed(1), cy: (cy + Math.sin(a) * 15).toFixed(1), r: 4.2, fill: "#57534e" }, spin);
          }
          el("circle", { cx, cy, r: 7.5, fill: "#be123c", stroke: "#4c0519", "stroke-width": 2 }, spin);
          wheels.push(g);
        });

        const menuRows = {};
        DISHES.forEach((dish, i) => {
          const y = 226 + i * 31;
          const row = el("g", { class: "hit menu-item", role: "button", tabindex: "0", "aria-label": "Order " + dish.name }, $("menu-rows"));
          el("rect", { class: "row-bg", x: 58, y, width: 134, height: 28, rx: 6 }, row);
          el("circle", { cx: 71, cy: y + 14, r: 3.5, fill: "#fde047" }, row);
          const label = el("text", { x: 83, y: y + 19, "font-size": 14, "font-weight": 600, fill: "#fff1f2" }, row);
          label.textContent = dish.name;
          menuRows[dish.key] = row;

          const chip = document.createElement("button");
          chip.type = "button";
          chip.textContent = dish.name;
          chip.dataset.order = dish.key;
          $("chips").appendChild(chip);
        });

        const hots = {};
        [["hatch", 578, 170, "rig-hots"], ["horn", 706, 234, "rig-hots"], ["lights", 794, 339, "rig-hots"],
         ["lap", 726, 330, "rig-hots"], ["menu", 190, 192, "board-hots"]].forEach(([name, cx, cy, parent]) => {
          const g = el("g", { class: "hot" }, $(parent));
          el("circle", { class: "hot-ring", cx, cy, r: 9, style: "transform-origin:" + cx + "px " + cy + "px" }, g);
          el("circle", { class: "hot-dot", cx, cy, r: 4.5 }, g);
          hots[name] = g;
        });
        const used = (name) => {
          if (hots[name]) { hots[name].remove(); delete hots[name]; }
        };

        // ---------- Behaviour ----------
        const restart = (className) => {
          scene.classList.remove(className);
          void scene.offsetWidth;
          scene.classList.add(className);
        };

        const wave = () => restart("is-waving");

        let orderTimer;
        const clearDish = () => {
          clearTimeout(orderTimer);
          scene.classList.remove("has-dish");
          art.querySelectorAll(".food.is-on").forEach((f) => f.classList.remove("is-on"));
          Object.values(menuRows).forEach((row) => row.classList.remove("is-picked"));
        };

        const hatchButton = document.querySelector('[data-act="hatch"]');
        const lightsButton = document.querySelector('[data-act="lights"]');
        const setHatch = (open) => {
          state.open = open;
          scene.classList.toggle("is-open", open);
          hatchButton.setAttribute("aria-pressed", String(open));
          hatchButton.textContent = open ? "Close hatch" : "Open hatch";
          if (!open) clearDish();
        };

        const toggleHatch = () => {
          if (state.busy) return;
          used("hatch");
          setHatch(!state.open);
          if (state.open) {
            setTimeout(wave, 450);
            say("The hatch is open. Choose a dish from the menu.");
          } else {
            say("The hatch is closed.");
          }
        };

        const order = (key) => {
          if (state.busy) return;
          used("menu");
          used("hatch");
          const dish = DISHES.find((d) => d.key === key);
          const wait = state.open ? 0 : 700;
          if (!state.open) setHatch(true);
          clearDish();
          menuRows[key].classList.add("is-picked");
          say("Preparing your " + dish.name + "…");
          orderTimer = setTimeout(() => {
            art.querySelector('.food[data-dish="' + key + '"]').classList.add("is-on");
            scene.classList.add("has-dish");
            wave();
            say("Order up: " + dish.name + ". " + dish.note);
          }, wait + 350);
        };

        const toggleLights = () => {
          used("lights");
          state.lit = !state.lit;
          scene.classList.toggle("is-lit", state.lit);
          lightsButton.setAttribute("aria-pressed", String(state.lit));
          lightsButton.textContent = state.lit ? "Lights off" : "Lights on";
          say(state.lit ? "Headlights on." : "Headlights off.");
        };

        let audio;
        const beep = () => {
          try {
            audio = audio || new (window.AudioContext || window.webkitAudioContext)();
            const now = audio.currentTime;
            [0, 0.24].forEach((offset) => {
              [370, 466].forEach((freq) => {
                const osc = audio.createOscillator();
                const gain = audio.createGain();
                osc.type = "triangle";
                osc.frequency.value = freq;
                gain.gain.setValueAtTime(0.0001, now + offset);
                gain.gain.exponentialRampToValueAtTime(0.05, now + offset + 0.02);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + offset + 0.18);
                osc.connect(gain).connect(audio.destination);
                osc.start(now + offset);
                osc.stop(now + offset + 0.2);
              });
            });
          } catch (err) {}
        };

        let honkTimer;
        const honk = () => {
          used("horn");
          restart("is-honking");
          clearTimeout(honkTimer);
          honkTimer = setTimeout(() => scene.classList.remove("is-honking"), 1000);
          beep();
          if (!state.busy) say("Beep beep!");
        };

        const lapButtons = document.querySelectorAll('[data-act="hatch"], [data-act="lap"], #chips button');
        let lapTimer;
        const endLap = () => {
          if (!state.busy) return;
          clearTimeout(lapTimer);
          scene.classList.remove("is-driving");
          state.busy = false;
          lapButtons.forEach((b) => { b.disabled = false; });
          say("Parked and ready to serve.");
        };
        const lap = () => {
          if (state.busy) return;
          used("lap");
          const wait = state.open ? 600 : 0;
          setHatch(false);
          state.busy = true;
          lapButtons.forEach((b) => { b.disabled = true; });
          say("Off for a quick lap of the block…");
          setTimeout(() => scene.classList.add("is-driving"), wait);
          lapTimer = setTimeout(endLap, wait + 5200);
        };
        truck.addEventListener("animationend", (event) => {
          if (event.animationName === "lap") endLap();
        });

        // ---------- Wiring ----------
        const bind = (node, action) => {
          node.addEventListener("click", action);
          node.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") {
              event.preventDefault();
              action();
            }
          });
        };
        bind($("hatch"), toggleHatch);
        bind($("awning"), toggleHatch);
        bind($("cab"), honk);
        bind($("lamp"), toggleLights);
        wheels.forEach((w) => bind(w, lap));
        DISHES.forEach((dish) => bind(menuRows[dish.key], () => order(dish.key)));

        const actions = { hatch: toggleHatch, lights: toggleLights, horn: honk, lap };
        document.querySelectorAll("[data-act]").forEach((button) => {
          button.addEventListener("click", actions[button.dataset.act]);
        });
        document.querySelectorAll("[data-order]").forEach((button) => {
          button.addEventListener("click", () => order(button.dataset.order));
        });

        // On small screens, zoom in on the truck; the menu moves to the buttons below.
        const small = window.matchMedia("(max-width: 640px)");
        const frame = () => art.setAttribute("viewBox", small.matches ? "205 14 630 436" : "0 0 1000 450");
        small.addEventListener("change", frame);
        frame();

        // Keep this frame exactly as tall as its content.
        const fit = () => {
          try {
            window.frameElement.style.height = Math.ceil(wrap.getBoundingClientRect().height) + "px";
          } catch (err) {}
        };
        new ResizeObserver(fit).observe(wrap);
        fit();

        say("Select the hatch to open up, or choose a dish from the menu.");
      })();
    </script>
    """,
    height=640,
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
c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    show_html(
        """
        <div class="ft-card">
          <h3>Business lunch</h3>
          <p>Efficient service for a limited break, without sacrificing quality.</p>
        </div>
        """
    )
with c2:
    show_html(
        """
        <div class="ft-card">
          <h3>Evening dining</h3>
          <p>A substantial, well-prepared option before or after your evening plans.</p>
        </div>
        """
    )
with c3:
    show_html(
        """
        <div class="ft-card">
          <h3>Groups &amp; families</h3>
          <p>Straightforward ordering for shared meals, with options to suit a range of tastes.</p>
        </div>
        """
    )

# --- CTA ---
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
