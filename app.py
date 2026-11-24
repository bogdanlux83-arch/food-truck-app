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
        background:
          radial-gradient(900px 480px at 50% -10%, rgba(253, 224, 71, 0.12), transparent 55%),
          radial-gradient(700px 420px at 100% 40%, rgba(76, 5, 25, 0.55), transparent 50%),
          radial-gradient(600px 380px at 0% 80%, rgba(136, 19, 55, 0.65), transparent 48%),
          var(--ft-red);
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
show_html('<p class="ft-section" id="truck">Our food truck</p>')
show_html(
    """
    <p class="ft-lead">
      Scroll to watch it arrive. Then open the hatch, order from the menu, switch
      the headlights, sound the horn, or send it for a lap of the block.
    </p>
    """
)

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Outfit:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
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
        border: 1px solid rgba(255, 255, 255, 0.22);
        box-shadow:
          0 28px 60px -20px rgba(0, 0, 0, 0.85),
          0 0 0 1px rgba(0, 0, 0, 0.35) inset;
        background: #0a1228;
        transition: opacity 1s ease, transform 1.1s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.8s ease;
      }
      .bar, .chips, .status { transition: opacity 0.7s ease 0.65s, transform 0.7s ease 0.65s; }

      /* Before the section scrolls into view: scene hidden, truck parked off-screen */
      .pre .scene {
        opacity: 0;
        transform: translateY(56px) scale(0.97);
        box-shadow: 0 8px 20px -16px rgba(0, 0, 0, 0.4);
      }
      .pre .bar, .pre .chips, .pre .status {
        opacity: 0;
        transform: translateY(18px);
      }
      .pre #truck { transform: translateX(-1120px); }

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
      svg text.chalk { font-family: "Caveat", "Outfit", cursive; }

      /* Clickable parts */
      .hit { cursor: pointer; outline: none; transition: filter 0.2s ease; }
      .hit:hover, .hit:focus-visible {
        filter: drop-shadow(0 0 5px rgba(255, 226, 140, 0.9)) brightness(1.04);
      }
      .menu-item:hover, .menu-item:focus-visible { filter: none; }
      .menu-item .row-bg { fill: transparent; transition: fill 0.2s ease; }
      .menu-item:hover .row-bg, .menu-item:focus-visible .row-bg { fill: rgba(255, 255, 255, 0.1); }
      .menu-item.is-picked .row-bg { fill: rgba(255, 226, 140, 0.22); }

      /* Small markers that show what can be clicked */
      .hot { pointer-events: none; }
      .hot-dot { fill: #ffe28c; stroke: #2b2622; stroke-width: 1; }
      .hot-ring {
        fill: none;
        stroke: #ffe28c;
        stroke-width: 2;
        animation: hotPulse 1.9s ease-out infinite;
      }
      @keyframes hotPulse {
        0% { transform: scale(0.6); opacity: 0.9; }
        100% { transform: scale(2.4); opacity: 0; }
      }

      /* Sky and street lighting */
      .star { fill: #ffffff; animation: twinkle 3.4s ease-in-out infinite; }
      @keyframes twinkle {
        0%, 100% { opacity: 0.2; }
        50% { opacity: 0.8; }
      }
      .bulb-halo { animation: bulbGlow 3s ease-in-out infinite; }
      @keyframes bulbGlow {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.55; }
      }

      /* Hatch: the flap is hinged at the top and swings up to become the canopy */
      .flap { transition: transform 0.75s cubic-bezier(0.3, 0.1, 0.2, 1); }
      .is-open .flap { transform: scale(1.035, -0.3); }
      .flap-out { transition: opacity 0.1s linear 0.1s; }
      .is-open .flap-out { opacity: 0; transition: opacity 0.1s linear 0.42s; }
      .struts { opacity: 0; transition: opacity 0.25s ease; }
      .is-open .struts { opacity: 1; transition-delay: 0.55s; }
      .led { opacity: 0.3; transition: opacity 0.4s ease 0.3s; }
      .is-open .led { opacity: 1; filter: drop-shadow(0 0 3px #ffe7a8); }
      .pool { opacity: 0; transition: opacity 0.6s ease 0.3s; }
      .is-open .pool { opacity: 1; }
      .condiments { opacity: 0; transition: opacity 0.2s ease; }
      .is-open .condiments { opacity: 1; transition: opacity 0.3s ease 0.6s; }
      .neon {
        fill: none;
        stroke: #ff7a8e;
        stroke-width: 1.2;
        filter: drop-shadow(0 0 2px #ff4d6d) drop-shadow(0 0 5px #ff4d6d);
      }
      .vendor {
        transform: translateY(90px);
        transition: transform 0.5s cubic-bezier(0.34, 1.3, 0.64, 1);
      }
      .is-open .vendor { transform: none; transition-delay: 0.45s; }
      .is-waving .arm { animation: wave 0.95s ease-in-out; }
      @keyframes wave {
        0%, 100% { transform: rotate(0deg); }
        25%, 75% { transform: rotate(-16deg); }
        50% { transform: rotate(9deg); }
      }
      .vent-steam circle { fill: #ffffff; opacity: 0; }
      .is-open .vent-steam circle { animation: puff 3s ease-out infinite; }
      @keyframes puff {
        0% { opacity: 0; transform: translate(0, 0); }
        25% { opacity: 0.35; }
        100% { opacity: 0; transform: translate(-18px, -46px); }
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
      .has-dish .steam path { animation: steam 2.2s ease-out infinite; }
      @keyframes steam {
        0% { opacity: 0; transform: translateY(6px); }
        30% { opacity: 0.55; }
        100% { opacity: 0; transform: translateY(-16px); }
      }

      /* Lights */
      .beam { opacity: 0; transition: opacity 0.3s ease; }
      .is-lit .beam { opacity: 1; }
      .lamp-glass { fill: #cfd6dd; transition: fill 0.2s ease; }
      .is-lit .lamp-glass { fill: #fff6d6; }
      .lamp-halo { opacity: 0; transition: opacity 0.25s ease; }
      .is-lit .lamp-halo { opacity: 1; }
      .marker, .indicator { fill: #8a4b12; transition: fill 0.2s ease; }
      .is-lit .marker { fill: #ffab3d; filter: drop-shadow(0 0 4px #ff9a1f); }
      .tail { fill: #7a1818; transition: fill 0.2s ease; }
      .is-lit .tail { fill: #ff3b30; filter: drop-shadow(0 0 5px #ff3b30); }
      .sign-halo { opacity: 0; transition: opacity 0.3s ease; }
      .is-lit .sign-halo { opacity: 0.6; }
      .sign-face { transition: filter 0.3s ease; }
      .is-lit .sign-face { filter: brightness(1.75) saturate(1.15); }
      .sign-text { fill: #f1d27c; transition: fill 0.3s ease; }
      .is-lit .sign-text { fill: #fff6d6; }

      /* Horn: sound waves from the front and a flash of the indicators */
      .honk path { opacity: 0; }
      .is-honking .honk path { animation: hornWave 0.45s ease-out 2; }
      .is-honking .honk path:nth-child(2) { animation-delay: 0.07s; }
      .is-honking .honk path:nth-child(3) { animation-delay: 0.14s; }
      @keyframes hornWave {
        0% { opacity: 0; }
        30% { opacity: 1; }
        100% { opacity: 0; }
      }
      .is-honking .indicator { animation: hazard 0.45s steps(1, end) 2; }
      @keyframes hazard {
        0%, 100% { fill: #8a4b12; }
        15%, 60% { fill: #ffab3d; }
      }
      .is-honking #rig { animation: jolt 0.4s ease-in-out; }
      @keyframes jolt {
        0%, 100% { transform: translateY(0); }
        25%, 75% { transform: translateY(-3px); }
        50% { transform: translateY(1px); }
      }

      /* Arriving: the truck drives in and parks the first time the section is seen */
      .is-arriving #truck { animation: arrive 3.1s cubic-bezier(0.12, 0.82, 0.18, 1) 0.35s backwards; }
      @keyframes arrive {
        0% { transform: translateX(-1120px); }
        78% { transform: translateX(18px); }
        90% { transform: translateX(-6px); }
        100% { transform: translateX(0); }
      }
      .is-arriving .wheel-spin { animation: arriveSpin 3.1s cubic-bezier(0.12, 0.82, 0.18, 1) 0.35s backwards; }
      @keyframes arriveSpin {
        0% { transform: rotate(-1680deg); }
        100% { transform: rotate(0deg); }
      }
      .is-arriving #rig { animation: settle 0.55s ease-out 3.2s backwards; }
      @keyframes settle {
        0% { transform: translateY(0); }
        40% { transform: translateY(3px); }
        100% { transform: translateY(0); }
      }

      /* Driving a lap: off to the right, back in from the left */
      .is-driving #truck { animation: lap 4.4s linear; }
      @keyframes lap {
        0% { transform: translateX(0); animation-timing-function: cubic-bezier(0.5, 0, 0.9, 0.5); }
        46% { transform: translateX(1100px); animation-timing-function: step-end; }
        46.01% { transform: translateX(-1080px); animation-timing-function: cubic-bezier(0.1, 0.6, 0.3, 1); }
        100% { transform: translateX(0); }
      }
      .is-driving .wheel-spin { animation: lapSpin 4.4s linear; }
      @keyframes lapSpin {
        0% { transform: rotate(0deg); animation-timing-function: cubic-bezier(0.5, 0, 0.9, 0.5); }
        46% { transform: rotate(1440deg); animation-timing-function: step-end; }
        46.01% { transform: rotate(1440deg); animation-timing-function: cubic-bezier(0.1, 0.6, 0.3, 1); }
        100% { transform: rotate(2880deg); }
      }
      .exhaust circle { fill: #d8dade; opacity: 0; }
      .is-driving .exhaust circle, .is-arriving .exhaust circle { animation: exhaust 0.8s ease-out infinite; }
      @keyframes exhaust {
        0% { opacity: 0.45; transform: translate(0, 0); }
        100% { opacity: 0; transform: translate(-50px, -12px); }
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
        padding: 0.65rem 1.2rem;
        border-radius: 999px;
        border: 1.5px solid rgba(255, 255, 255, 0.55);
        background: rgba(20, 8, 14, 0.45);
        color: #ffffff;
        cursor: pointer;
        backdrop-filter: blur(6px);
        box-shadow: 0 8px 18px rgba(0, 0, 0, 0.22);
        transition: transform 0.2s ease, background 0.2s ease, color 0.2s ease,
                    border-color 0.2s ease, box-shadow 0.2s ease;
      }
      button:hover:not(:disabled), button:focus-visible {
        background: #fde047;
        box-shadow: 0 10px 22px rgba(0, 0, 0, 0.28);
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
        margin: 0.95rem 0 0;
        min-height: 1.6em;
        font-size: 1.02rem;
        font-weight: 500;
        letter-spacing: -0.01em;
        line-height: 1.5;
        color: #ffffff;
        text-shadow: 0 1px 8px rgba(0, 0, 0, 0.25);
      }
      @media (max-width: 640px) {
        .chips { display: flex; }
        .scene { border-radius: 16px; }
      }
      @media (prefers-reduced-motion: reduce) {
        .star, .bulb-halo, .hot-ring { animation: none; }
      }
    </style>

    <div class="wrap pre" id="wrap">
      <div class="scene" id="scene">
        <svg id="art" viewBox="0 0 1000 470" role="group" aria-label="Interactive LoadedBites GLA food truck parked on a Bath street at dusk">
          <defs>
            <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#060b1c"/>
              <stop offset="0.28" stop-color="#141a3a"/>
              <stop offset="0.52" stop-color="#2a2758"/>
              <stop offset="0.72" stop-color="#7a3d5e"/>
              <stop offset="0.88" stop-color="#c96a4e"/>
              <stop offset="1" stop-color="#e8a06a"/>
            </linearGradient>
            <linearGradient id="paint" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#fffcf7"/>
              <stop offset="0.22" stop-color="#f5efe6"/>
              <stop offset="0.55" stop-color="#e4dbcf"/>
              <stop offset="0.82" stop-color="#cfc4b4"/>
              <stop offset="1" stop-color="#b8ad9c"/>
            </linearGradient>
            <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
              <stop offset="0.28" stop-color="#ffffff" stop-opacity="0"/>
              <stop offset="0.38" stop-color="#ffffff" stop-opacity="0.38"/>
              <stop offset="0.46" stop-color="#ffffff" stop-opacity="0.08"/>
              <stop offset="0.72" stop-color="#ffffff" stop-opacity="0"/>
              <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
            </linearGradient>
            <linearGradient id="wetRoad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#4a4d55"/>
              <stop offset="0.35" stop-color="#2e3036"/>
              <stop offset="0.7" stop-color="#1c1e22"/>
              <stop offset="1" stop-color="#121316"/>
            </linearGradient>
            <linearGradient id="roadShine" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
              <stop offset="0.35" stop-color="#ffe2b0" stop-opacity="0.14"/>
              <stop offset="0.55" stop-color="#ffffff" stop-opacity="0.22"/>
              <stop offset="0.75" stop-color="#ffcf70" stop-opacity="0.12"/>
              <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
            </linearGradient>
            <radialGradient id="haze" cx="0.5" cy="1" r="0.85">
              <stop offset="0" stop-color="#e8a06a" stop-opacity="0.45"/>
              <stop offset="0.45" stop-color="#7a3d5e" stop-opacity="0.18"/>
              <stop offset="1" stop-color="#141a3a" stop-opacity="0"/>
            </radialGradient>
            <linearGradient id="edgeShade" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0" stop-color="#000000" stop-opacity="0.16"/>
              <stop offset="0.06" stop-color="#000000" stop-opacity="0"/>
              <stop offset="0.94" stop-color="#000000" stop-opacity="0"/>
              <stop offset="1" stop-color="#000000" stop-opacity="0.12"/>
            </linearGradient>
            <linearGradient id="alu" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#f6f7f8"/>
              <stop offset="0.5" stop-color="#b4b9bf"/>
              <stop offset="1" stop-color="#7a8087"/>
            </linearGradient>
            <linearGradient id="aluV" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0" stop-color="#8b9198"/>
              <stop offset="0.45" stop-color="#f1f2f4"/>
              <stop offset="1" stop-color="#8b9198"/>
            </linearGradient>
            <linearGradient id="rose" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#da2150"/>
              <stop offset="1" stop-color="#a51337"/>
            </linearGradient>
            <linearGradient id="signFace" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#7d1431"/>
              <stop offset="1" stop-color="#560c20"/>
            </linearGradient>
            <linearGradient id="glass" x1="0" y1="0" x2="0.55" y2="1">
              <stop offset="0" stop-color="#9bb8cf"/>
              <stop offset="0.25" stop-color="#5a7a96"/>
              <stop offset="0.55" stop-color="#24384c"/>
              <stop offset="1" stop-color="#0c121c"/>
            </linearGradient>
            <linearGradient id="glassReflect" x1="0" y1="0" x2="1" y2="0.4">
              <stop offset="0" stop-color="#ffffff" stop-opacity="0.45"/>
              <stop offset="0.35" stop-color="#ffffff" stop-opacity="0.12"/>
              <stop offset="0.7" stop-color="#e8a06a" stop-opacity="0.1"/>
              <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
            </linearGradient>
            <radialGradient id="tyre" cx="0.5" cy="0.5" r="0.5">
              <stop offset="0.6" stop-color="#2f2f33"/>
              <stop offset="0.86" stop-color="#18181b"/>
              <stop offset="1" stop-color="#070708"/>
            </radialGradient>
            <radialGradient id="rim" cx="0.42" cy="0.36" r="0.7">
              <stop offset="0" stop-color="#fbfcfd"/>
              <stop offset="0.55" stop-color="#b9bec4"/>
              <stop offset="1" stop-color="#676d74"/>
            </radialGradient>
            <radialGradient id="skin" cx="0.45" cy="0.4" r="0.65">
              <stop offset="0" stop-color="#ecbd99"/>
              <stop offset="1" stop-color="#bf8562"/>
            </radialGradient>
            <linearGradient id="interior" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#dccdb0"/>
              <stop offset="1" stop-color="#8d8070"/>
            </linearGradient>
            <linearGradient id="hood" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#8e949b"/>
              <stop offset="1" stop-color="#555a60"/>
            </linearGradient>
            <linearGradient id="flapIn" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#fdeccb"/>
              <stop offset="1" stop-color="#b7b0a4"/>
            </linearGradient>
            <radialGradient id="warm" cx="0.5" cy="0.2" r="0.8">
              <stop offset="0" stop-color="#ffc867" stop-opacity="0.5"/>
              <stop offset="1" stop-color="#ffc867" stop-opacity="0"/>
            </radialGradient>
            <linearGradient id="wood" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0" stop-color="#8d5c2f"/>
              <stop offset="0.5" stop-color="#a56d3a"/>
              <stop offset="1" stop-color="#6c4320"/>
            </linearGradient>
            <linearGradient id="slate" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#30353a"/>
              <stop offset="1" stop-color="#181a1c"/>
            </linearGradient>
            <linearGradient id="asphalt" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#4a4d55"/>
              <stop offset="0.4" stop-color="#2e3036"/>
              <stop offset="1" stop-color="#16181c"/>
            </linearGradient>
            <linearGradient id="slab" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#8d877e"/>
              <stop offset="1" stop-color="#57524c"/>
            </linearGradient>
            <linearGradient id="kerb" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#b3ada3"/>
              <stop offset="1" stop-color="#7a746b"/>
            </linearGradient>
            <linearGradient id="litWin" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#ffe6ad"/>
              <stop offset="1" stop-color="#eda34a"/>
            </linearGradient>
            <linearGradient id="darkWin" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#3d4a68"/>
              <stop offset="1" stop-color="#121829"/>
            </linearGradient>
            <linearGradient id="beamFill" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0" stop-color="#fff1c2" stop-opacity="0.75"/>
              <stop offset="1" stop-color="#fff1c2" stop-opacity="0"/>
            </linearGradient>
            <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
              <stop offset="0" stop-color="#fff0c4" stop-opacity="0.95"/>
              <stop offset="0.35" stop-color="#ffcf70" stop-opacity="0.45"/>
              <stop offset="1" stop-color="#ffb347" stop-opacity="0"/>
            </radialGradient>
            <radialGradient id="vignette" cx="0.5" cy="0.48" r="0.75">
              <stop offset="0.55" stop-color="#050814" stop-opacity="0"/>
              <stop offset="1" stop-color="#050814" stop-opacity="0.6"/>
            </radialGradient>
            <pattern id="rail" width="7" height="20" patternUnits="userSpaceOnUse">
              <rect x="3" y="2" width="1.3" height="18" fill="#101217"/>
              <circle cx="3.65" cy="1.8" r="1.5" fill="#101217"/>
            </pattern>
            <filter id="soft" x="-30%" y="-80%" width="160%" height="260%">
              <feGaussianBlur stdDeviation="5"/>
            </filter>
            <filter id="soft2" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="2.2"/>
            </filter>
            <filter id="far" x="-2%" y="-2%" width="104%" height="104%">
              <feGaussianBlur stdDeviation="0.55"/>
            </filter>
            <filter id="grain" x="0" y="0" width="100%" height="100%">
              <feTurbulence type="fractalNoise" baseFrequency="1.15" numOctaves="2" seed="7"/>
              <feColorMatrix type="matrix" values="0 0 0 0 0.55  0 0 0 0 0.55  0 0 0 0 0.55  0.9 0.9 0.9 0 -0.8"/>
            </filter>
            <clipPath id="hatchClip">
              <rect x="330" y="150" width="270" height="112" rx="2"/>
            </clipPath>
          </defs>

          <!-- Dusk sky -->
          <rect x="0" y="0" width="1000" height="366" fill="url(#sky)"/>
          <rect x="0" y="80" width="1000" height="286" fill="url(#haze)"/>
          <g id="stars"></g>
          <g filter="url(#soft)" opacity="0.55">
            <ellipse cx="280" cy="96" rx="150" ry="14" fill="#9a6a88"/>
            <ellipse cx="640" cy="78" rx="170" ry="12" fill="#7a5687"/>
            <ellipse cx="110" cy="118" rx="120" ry="10" fill="#b07080"/>
            <ellipse cx="880" cy="110" rx="100" ry="9" fill="#c08070"/>
          </g>
          <circle cx="770" cy="92" r="48" fill="url(#halo)" opacity="0.55"/>
          <circle cx="770" cy="92" r="14" fill="#fff6e0"/>
          <circle cx="766" cy="88" r="2.4" fill="#e8dcc0" opacity="0.7"/>
          <circle cx="775" cy="97" r="1.8" fill="#e8dcc0" opacity="0.55"/>

          <!-- Stone terraces, railings, tree -->
          <g id="town" filter="url(#far)"></g>
          <rect x="0" y="100" width="1000" height="252" fill="#151a3a" opacity="0.22"/>
          <g id="tree" filter="url(#far)">
            <path d="M108 352 C110 320 106 290 114 250 L124 250 C122 290 126 320 124 352 Z" fill="#231b16"/>
            <circle cx="96" cy="214" r="46" fill="#15211b"/>
            <circle cx="142" cy="196" r="52" fill="#15211b"/>
            <circle cx="70" cy="176" r="40" fill="#18261e"/>
            <circle cx="120" cy="158" r="48" fill="#18261e"/>
            <circle cx="164" cy="234" r="36" fill="#131d18"/>
            <circle cx="44" cy="228" r="34" fill="#131d18"/>
            <circle cx="108" cy="150" r="26" fill="#22362a"/>
            <circle cx="150" cy="176" r="22" fill="#22362a"/>
            <circle cx="72" cy="190" r="20" fill="#1f3126"/>
            <circle cx="132" cy="216" r="18" fill="#1f3126"/>
          </g>
          <rect x="0" y="333" width="1000" height="19" fill="url(#rail)"/>
          <rect x="0" y="336" width="1000" height="1.6" fill="#101217"/>

          <!-- Far pavement and street lamp -->
          <rect x="0" y="352" width="1000" height="14" fill="#6d6861"/>
          <rect x="0" y="352" width="1000" height="1.5" fill="#928b81"/>
          <rect x="0" y="364" width="1000" height="2.5" fill="#3f3c38"/>
          <g id="streetlamp">
            <ellipse cx="915" cy="368" rx="95" ry="10" fill="#ffcf70" opacity="0.28" filter="url(#soft)"/>
            <circle cx="915" cy="148" r="85" fill="url(#halo)" opacity="0.8"/>
            <rect x="912.5" y="172" width="5" height="190" fill="#14161a"/>
            <rect x="908" y="340" width="14" height="22" rx="2" fill="#14161a"/>
            <rect x="901" y="196" width="28" height="2.5" rx="1" fill="#14161a"/>
            <path d="M905 170 L901 142 H929 L925 170 Z" fill="#fff0c4" stroke="#14161a" stroke-width="2" stroke-linejoin="round"/>
            <path d="M915 142 V170" stroke="#14161a" stroke-width="1.2"/>
            <path d="M897 142 H933 L924 132 H906 Z" fill="#14161a"/>
            <rect x="913" y="124" width="4" height="9" fill="#14161a"/>
            <circle cx="915" cy="123" r="2.6" fill="#14161a"/>
          </g>

          <!-- Wet road with dusk reflection -->
          <rect x="0" y="366" width="1000" height="40" fill="url(#wetRoad)"/>
          <rect x="0" y="372" width="1000" height="10" fill="url(#roadShine)"/>
          <ellipse cx="465" cy="384" rx="220" ry="6" fill="#ffe2b0" opacity="0.12" filter="url(#soft)"/>
          <ellipse cx="900" cy="386" rx="90" ry="5" fill="#ffcf70" opacity="0.18" filter="url(#soft)"/>

          <!-- Festoon lights -->
          <path id="wire" d="M-10 22 Q245 80 500 32 Q755 80 1010 22" fill="none" stroke="#0a0c12" stroke-width="1.6"/>
          <g id="bulbs"></g>

          <!-- The truck -->
          <g id="truck">
            <g id="rig">
              <ellipse cx="525" cy="396" rx="320" ry="11" fill="#000000" opacity="0.72" filter="url(#soft)"/>
              <ellipse cx="525" cy="394" rx="260" ry="4" fill="#000000" opacity="0.35"/>

              <g class="exhaust" filter="url(#soft2)">
                <circle cx="226" cy="362" r="7"/>
                <circle cx="226" cy="362" r="5" style="animation-delay: 0.27s"/>
                <circle cx="226" cy="362" r="9" style="animation-delay: 0.53s"/>
              </g>

              <g class="beam">
                <polygon points="806,292 1010,246 1010,398 806,312" fill="url(#beamFill)" filter="url(#soft)"/>
                <ellipse cx="905" cy="390" rx="110" ry="6" fill="#ffe9ad" opacity="0.35" filter="url(#soft)"/>
              </g>

              <!-- Underbody: frame, step, locker, side guard, mud flaps -->
              <rect x="250" y="342" width="540" height="12" fill="#131416"/>
              <rect x="222" y="344" width="30" height="9" rx="2" fill="url(#alu)" stroke="#4a4f55" stroke-width="0.8"/>
              <rect x="396" y="350" width="86" height="26" rx="3" fill="#25272b" stroke="#0e0f10" stroke-width="1"/>
              <path d="M404 357 H474 M404 362 H474 M404 367 H474" stroke="#0e0f10" stroke-width="1.5"/>
              <rect x="436" y="371" width="8" height="2.5" rx="1" fill="#8b9198"/>
              <rect x="520" y="352" width="4" height="12" fill="#131416"/>
              <rect x="640" y="352" width="4" height="12" fill="#131416"/>
              <rect x="488" y="361" width="188" height="5" rx="2.5" fill="url(#alu)"/>
              <rect x="280" y="352" width="5" height="42" fill="#0e0f10"/>
              <rect x="676" y="352" width="5" height="42" fill="#0e0f10"/>

              <!-- Box body -->
              <rect x="236" y="118" width="408" height="230" rx="7" fill="url(#paint)" stroke="#2b2622" stroke-width="1.2"/>
              <rect x="236" y="118" width="408" height="230" rx="7" fill="url(#edgeShade)"/>
              <rect x="236" y="118" width="408" height="230" rx="7" fill="url(#sheen)"/>
              <path d="M322 126 V341 M608 126 V341" stroke="#000000" stroke-opacity="0.22" stroke-width="1"/>
              <path d="M323.2 126 V341 M609.2 126 V341" stroke="#ffffff" stroke-opacity="0.55" stroke-width="0.8"/>
              <path d="M250 128 H420" stroke="#ffffff" stroke-opacity="0.35" stroke-width="1.4" stroke-linecap="round"/>
              <path d="M255 340 H430" stroke="#000000" stroke-opacity="0.18" stroke-width="2" stroke-linecap="round"/>
              <!-- Subtle wear near the arches -->
              <ellipse cx="330" cy="340" rx="48" ry="8" fill="#000000" opacity="0.08"/>
              <ellipse cx="726" cy="340" rx="48" ry="8" fill="#000000" opacity="0.08"/>
              <rect x="243" y="292" width="394" height="28" fill="url(#rose)"/>
              <rect x="243" y="292" width="394" height="1.2" fill="#ffffff" opacity="0.35"/>
              <rect x="243" y="323.5" width="394" height="3" fill="#e9c04a"/>
              <rect x="236" y="118" width="408" height="7" rx="3" fill="url(#alu)"/>
              <rect x="236" y="341" width="408" height="7" rx="3" fill="url(#alu)"/>
              <rect x="236" y="118" width="7" height="230" rx="3" fill="url(#aluV)"/>
              <rect x="637" y="118" width="7" height="230" rx="3" fill="url(#aluV)"/>
              <g id="rivets"></g>

              <circle cx="283" cy="200" r="27" fill="url(#rose)" stroke="#e9c04a" stroke-width="2.5"/>
              <circle cx="283" cy="200" r="22" fill="none" stroke="#e9c04a" stroke-width="0.8" opacity="0.7"/>
              <text x="283" y="208" text-anchor="middle" font-size="22" font-weight="700" fill="#f6dc8a">LB</text>
              <rect x="258" y="252" width="50" height="26" rx="2" fill="#cbc4b8" stroke="#8a8378" stroke-width="0.8"/>
              <path d="M262 258 H304 M262 263 H304 M262 268 H304 M262 273 H304" stroke="#7f786d" stroke-width="1.6"/>

              <rect class="indicator" x="237.5" y="284" width="5" height="10" rx="1.5"/>
              <rect class="tail" x="237.5" y="296" width="5" height="14" rx="1.5"/>
              <rect x="237.5" y="312" width="5" height="8" rx="1.5" fill="#e5e7eb"/>
              <rect class="marker" x="300" y="335.5" width="9" height="3.5" rx="1.5"/>
              <rect class="marker" x="468" y="335.5" width="9" height="3.5" rx="1.5"/>
              <rect class="marker" x="616" y="335.5" width="9" height="3.5" rx="1.5"/>

              <!-- Pod over the cab -->
              <path d="M644 118 H694 Q720 118 722 144 V166 Q722 176 712 176 H644 Z" fill="url(#paint)" stroke="#2b2622" stroke-width="1.2" stroke-linejoin="round"/>
              <rect x="644" y="118.6" width="52" height="6.4" fill="url(#alu)"/>
              <rect class="marker" x="714" y="136" width="4.5" height="9" rx="2"/>

              <!-- Cab -->
              <path d="M644 176 H704 C722 176 733 183 744 199 L770 244 C790 248 800 260 804 282 L806 318 V344 H644 Z" fill="url(#paint)" stroke="#2b2622" stroke-width="1.2" stroke-linejoin="round"/>
              <path d="M644 176 H704 C722 176 733 183 744 199 L770 244 C790 248 800 260 804 282 L806 318 V344 H644 Z" fill="url(#sheen)"/>
              <path d="M773 246.5 C788 250.5 797 261 801 280" fill="none" stroke="#ffffff" stroke-opacity="0.8" stroke-width="1.6" stroke-linecap="round"/>
              <path d="M644 292 H804.6 L806 320 H644 Z" fill="url(#rose)"/>
              <path d="M644 323.5 H806 V326.5 H644 Z" fill="#e9c04a"/>
              <rect x="644" y="336" width="30" height="10" fill="#1d1e20"/>
              <path d="M782 324 H806 Q812 324 812 330 V346 Q812 352 806 352 H782 Z" fill="#1d1e20"/>
              <path d="M784 326.5 H807" stroke="#55585d" stroke-width="1.2" stroke-linecap="round"/>
              <circle cx="802" cy="340" r="3.2" fill="#d9dde2" stroke="#000000" stroke-width="0.8"/>
              <path d="M653 184 V336 M766 252 V308" stroke="#000000" stroke-opacity="0.22" stroke-width="1"/>
              <path d="M752 232 L772 226" stroke="#1d1e20" stroke-width="3" stroke-linecap="round"/>
              <rect x="769" y="210" width="10" height="30" rx="4" fill="#1d1e20"/>
              <rect x="771" y="213" width="2" height="24" rx="1" fill="#ffffff" opacity="0.2"/>
              <ellipse class="indicator" cx="786" cy="274" rx="5" ry="2.6"/>

              <g id="cab" class="hit" role="button" tabindex="0" aria-label="Cab horn">
                <rect x="648" y="182" width="124" height="104" fill="transparent"/>
                <path d="M660 190 H706 C718 190 726 195 732 205 L753 243 H660 Z" fill="url(#glass)" stroke="#101214" stroke-width="2" stroke-linejoin="round"/>
                <path d="M660 190 H706 C718 190 726 195 732 205 L753 243 H660 Z" fill="url(#glassReflect)"/>
                <path d="M668 240 V214 Q668 206 676 206 Q684 206 684 214 V240 Z" fill="#0a0e14" opacity="0.72"/>
                <ellipse cx="733" cy="234" rx="4" ry="8" fill="none" stroke="#0a0e14" stroke-width="2.5" opacity="0.8"/>
                <path d="M676 242 L701 191 H715 L690 242 Z" fill="#ffffff" opacity="0.22"/>
                <path d="M700 242 L721 199 L726 205 L707 242 Z" fill="#ffffff" opacity="0.12"/>
                <path d="M664 228 Q690 210 740 226" fill="none" stroke="#e8a06a" stroke-opacity="0.25" stroke-width="3" stroke-linecap="round"/>
                <rect x="664" y="262" width="22" height="7" rx="3" fill="#1d1e20"/>
                <rect x="666" y="263" width="18" height="1.5" rx="0.75" fill="#ffffff" opacity="0.35"/>
              </g>

              <!-- Headlight -->
              <g id="lamp" class="hit" role="button" tabindex="0" aria-label="Headlights">
                <circle cx="796" cy="296" r="18" fill="transparent"/>
                <circle class="lamp-halo" cx="799" cy="296" r="22" fill="url(#halo)"/>
                <path class="lamp-glass" d="M788 286 H802.6 L804.4 306 H792 Q786 306 786 300 V288 Q786 286 788 286 Z" stroke="#3a3d42" stroke-width="1"/>
                <path d="M790 291 H801.5 M790 296 H802 M790 301 H802.5" stroke="#ffffff" stroke-opacity="0.6" stroke-width="0.8"/>
              </g>

              <!-- Roof: extraction vent and illuminated sign -->
              <rect x="286" y="98" width="20" height="21" fill="url(#aluV)" stroke="#5d6268" stroke-width="0.8"/>
              <rect x="278" y="90" width="36" height="9" rx="4.5" fill="url(#alu)" stroke="#5d6268" stroke-width="0.8"/>
              <g class="vent-steam" filter="url(#soft2)">
                <circle cx="296" cy="80" r="8"/>
                <circle cx="302" cy="76" r="6" style="animation-delay: 1s"/>
                <circle cx="291" cy="78" r="10" style="animation-delay: 2s"/>
              </g>
              <rect x="394" y="104" width="4" height="15" fill="#2a2c30"/>
              <rect x="552" y="104" width="4" height="15" fill="#2a2c30"/>
              <g class="sign">
                <rect class="sign-halo" x="362" y="52" width="226" height="64" rx="12" fill="#ffcf70" filter="url(#soft)"/>
                <rect x="372" y="62" width="206" height="44" rx="5" fill="#26282c" stroke="#0e0f10" stroke-width="1"/>
                <rect class="sign-face" x="376" y="66" width="198" height="36" rx="3" fill="url(#signFace)"/>
                <text class="sign-text" x="475" y="91" text-anchor="middle" font-size="20" font-weight="700" letter-spacing="-0.4">LoadedBites GLA</text>
              </g>

              <!-- Serving hatch -->
              <g id="hatch" class="hit" role="button" tabindex="0" aria-label="Serving hatch">
                <rect x="324" y="144" width="282" height="124" rx="4" fill="url(#alu)" stroke="#5d6268" stroke-width="0.8"/>
                <g clip-path="url(#hatchClip)">
                  <rect x="330" y="150" width="270" height="112" fill="url(#interior)"/>
                  <path d="M420 150 V262 M510 150 V262" stroke="#000000" stroke-opacity="0.12" stroke-width="1"/>

                  <!-- Extraction hood and light strip -->
                  <path d="M330 150 H600 V164 L566 176 H364 L330 164 Z" fill="url(#hood)"/>
                  <path d="M364 176 H566" stroke="#ffffff" stroke-opacity="0.5" stroke-width="1"/>
                  <rect class="led" x="372" y="177" width="186" height="2.5" rx="1.2" fill="#fff4cf"/>

                  <!-- Shelf: sauce bottles and takeaway boxes -->
                  <rect x="330" y="204" width="84" height="3" fill="#6f757c"/>
                  <rect x="338" y="187" width="8" height="17" rx="2" fill="#c81e3a"/>
                  <path d="M340 187 L342 181 L344 187 Z" fill="#c81e3a"/>
                  <rect x="350" y="187" width="8" height="17" rx="2" fill="#e2b429"/>
                  <path d="M352 187 L354 181 L356 187 Z" fill="#e2b429"/>
                  <rect x="362" y="187" width="8" height="17" rx="2" fill="#efe9dc"/>
                  <path d="M364 187 L366 181 L368 187 Z" fill="#efe9dc"/>
                  <rect x="378" y="194" width="30" height="10" fill="#b58a57" stroke="#7d5d37" stroke-width="0.6"/>
                  <rect x="380" y="185" width="26" height="9" fill="#c39a65" stroke="#7d5d37" stroke-width="0.6"/>

                  <!-- Fridge, griddle, hanging utensils, neon -->
                  <rect x="330" y="222" width="66" height="40" fill="#b3b8be"/>
                  <rect x="330" y="222" width="66" height="1.5" fill="#e6e9ec"/>
                  <rect x="386" y="228" width="3" height="18" rx="1.5" fill="#5d6268"/>
                  <rect x="484" y="240" width="116" height="22" fill="#3b3e43"/>
                  <rect x="484" y="240" width="116" height="2" fill="#8a9097"/>
                  <path d="M512 176 V196 M524 176 V192 M536 176 V198" stroke="#3f4347" stroke-width="1.5"/>
                  <circle cx="512" cy="200" r="4.5" fill="#6f757c"/>
                  <rect x="520.5" y="192" width="7" height="10" rx="1" fill="#6f757c"/>
                  <path d="M533 198 L536 208 L539 198" fill="none" stroke="#6f757c" stroke-width="1.6"/>
                  <text class="neon" x="572" y="198" text-anchor="middle" font-size="13" font-weight="700" letter-spacing="1.5">OPEN</text>

                  <rect x="330" y="150" width="270" height="112" fill="url(#warm)"/>

                  <!-- Vendor -->
                  <g class="vendor">
                    <g class="arm" style="transform-origin: 476px 244px">
                      <path d="M476 244 L488 228" stroke="#1f2126" stroke-width="11" stroke-linecap="round"/>
                      <path d="M488 228 L498 208" stroke="#c9906c" stroke-width="7.5" stroke-linecap="round"/>
                      <circle cx="499" cy="205" r="5.5" fill="#d9a27e"/>
                    </g>
                    <path d="M400 264 V252 C400 240 410 234 424 231 L434 228 H446 L456 231 C470 234 480 240 480 252 V264 Z" fill="#1f2126"/>
                    <path d="M425 264 V246 Q425 241 430 241 H450 Q455 241 455 246 V264 Z" fill="url(#rose)"/>
                    <path d="M430 241 L434 229 M450 241 L446 229" stroke="#a51337" stroke-width="2.2" stroke-linecap="round"/>
                    <path d="M433 218 H447 V230 Q440 234 433 230 Z" fill="#b57b5a"/>
                    <ellipse cx="425.5" cy="208" rx="2.6" ry="4.5" fill="#bf8562"/>
                    <ellipse cx="454.5" cy="208" rx="2.6" ry="4.5" fill="#bf8562"/>
                    <ellipse cx="440" cy="206" rx="14.5" ry="17" fill="url(#skin)"/>
                    <path d="M425.6 200 Q424.8 205 426.4 210 L428.6 203 Z M454.4 200 Q455.2 205 453.6 210 L451.4 203 Z" fill="#2a1c16"/>
                    <path d="M425.5 200 C425 184 455 184 454.5 200 C448 196.5 432 196.5 425.5 200 Z" fill="url(#rose)"/>
                    <path d="M426 199.5 C432 204.5 448 204.5 454 199.5 C448 196.5 432 196.5 426 199.5 Z" fill="#8e1030"/>
                    <circle cx="440" cy="190.5" r="2.2" fill="#e9c04a"/>
                    <path d="M431.5 205.6 Q434.5 204.4 437 205.6 M443 205.6 Q445.5 204.4 448.5 205.6" fill="none" stroke="#3a271e" stroke-width="1" stroke-linecap="round"/>
                    <ellipse cx="434.5" cy="208.6" rx="1.5" ry="1.3" fill="#2a1c16"/>
                    <ellipse cx="445.5" cy="208.6" rx="1.5" ry="1.3" fill="#2a1c16"/>
                    <path d="M440 209.5 Q441.6 213.6 439.4 214.6" fill="none" stroke="#a26b4c" stroke-width="1" stroke-linecap="round"/>
                    <path d="M435.5 217.6 Q440 220.8 444.5 217.6" fill="none" stroke="#8a4737" stroke-width="1.3" stroke-linecap="round"/>
                  </g>
                </g>
                <rect x="330" y="150" width="270" height="112" rx="2" fill="none" stroke="#3f4347" stroke-width="1"/>

                <!-- Gas struts that hold the flap up -->
                <g class="struts">
                  <path d="M334 200 L327 122 M596 200 L603 122" stroke="#2f3236" stroke-width="3" stroke-linecap="round"/>
                  <path d="M331.6 172 L327.6 126 M598.4 172 L602.4 126" stroke="#d5d9dd" stroke-width="1.4" stroke-linecap="round"/>
                </g>

                <!-- Hatch flap: outside face when shut, underside when raised -->
                <g class="flap" style="transform-origin: 465px 148px">
                  <g class="flap-in">
                    <rect x="326" y="146" width="278" height="115" rx="3" fill="url(#flapIn)" stroke="#8a8378" stroke-width="0.9"/>
                    <rect x="334" y="158" width="262" height="95" fill="none" stroke="#000000" stroke-opacity="0.14" stroke-width="2"/>
                    <path d="M420 158 V253 M510 158 V253" stroke="#000000" stroke-opacity="0.12" stroke-width="2"/>
                    <rect class="led" x="336" y="151" width="258" height="3.5" rx="1.7" fill="#fff4cf"/>
                  </g>
                  <g class="flap-out">
                    <rect x="326" y="146" width="278" height="115" rx="3" fill="url(#paint)" stroke="#6f6a62" stroke-width="0.9"/>
                    <rect x="330" y="152" width="270" height="105" rx="2" fill="none" stroke="#ffffff" stroke-opacity="0.6" stroke-width="1"/>
                    <rect x="326" y="146" width="278" height="4.5" rx="2" fill="url(#alu)"/>
                    <text x="465" y="206" text-anchor="middle" font-size="31" font-weight="700" letter-spacing="-1.2" fill="#c2183f">Fresh Hot Bites</text>
                    <rect x="404" y="214" width="122" height="2.5" rx="1.2" fill="#e9c04a"/>
                    <text x="465" y="233" text-anchor="middle" font-size="9.5" font-weight="600" letter-spacing="3.2" fill="#5f574f">BATH FOOD VENDOR</text>
                    <rect x="372" y="249" width="14" height="8" rx="1.5" fill="url(#alu)" stroke="#5d6268" stroke-width="0.6"/>
                    <rect x="544" y="249" width="14" height="8" rx="1.5" fill="url(#alu)" stroke="#5d6268" stroke-width="0.6"/>
                    <rect x="447" y="250" width="36" height="6" rx="3" fill="#1d1e20"/>
                  </g>
                </g>
              </g>

              <!-- Steel counter, condiments and the dish served on it -->
              <rect x="320" y="271" width="290" height="7" fill="#000000" opacity="0.14" filter="url(#soft2)"/>
              <path d="M344 271 V284 L356 271 Z M586 271 V284 L574 271 Z" fill="#6f757c"/>
              <rect x="318" y="262" width="294" height="9" rx="1.5" fill="url(#alu)" stroke="#5d6268" stroke-width="0.8"/>
              <rect x="320" y="263" width="290" height="1.2" fill="#ffffff" opacity="0.8"/>
              <g class="condiments">
                <rect x="336" y="246" width="16" height="16" rx="1.5" fill="url(#alu)" stroke="#5d6268" stroke-width="0.6"/>
                <rect x="339" y="250" width="10" height="3" fill="#ffffff"/>
                <rect x="357" y="247" width="7" height="15" rx="2" fill="#c81e3a"/>
                <path d="M359 247 L360.5 242 L362 247 Z" fill="#c81e3a"/>
                <rect x="367" y="247" width="7" height="15" rx="2" fill="#e2b429"/>
                <path d="M369 247 L370.5 242 L372 247 Z" fill="#e2b429"/>
              </g>
              <g transform="translate(552 262)">
                <g class="steam" filter="url(#soft2)">
                  <path d="M-10 -54 q-5 -7 0 -14 q5 -7 0 -14"/>
                  <path d="M0 -58 q-5 -7 0 -14 q5 -7 0 -14" style="animation-delay: 0.6s"/>
                  <path d="M10 -54 q-5 -7 0 -14 q5 -7 0 -14" style="animation-delay: 1.2s"/>
                </g>
                <g class="food" data-dish="wrap">
                  <path d="M-15 0 L-11 -42 Q0 -52 11 -42 L15 0 Z" fill="#e7c489" stroke="#8a5a22" stroke-width="1" stroke-linejoin="round"/>
                  <path d="M-6 -44 Q0 -49 7 -43 L6 -30 H-6 Z" fill="#c9a063" opacity="0.6"/>
                  <circle cx="-5" cy="-44" r="4.5" fill="#5f9a17"/>
                  <circle cx="3" cy="-46" r="4.5" fill="#c9302c"/>
                  <circle cx="8" cy="-42" r="3.5" fill="#e8b923"/>
                  <path d="M-15 0 L-13 -22 L13 -22 L15 0 Z" fill="#f4f2ee" stroke="#a8a29e" stroke-width="0.8" stroke-linejoin="round"/>
                  <path d="M-12.6 -12 H12.6" stroke="#c2183f" stroke-width="3"/>
                </g>
                <g class="food" data-dish="cheese">
                  <ellipse cx="0" cy="-4" rx="32" ry="6" fill="#f4f2ee" stroke="#a8a29e" stroke-width="0.8"/>
                  <path d="M-24 -6 Q-22 -30 0 -32 Q22 -30 24 -6 Z" fill="#d98a1c" stroke="#8a4f10" stroke-width="1" stroke-linejoin="round"/>
                  <path d="M-18 -18 Q-16 -30 0 -31 Q16 -30 18 -18 Q13 -10 8 -18 Q3 -8 -3 -18 Q-9 -9 -18 -18 Z" fill="#f6d24a" stroke="#c08d12" stroke-width="0.8" stroke-linejoin="round"/>
                  <path d="M-10 -26 Q-4 -22 2 -27 Q8 -22 13 -25" fill="none" stroke="#c2183f" stroke-width="2.2" stroke-linecap="round"/>
                  <circle cx="-7" cy="-21" r="1.6" fill="#4d7c0f"/>
                  <circle cx="6" cy="-20" r="1.6" fill="#4d7c0f"/>
                </g>
                <g class="food" data-dish="spiced">
                  <circle cx="-15" cy="-20" r="9" fill="#b3400f" stroke="#6f2a0c" stroke-width="0.8"/>
                  <circle cx="0" cy="-24" r="9" fill="#cf5413" stroke="#6f2a0c" stroke-width="0.8"/>
                  <circle cx="15" cy="-20" r="9" fill="#b3400f" stroke="#6f2a0c" stroke-width="0.8"/>
                  <path d="M-27 0 L-31 -17 H31 L27 0 Z" fill="#f4f2ee" stroke="#a8a29e" stroke-width="0.8" stroke-linejoin="round"/>
                  <path d="M-19 -17 L-17 0 M-6 -17 L-5 0 M6 -17 L5 0 M19 -17 L17 0" stroke="#c2183f" stroke-width="3"/>
                  <path d="M-4 -36 Q8 -44 18 -34" fill="none" stroke="#c9302c" stroke-width="5" stroke-linecap="round"/>
                  <path d="M-4 -36 L-9 -40" stroke="#4d7c0f" stroke-width="3" stroke-linecap="round"/>
                </g>
                <g class="food" data-dish="special">
                  <ellipse cx="0" cy="-4" rx="32" ry="6" fill="#f4f2ee" stroke="#a8a29e" stroke-width="0.8"/>
                  <path d="M-26 -6 A26 25 0 0 1 26 -6 Z" fill="url(#rim)" stroke="#57534e" stroke-width="1" stroke-linejoin="round"/>
                  <circle cx="0" cy="-34" r="4.5" fill="url(#rim)" stroke="#57534e" stroke-width="1"/>
                  <path d="M-15 -20 Q-9 -27 -1 -28.5" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" opacity="0.9"/>
                </g>
              </g>

              <!-- Wheel arches and wheels -->
              <path d="M276 348 A54 54 0 0 1 384 348 Z" fill="#0a0a0c"/>
              <path d="M276 348 A54 54 0 0 1 384 348" fill="none" stroke="url(#alu)" stroke-width="3"/>
              <path d="M672 348 A54 54 0 0 1 780 348 Z" fill="#0a0a0c"/>
              <path d="M672 348 A54 54 0 0 1 780 348" fill="none" stroke="#1d1e20" stroke-width="6"/>
              <g id="wheels"></g>

              <!-- Horn -->
              <g transform="translate(818 300)" class="honk" fill="none" stroke="#fff1c2" stroke-width="2.6" stroke-linecap="round">
                <path d="M0 -7 Q5 0 0 7"/>
                <path d="M9 -13 Q18 0 9 13"/>
                <path d="M18 -19 Q31 0 18 19"/>
              </g>

              <g id="rig-hots"></g>
            </g>
          </g>

          <!-- Near kerb and pavement, in front of the truck -->
          <rect x="0" y="398" width="1000" height="7" fill="url(#kerb)"/>
          <rect x="0" y="398" width="1000" height="1.2" fill="#d6d0c6" opacity="0.85"/>
          <rect x="0" y="405" width="1000" height="65" fill="url(#slab)"/>
          <g id="paving"></g>
          <!-- Wet patches and lamp reflection on the pavement -->
          <ellipse cx="465" cy="420" rx="180" ry="8" fill="#ffffff" opacity="0.06" filter="url(#soft)"/>
          <ellipse cx="900" cy="418" rx="70" ry="7" fill="#ffcf70" opacity="0.14" filter="url(#soft)"/>
          <ellipse cx="200" cy="430" rx="50" ry="5" fill="#ffffff" opacity="0.05"/>
          <rect x="0" y="366" width="1000" height="104" filter="url(#grain)" opacity="0.22"/>
          <ellipse class="pool" cx="465" cy="432" rx="240" ry="38" fill="url(#halo)" opacity="0.55"/>

          <!-- Chalkboard menu on the pavement -->
          <g id="board">
            <ellipse cx="125" cy="443" rx="96" ry="6" fill="#000000" opacity="0.5" filter="url(#soft2)"/>
            <path d="M58 214 L46 440 M192 214 L204 440" stroke="#5b3a1c" stroke-width="7" stroke-linecap="round"/>
            <rect x="40" y="186" width="170" height="234" rx="4" fill="url(#wood)" stroke="#3d2613" stroke-width="1"/>
            <path d="M44 190 V416 M206 190 V416" stroke="#ffffff" stroke-opacity="0.12" stroke-width="1"/>
            <rect x="40" y="420" width="9" height="20" fill="#6c4320"/>
            <rect x="201" y="420" width="9" height="20" fill="#6c4320"/>
            <rect x="50" y="196" width="150" height="214" rx="2" fill="url(#slate)"/>
            <ellipse cx="140" cy="300" rx="52" ry="80" fill="#ffffff" opacity="0.035"/>
            <rect x="112" y="183" width="26" height="6" rx="2" fill="url(#alu)"/>
            <text class="chalk" x="125" y="228" text-anchor="middle" font-size="32" font-weight="700" fill="#f6f1e6">Menu</text>
            <path d="M88 236 Q106 232 125 236 T162 235" fill="none" stroke="#f1d27c" stroke-width="2" stroke-linecap="round" opacity="0.9"/>
            <g id="menu-rows"></g>
            <text class="chalk" x="125" y="398" text-anchor="middle" font-size="17" font-weight="600" fill="#f1d27c">tap to order</text>
            <g id="board-hots"></g>
          </g>

          <rect x="0" y="0" width="1000" height="470" fill="url(#vignette)" pointer-events="none"/>
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
        const INTRO = "Select the hatch to open up, or choose a dish from the menu.";

        // The truck starts off-screen and cannot be used until it has parked.
        const state = { open: false, lit: false, busy: true };
        const say = (text) => { statusEl.textContent = text; };

        // ---------- Build the repeated parts of the drawing ----------
        [[60, 16], [210, 12], [330, 54], [395, 12], [560, 18], [640, 46], [840, 14], [962, 44], [130, 60]]
          .forEach(([cx, cy], i) => {
            el("circle", { class: "star", cx, cy, r: i % 3 === 0 ? 1.2 : 0.8, style: "animation-delay:" + (i * 0.41) % 3 + "s" }, $("stars"));
          });

        // Terraced stone buildings with sash windows, some lit.
        const town = $("town");
        [
          { x: -10, w: 312, top: 152, stone: "#6b5e53", trim: "#877868" },
          { x: 302, w: 340, top: 126, stone: "#76685b", trim: "#93836f" },
          { x: 642, w: 370, top: 160, stone: "#63574e", trim: "#7e6f61" },
        ].forEach((b, bi) => {
          const height = 352 - b.top;
          [b.x + 26, b.x + b.w - 56].forEach((cx) => {
            el("rect", { x: cx, y: b.top - 46, width: 30, height: 44, fill: b.stone }, town);
            el("rect", { x: cx - 2, y: b.top - 48, width: 34, height: 4, fill: b.trim }, town);
            [4, 13, 22].forEach((dx) => el("rect", { x: cx + dx, y: b.top - 56, width: 5, height: 8, fill: "#74483a" }, town));
          });
          el("path", { d: "M" + b.x + " " + b.top + " L" + (b.x + 12) + " " + (b.top - 24) + " H" + (b.x + b.w - 12) + " L" + (b.x + b.w) + " " + b.top + " Z", fill: "#22252e" }, town);
          el("rect", { x: b.x, y: b.top, width: b.w, height, fill: b.stone }, town);
          el("rect", { x: b.x, y: b.top, width: b.w, height: 7, fill: b.trim }, town);
          el("rect", { x: b.x, y: b.top + 7, width: b.w, height: 2.5, fill: "#000000", opacity: 0.25 }, town);
          el("rect", { x: b.x, y: b.top + height * 0.62, width: b.w, height: 4, fill: b.trim }, town);
          el("rect", { x: b.x + b.w - 2.5, y: b.top, width: 2.5, height, fill: "#000000", opacity: 0.3 }, town);

          const cols = Math.floor((b.w - 30) / 52);
          const first = b.x + (b.w - (cols - 1) * 52) / 2;
          for (let c = 0; c < cols; c++) {
            [[0.1, 0.17], [0.34, 0.24], [0.69, 0.23]].forEach(([at, tall], r) => {
              const x = first + c * 52 - 12;
              const y = b.top + height * at;
              const h = height * tall;
              const lit = (c * 7 + r * 5 + bi * 3) % 5 < 2;
              el("rect", { x: x - 3, y: y - 3, width: 30, height: h + 6, fill: b.trim }, town);
              if (lit) el("rect", { x: x - 6, y: y - 4, width: 36, height: h + 10, fill: "#ffcf70", opacity: 0.18, filter: "url(#soft2)" }, town);
              el("rect", { x, y, width: 24, height: h, fill: lit ? "url(#litWin)" : "url(#darkWin)" }, town);
              el("path", {
                d: "M" + (x + 12) + " " + y + " V" + (y + h) + " M" + x + " " + (y + h / 3) + " H" + (x + 24) + " M" + x + " " + (y + (2 * h) / 3) + " H" + (x + 24),
                stroke: lit ? "#8a6a3c" : "#5a6682",
                "stroke-width": 1,
                fill: "none",
              }, town);
              el("rect", { x: x - 5, y: y + h + 3, width: 34, height: 3, fill: b.trim }, town);
            });
          }
        });

        // Festoon bulbs along the cable.
        const wire = $("wire");
        const wireLength = wire.getTotalLength();
        for (let i = 1; i < 20; i++) {
          const p = wire.getPointAtLength((wireLength * i) / 20);
          el("circle", { class: "bulb-halo", cx: p.x, cy: p.y + 6, r: 9, fill: "url(#halo)", style: "animation-delay:" + (i % 5) * 0.5 + "s" }, $("bulbs"));
          el("rect", { x: p.x - 1.2, y: p.y, width: 2.4, height: 3.5, fill: "#0a0c12" }, $("bulbs"));
          el("circle", { cx: p.x, cy: p.y + 6, r: 2.8, fill: "#fff3c9" }, $("bulbs"));
        }

        // Rivets along the aluminium trim.
        const rivet = (cx, cy) => {
          el("circle", { cx, cy, r: 1.1, fill: "#7b8087" }, $("rivets"));
          el("circle", { cx: cx - 0.3, cy: cy - 0.3, r: 0.45, fill: "#ffffff", opacity: 0.8 }, $("rivets"));
        };
        for (let x = 252; x <= 632; x += 16) { rivet(x, 121.5); rivet(x, 344.5); }
        for (let y = 136; y <= 332; y += 18) { rivet(239.5, y); rivet(640.5, y); }

        // Paving joints and kerb stones.
        const paving = $("paving");
        for (let x = 40; x < 1000; x += 92) el("rect", { x, y: 398, width: 1, height: 7, fill: "#4b4741", opacity: 0.7 }, paving);
        [[424, 110, 30, 405], [448, 132, -24, 424], [470, 156, 64, 448]].forEach(([bottom, step, start, top]) => {
          if (bottom < 470) {
            el("rect", { x: 0, y: bottom, width: 1000, height: 1.3, fill: "#3b3733", opacity: 0.8 }, paving);
            el("rect", { x: 0, y: bottom + 1.3, width: 1000, height: 0.8, fill: "#a39d93", opacity: 0.35 }, paving);
          }
          for (let x = start; x < 1000; x += step) {
            el("rect", { x, y: top, width: 1.2, height: bottom - top, fill: "#3b3733", opacity: 0.7 }, paving);
          }
        });

        // Wheels: tyre, steel rim with vent holes, hub and nuts.
        const wheels = [];
        [[330, 364, "Rear wheel"], [726, 364, "Front wheel"]].forEach(([cx, cy, label]) => {
          const g = el("g", { class: "hit wheel", role: "button", tabindex: "0", "aria-label": label }, $("wheels"));
          const spin = el("g", { class: "wheel-spin", style: "transform-origin:" + cx + "px " + cy + "px" }, g);
          el("circle", { cx, cy, r: 42, fill: "url(#tyre)" }, spin);
          el("circle", { cx, cy, r: 40, fill: "none", stroke: "#000000", "stroke-width": 3.5, "stroke-dasharray": "2.2 4.4", opacity: 0.55 }, spin);
          el("circle", { cx, cy, r: 33, fill: "none", stroke: "#3a3a3f", "stroke-width": 1 }, spin);
          el("circle", { cx, cy, r: 28, fill: "#0c0c0e" }, spin);
          el("circle", { cx, cy, r: 26.5, fill: "url(#rim)", stroke: "#4f545a", "stroke-width": 1 }, spin);
          el("circle", { cx, cy, r: 19.5, fill: "none", stroke: "#6c7279", "stroke-width": 1, opacity: 0.7 }, spin);
          for (let i = 0; i < 6; i++) {
            const deg = i * 60;
            const a = (deg * Math.PI) / 180;
            const hx = (cx + Math.cos(a) * 13.5).toFixed(1);
            const hy = (cy + Math.sin(a) * 13.5).toFixed(1);
            el("ellipse", { cx: hx, cy: hy, rx: 4.6, ry: 2.7, fill: "#17181b", transform: "rotate(" + (deg + 90) + " " + hx + " " + hy + ")" }, spin);
          }
          el("circle", { cx, cy, r: 6.5, fill: "url(#rim)", stroke: "#4f545a", "stroke-width": 1 }, spin);
          for (let i = 0; i < 5; i++) {
            const a = (i / 5) * Math.PI * 2;
            el("circle", { cx: (cx + Math.cos(a) * 3.8).toFixed(1), cy: (cy + Math.sin(a) * 3.8).toFixed(1), r: 0.9, fill: "#3a3d42" }, spin);
          }
          // Shadow from the arch stays put while the wheel turns.
          el("path", { d: "M" + (cx - 42) + " " + cy + " A42 42 0 0 1 " + (cx + 42) + " " + cy + " Z", fill: "#000000", opacity: 0.3 }, g);
          wheels.push(g);
        });

        // Chalk menu rows, and matching buttons for small screens.
        const menuRows = {};
        DISHES.forEach((dish, i) => {
          const y = 246 + i * 33;
          const row = el("g", { class: "hit menu-item", role: "button", tabindex: "0", "aria-label": "Order " + dish.name }, $("menu-rows"));
          el("rect", { class: "row-bg", x: 56, y, width: 138, height: 30, rx: 5 }, row);
          el("path", { d: "M66 " + (y + 16) + " h7", stroke: "#f1d27c", "stroke-width": 2, "stroke-linecap": "round" }, row);
          const label = el("text", { class: "chalk", x: 80, y: y + 22, "font-size": 23, "font-weight": 600, fill: "#f6f1e6" }, row);
          label.textContent = dish.name;
          menuRows[dish.key] = row;

          const chip = document.createElement("button");
          chip.type = "button";
          chip.textContent = dish.name;
          chip.dataset.order = dish.key;
          $("chips").appendChild(chip);
        });

        const hots = {};
        [["hatch", 582, 166, "rig-hots"], ["horn", 706, 222, "rig-hots"], ["lights", 797, 296, "rig-hots"],
         ["lap", 726, 328, "rig-hots"], ["menu", 196, 202, "board-hots"]].forEach(([name, cx, cy, parent]) => {
          const g = el("g", { class: "hot" }, $(parent));
          el("circle", { class: "hot-ring", cx, cy, r: 8, style: "transform-origin:" + cx + "px " + cy + "px" }, g);
          el("circle", { class: "hot-dot", cx, cy, r: 3.6 }, g);
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
        const lockable = document.querySelectorAll('[data-act="hatch"], [data-act="lap"], #chips button');
        const setLocked = (locked) => lockable.forEach((b) => { b.disabled = locked; });

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
            setTimeout(wave, 750);
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
          const wait = state.open ? 0 : 900;
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
          honkTimer = setTimeout(() => scene.classList.remove("is-honking"), 1100);
          beep();
          if (!state.busy) say("Beep beep!");
        };

        let lapTimer;
        const endLap = () => {
          if (!scene.classList.contains("is-driving")) return;
          clearTimeout(lapTimer);
          scene.classList.remove("is-driving");
          state.busy = false;
          setLocked(false);
          say("Parked and ready to serve.");
        };
        const lap = () => {
          if (state.busy) return;
          used("lap");
          const wait = state.open ? 800 : 0;
          setHatch(false);
          state.busy = true;
          setLocked(true);
          say("Off for a quick lap of the block…");
          setTimeout(() => {
            scene.classList.add("is-driving");
            lapTimer = setTimeout(endLap, 5200);
          }, wait);
        };

        // ---------- Arrival: drive in the first time the section is on screen ----------
        let arrived = false;
        let arriveTimer;
        const park = () => {
          if (!state.busy || scene.classList.contains("is-driving")) return;
          clearTimeout(arriveTimer);
          scene.classList.remove("is-arriving");
          state.busy = false;
          setLocked(false);
          say(INTRO);
        };
        const arrive = () => {
          if (arrived) return;
          arrived = true;
          wrap.classList.remove("pre");
          if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
            park();
            return;
          }
          say("Pulling in…");
          scene.classList.add("is-arriving");
          arriveTimer = setTimeout(park, 4200);
        };

        truck.addEventListener("animationend", (event) => {
          if (event.animationName === "lap") endLap();
          if (event.animationName === "arrive") park();
        });

        setLocked(true);
        if ("IntersectionObserver" in window) {
          const watcher = new IntersectionObserver((entries) => {
            if (entries.some((entry) => entry.isIntersecting)) {
              watcher.disconnect();
              arrive();
            }
          }, { threshold: 0.35 });
          watcher.observe(wrap);
        } else {
          arrive();
        }

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
        const frame = () => art.setAttribute("viewBox", small.matches ? "216 44 620 426" : "0 0 1000 470");
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
      })();
    </script>
    """,
    height=660,
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
