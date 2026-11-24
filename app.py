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
      @import url("https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap");

      :root {
        --ft-display: "Space Grotesk", sans-serif;
        --ft-sans: "Outfit", sans-serif;
        --ft-red: #9f1239;
        --ft-deep: #6b0f2b;
        --ft-night: #2a0612;
        --ft-gold: #f5d56a;
        --ft-cream: #fff4f0;
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

      /* Real skyscraper photo sits behind everything; blur rises as you scroll */
      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stHeader"],
      section.main {
        background: transparent !important;
      }
      .ft-sky {
        position: fixed;
        inset: -4%;
        z-index: 0;
        pointer-events: none;
        background:
          url("https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=2400&q=80")
          center center / cover no-repeat;
        transform: scale(1.08);
        filter: blur(var(--ft-sky-blur, 2px)) saturate(1.15) brightness(0.78);
        will-change: filter;
      }
      .ft-sky-tint {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background:
          linear-gradient(180deg, rgba(42, 6, 18, 0.28) 0%, rgba(159, 18, 57, 0.42) 48%, rgba(42, 6, 18, 0.72) 100%),
          radial-gradient(900px 500px at 15% 0%, rgba(245, 213, 106, 0.16), transparent 55%);
      }
      ::selection {
        background: var(--ft-gold);
        color: var(--ft-night);
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        position: relative;
        z-index: 1;
        padding-top: 1.8rem;
        padding-bottom: 3.4rem;
        padding-left: 1.4rem !important;
        padding-right: 1.4rem !important;
        max-width: 1120px;
      }

      @keyframes ftHeroIn {
        from { opacity: 0; transform: translateY(28px) scale(0.97); }
        to { opacity: 1; transform: translateY(0) scale(1); }
      }
      @keyframes ftShine {
        0% { transform: translateX(-120%) rotate(12deg); }
        100% { transform: translateX(220%) rotate(12deg); }
      }
      @keyframes ftBob {
        0%, 100% { transform: translateY(-2px); }
        50% { transform: translateY(6px); }
      }
      @keyframes ftFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
      }

      /* Hero — frosted glass over the city */
      .ft-hero {
        position: relative;
        overflow: hidden;
        isolation: isolate;
        background: linear-gradient(145deg, rgba(255,255,255,0.22), rgba(159,18,57,0.28) 55%, rgba(42,6,18,0.38));
        border: 1px solid rgba(255, 255, 255, 0.42);
        border-radius: 32px;
        padding: 3.6rem 3.1rem 3.2rem;
        margin-bottom: 0.45rem;
        box-shadow:
          0 30px 70px rgba(0, 0, 0, 0.35),
          inset 0 1px 0 rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(22px) saturate(1.35);
        -webkit-backdrop-filter: blur(22px) saturate(1.35);
        animation: ftHeroIn 0.75s cubic-bezier(0.22, 1, 0.36, 1) both;
        width: 100%;
        box-sizing: border-box;
      }
      .ft-hero::before {
        content: "";
        position: absolute;
        inset: -40% auto auto -20%;
        width: 55%;
        height: 140%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.28), transparent);
        animation: ftShine 4.8s ease-in-out infinite;
        pointer-events: none;
      }
      .ft-hero::after {
        content: "";
        position: absolute;
        right: -80px;
        top: -100px;
        width: 340px;
        height: 340px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(245, 213, 106, 0.35), transparent 68%);
        pointer-events: none;
        animation: ftFloat 5.5s ease-in-out infinite;
      }
      .ft-tag {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        background: rgba(255, 255, 255, 0.14);
        color: var(--ft-gold);
        border: 1px solid rgba(245, 213, 106, 0.5);
        padding: 0.48rem 0.9rem;
        border-radius: 999px;
        margin-bottom: 1.1rem;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
      }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.9rem, 7vw, 4.6rem);
        font-weight: 700;
        margin: 0 0 0.8rem 0;
        line-height: 0.95;
        letter-spacing: -0.06em;
        color: #ffffff;
        text-shadow: 0 10px 40px rgba(42, 6, 18, 0.35);
      }
      .ft-sub {
        margin: 0;
        font-size: 1.2rem;
        max-width: 36rem;
        line-height: 1.5;
        color: rgba(255, 255, 255, 0.94);
        font-weight: 500;
        letter-spacing: -0.015em;
      }
      .ft-points {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin-top: 1.6rem;
      }
      .ft-points span {
        font-size: 0.84rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        padding: 0.45rem 0.95rem;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.38);
        color: #ffffff;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: transform 0.25s ease, background 0.25s ease, border-color 0.25s ease;
      }
      .ft-points span:hover {
        transform: translateY(-2px) scale(1.04);
        background: rgba(255, 255, 255, 0.22);
        border-color: var(--ft-gold);
      }

      .ft-scroll-hint {
        text-align: center;
        color: rgba(255, 255, 255, 0.92);
        font-size: 0.92rem;
        font-weight: 600;
        letter-spacing: -0.01em;
        margin: 0.55rem 0 0.15rem;
        text-shadow: 0 2px 12px rgba(0,0,0,0.45);
      }
      .ft-arrow {
        display: inline-block;
        color: var(--ft-gold);
        animation: ftBob 1.4s ease-in-out infinite;
      }

      /* Sections */
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(1.85rem, 3.4vw, 2.45rem);
        font-weight: 700;
        margin: 2.3rem 0 0.55rem;
        color: #ffffff;
        letter-spacing: -0.05em;
        line-height: 1.05;
        display: inline-block;
        text-shadow: 0 4px 24px rgba(0,0,0,0.35);
      }
      .ft-section::after {
        content: "";
        display: block;
        width: 64px;
        height: 4px;
        border-radius: 999px;
        background: linear-gradient(90deg, var(--ft-gold), transparent);
        margin-top: 0.65rem;
      }
      .ft-lead, .ft-body {
        padding: 1rem 1.15rem;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.22);
        backdrop-filter: blur(16px) saturate(1.2);
        -webkit-backdrop-filter: blur(16px) saturate(1.2);
        box-shadow: 0 10px 28px rgba(0,0,0,0.18);
      }
      .ft-lead {
        font-size: 1.18rem;
        line-height: 1.55;
        color: rgba(255, 255, 255, 0.96);
        font-weight: 500;
        letter-spacing: -0.015em;
        max-width: 48rem;
        margin: 0 0 0.8rem 0;
      }
      .ft-body {
        font-size: 1.05rem;
        line-height: 1.65;
        color: rgba(255, 255, 255, 0.92);
        letter-spacing: -0.01em;
        max-width: 48rem;
        margin: 0 0 0.75rem 0;
      }

      /* Glass cards */
      .ft-card {
        position: relative;
        overflow: hidden;
        background: linear-gradient(160deg, rgba(255,255,255,0.2), rgba(255,255,255,0.06));
        border: 1px solid rgba(255, 255, 255, 0.38);
        border-radius: 20px;
        padding: 1.35rem 1.35rem 1.25rem 1.55rem;
        margin-bottom: 0.95rem;
        box-shadow:
          0 16px 40px rgba(0, 0, 0, 0.22),
          inset 0 1px 0 rgba(255, 255, 255, 0.35);
        backdrop-filter: blur(18px) saturate(1.3);
        -webkit-backdrop-filter: blur(18px) saturate(1.3);
        transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.3s ease, border-color 0.3s ease;
      }
      .ft-card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, var(--ft-gold), #fb7185);
      }
      .ft-card:hover {
        transform: translateY(-4px) scale(1.02);
        border-color: rgba(245, 213, 106, 0.75);
        box-shadow: 0 22px 48px rgba(42, 6, 18, 0.42);
      }
      .ft-card h3 {
        font-family: var(--ft-display) !important;
        font-size: 1.28rem;
        font-weight: 700;
        margin: 0 0 0.4rem 0;
        padding: 0;
        color: #ffffff;
        letter-spacing: -0.035em;
      }
      .ft-card p {
        font-size: 0.98rem;
        line-height: 1.55;
        color: rgba(255, 255, 255, 0.9);
        margin: 0;
        letter-spacing: -0.01em;
      }

      .ft-footer {
        text-align: center;
        color: rgba(255, 255, 255, 0.92);
        font-size: 0.95rem;
        margin-top: 2.6rem;
        padding: 1.4rem 1.2rem;
        border: 1px solid rgba(255, 255, 255, 0.28);
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        font-weight: 500;
        line-height: 1.65;
      }
      .ft-footer strong {
        font-family: var(--ft-display);
        font-size: 1.15rem;
        letter-spacing: -0.03em;
        color: #ffffff;
      }

      /* Buttons */
      div[data-testid="stButton"] button,
      .stLinkButton a {
        border-radius: 999px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.85rem 1.35rem !important;
        letter-spacing: -0.01em !important;
        background: rgba(255, 255, 255, 0.88) !important;
        color: var(--ft-red) !important;
        border: 1px solid rgba(255, 255, 255, 0.7) !important;
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.28) !important;
        backdrop-filter: blur(12px) !important;
        transition: transform 0.25s ease, background 0.25s ease,
                    border-color 0.25s ease, box-shadow 0.25s ease !important;
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
        transform: translateY(-3px) scale(1.03) !important;
        box-shadow: 0 16px 34px rgba(42, 6, 18, 0.4) !important;
      }

      /* Scroll reveal */
      .ft-reveal:not(.ft-in) { opacity: 0; }
      .ft-in { animation: ftRise 0.8s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .ft-section.ft-in { animation-name: ftSlideIn; }
      .ft-card.ft-in { animation-name: ftPop; }
      @keyframes ftRise {
        from { opacity: 0; transform: translateY(36px); filter: blur(6px); }
      }
      @keyframes ftSlideIn {
        from { opacity: 0; transform: translateX(-60px); }
      }
      @keyframes ftPop {
        from { opacity: 0; transform: translateY(48px) scale(0.92); }
      }
      @media (prefers-reduced-motion: reduce) {
        .ft-reveal:not(.ft-in) { opacity: 1; }
        .ft-in, .ft-arrow, .ft-hero::before, .ft-hero::after { animation: none; }
      }
      @media (max-width: 640px) {
        .ft-hero { padding: 2.3rem 1.5rem 2.1rem; border-radius: 24px; }
      }
    </style>
    """
)

# --- City sky + glass hero ---
show_html(
    """
    <div class="ft-sky" aria-hidden="true"></div>
    <div class="ft-sky-tint" aria-hidden="true"></div>
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
        gap: 1rem;
        padding: 0.35rem 2px 1.6rem;
        width: 100%;
        box-sizing: border-box;
      }
      .bit { width: 100%; }
      .bit-inner {
        width: 100%;
        box-sizing: border-box;
        border-radius: 22px;
        padding: 1.85rem 2rem 1.65rem;
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
        justify-content: center;
        min-height: 118px;
        border: 1px solid rgba(255, 255, 255, 0.38);
        box-shadow: 0 20px 40px -18px rgba(42, 6, 18, 0.85);
        position: relative;
        overflow: hidden;
        cursor: default;
        transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.35s ease;
        will-change: transform, opacity, filter;
      }
      .bit-inner::before {
        content: "";
        position: absolute;
        inset: 0 auto 0 -40%;
        width: 40%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.28), transparent);
        transform: skewX(-18deg);
        opacity: 0;
        transition: opacity 0.3s ease;
      }
      .bit-inner:hover::before { opacity: 1; animation: sweep 0.9s ease; }
      @keyframes sweep {
        from { left: -40%; }
        to { left: 120%; }
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
        background: rgba(42, 6, 18, 0.45);
        border: 1px solid rgba(255,255,255,0.2);
        padding: 0.32rem 0.7rem;
        border-radius: 999px;
        backdrop-filter: blur(6px);
      }
      .bit-1 .bit-inner {
        background: linear-gradient(115deg, rgba(190,18,60,0.72), rgba(225,29,72,0.55) 55%, rgba(251,113,133,0.5));
        backdrop-filter: blur(18px) saturate(1.35);
        -webkit-backdrop-filter: blur(18px) saturate(1.35);
      }
      .bit-2 .bit-inner {
        background: linear-gradient(115deg, rgba(136,19,55,0.72), rgba(244,63,94,0.52) 52%, rgba(245,213,106,0.42));
        backdrop-filter: blur(18px) saturate(1.35);
        -webkit-backdrop-filter: blur(18px) saturate(1.35);
      }
      .bit-3 .bit-inner {
        background: linear-gradient(115deg, rgba(76,5,25,0.75), rgba(190,18,60,0.55) 48%, rgba(251,113,133,0.48));
        backdrop-filter: blur(18px) saturate(1.35);
        -webkit-backdrop-filter: blur(18px) saturate(1.35);
      }
      .bit-inner:hover {
        transform: scale(1.02);
        box-shadow: 0 26px 46px -16px rgba(42, 6, 18, 0.95);
      }
      .bit-kicker {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #f5d56a;
      }
      .bit-words {
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(2rem, 5vw, 3.15rem);
        font-weight: 700;
        letter-spacing: -0.05em;
        line-height: 1.05;
        color: #ffffff;
        margin: 0;
        transition: transform 0.3s ease;
        transform-origin: left center;
      }
      .bit-inner:hover .bit-words { transform: scale(1.05); }
      .bit-sub {
        margin: 0;
        font-size: 1.05rem;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.92);
        letter-spacing: -0.015em;
        max-width: 36rem;
      }
      .bit:not(.in) .bit-inner { opacity: 0; }
      .bit-1.in .bit-inner { animation: adSweepLeft 0.95s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .bit-2.in .bit-inner { animation: adSweepRight 0.95s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .bit-3.in .bit-inner { animation: adDropSpin 1.05s cubic-bezier(0.34, 1.3, 0.64, 1) backwards; }
      @keyframes adSweepLeft {
        0% { opacity: 0; filter: blur(12px); transform: translateX(-110%) rotate(-8deg); }
        70% { opacity: 1; filter: blur(0); transform: translateX(2%) rotate(1.5deg); }
      }
      @keyframes adSweepRight {
        0% { opacity: 0; filter: blur(12px); transform: translateX(110%) rotate(8deg); }
        70% { opacity: 1; filter: blur(0); transform: translateX(-2%) rotate(-1.5deg); }
      }
      @keyframes adDropSpin {
        0% { opacity: 0; filter: blur(14px); transform: translateY(90px) scale(0.9) rotate(-10deg); }
        60% { opacity: 1; filter: blur(0); transform: translateY(-8px) scale(1.03) rotate(2deg); }
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
              entry.target.style.animationDelay = order * 100 + "ms";
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

        // City background gets blurrier the further you scroll down.
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
          el.style.setProperty("--ft-sky-blur", (2 + t * 14).toFixed(2) + "px");
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
    height=520,
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
