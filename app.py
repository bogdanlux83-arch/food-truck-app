from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


def bite_show_html() -> str:
    return r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Manrope:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    html, body {
      margin: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: transparent;
      font-family: Manrope, system-ui, sans-serif;
    }
    #stage {
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 28px;
      overflow: hidden;
      border: 1px solid rgba(232, 106, 23, 0.22);
      background:
        radial-gradient(ellipse 80% 60% at 50% 100%, rgba(232,106,23,0.22), transparent 55%),
        linear-gradient(160deg, #fff6e4 0%, #ffe2b0 45%, #f5c56a 100%);
      box-shadow: 0 20px 50px rgba(120, 55, 10, 0.12);
      cursor: grab;
      transform: translateY(48px) scale(0.94);
      opacity: 0;
      transition: opacity 0.9s cubic-bezier(0.22,1,0.36,1), transform 0.9s cubic-bezier(0.22,1,0.36,1);
    }
    #stage.in {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
    #stage:active { cursor: grabbing; }
    #stage.hot { box-shadow: 0 28px 60px rgba(232,106,23,0.28); }

    .label {
      position: absolute;
      left: 1.25rem;
      top: 1.15rem;
      z-index: 5;
      pointer-events: none;
    }
    .label .kicker {
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(28,20,14,0.55);
    }
    .label .title {
      margin: 0.2rem 0 0;
      font-family: Syne, sans-serif;
      font-size: clamp(1.35rem, 3vw, 1.9rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      text-transform: uppercase;
      line-height: 0.95;
      color: #1c140e;
    }
    .hint {
      position: absolute;
      right: 1.25rem;
      top: 1.25rem;
      z-index: 5;
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: rgba(28,20,14,0.4);
      pointer-events: none;
      transition: color 0.3s ease;
    }
    #stage.hot .hint { color: rgba(28,20,14,0.7); }

    .world {
      position: absolute;
      inset: 0;
      display: grid;
      place-items: center;
      perspective: 900px;
      transform-style: preserve-3d;
    }
    .bite {
      position: relative;
      width: min(280px, 58vw);
      height: 220px;
      transform-style: preserve-3d;
      transform: rotateX(18deg) rotateY(-18deg);
      transition: transform 0.15s ease-out;
    }

    .layer {
      position: absolute;
      left: 50%;
      width: 100%;
      border-radius: 999px;
      transform: translateX(-50%) translateY(var(--y)) translateZ(var(--z)) scale(0.3);
      opacity: 0;
      box-shadow: 0 10px 20px rgba(0,0,0,0.18);
      transform-origin: center;
    }
    #stage.in .layer {
      animation: dropIn 0.85s cubic-bezier(0.22, 1.4, 0.36, 1) forwards;
      animation-delay: var(--d);
    }
    @keyframes dropIn {
      0% { opacity: 0; transform: translateX(-50%) translateY(calc(var(--y) - 90px)) translateZ(var(--z)) scale(0.4) rotateX(-25deg); filter: blur(6px); }
      70% { opacity: 1; filter: blur(0); }
      100% { opacity: 1; transform: translateX(-50%) translateY(var(--y)) translateZ(var(--z)) scale(1); }
    }

    .bun-top {
      height: 54px;
      background: linear-gradient(180deg, #f0b429 0%, #e08612 55%, #c96b0c 100%);
      border-radius: 90px 90px 40px 40px / 70px 70px 28px 28px;
      --y: 18px; --z: 70px; --d: 0.55s;
    }
    .bun-top::after {
      content: "";
      position: absolute;
      inset: 10px 18% auto;
      height: 8px;
      background:
        radial-gradient(circle, #8b5a1a 0 2px, transparent 3px) 0 0 / 14px 8px,
        radial-gradient(circle, #8b5a1a 0 1.5px, transparent 2.5px) 7px 4px / 14px 8px;
      opacity: 0.55;
    }
    .lettuce {
      height: 22px;
      background: linear-gradient(90deg, #6fbf3b, #8fd84e, #5aa82f, #9ae05a, #6fbf3b);
      clip-path: polygon(0 40%, 8% 10%, 16% 45%, 24% 5%, 32% 48%, 40% 8%, 48% 50%, 56% 6%, 64% 46%, 72% 10%, 80% 48%, 88% 8%, 100% 42%, 100% 100%, 0 100%);
      --y: 48px; --z: 52px; --d: 0.45s;
      box-shadow: 0 6px 12px rgba(40,100,20,0.25);
    }
    .cheese {
      height: 16px;
      background: linear-gradient(180deg, #ffd54a, #f0a800);
      border-radius: 8px;
      width: 92%;
      --y: 62px; --z: 40px; --d: 0.35s;
      clip-path: polygon(0 0, 100% 0, 100% 55%, 88% 100%, 72% 60%, 55% 100%, 40% 58%, 22% 100%, 10% 62%, 0 90%);
    }
    .patty {
      height: 28px;
      background:
        radial-gradient(circle at 30% 40%, rgba(255,180,100,0.35), transparent 40%),
        linear-gradient(180deg, #7a3b1a, #4a2210 55%, #3a180c);
      border-radius: 40px;
      --y: 82px; --z: 28px; --d: 0.25s;
    }
    .sauce {
      height: 12px;
      background: linear-gradient(90deg, #e86a17, #ff3b3b, #e86a17);
      width: 78%;
      border-radius: 20px;
      --y: 100px; --z: 18px; --d: 0.18s;
      filter: saturate(1.2);
    }
    .bun-bot {
      height: 36px;
      background: linear-gradient(180deg, #efb03a 0%, #d4891a 40%, #b86b10 100%);
      border-radius: 30px 30px 70px 70px / 20px 20px 50px 50px;
      --y: 118px; --z: 8px; --d: 0.08s;
    }

    .steam {
      position: absolute;
      left: 50%;
      top: 8%;
      width: 120px;
      height: 90px;
      transform: translateX(-50%);
      pointer-events: none;
      opacity: 0;
    }
    #stage.in .steam { opacity: 1; }
    .steam span {
      position: absolute;
      bottom: 0;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: rgba(255,255,255,0.55);
      filter: blur(6px);
      animation: steamUp 2.4s ease-in-out infinite;
    }
    .steam span:nth-child(1) { left: 20%; animation-delay: 0s; }
    .steam span:nth-child(2) { left: 45%; width: 24px; height: 24px; animation-delay: 0.4s; }
    .steam span:nth-child(3) { left: 68%; animation-delay: 0.8s; }
    @keyframes steamUp {
      0% { transform: translateY(20px) scale(0.6); opacity: 0; }
      30% { opacity: 0.7; }
      100% { transform: translateY(-70px) scale(1.4); opacity: 0; }
    }

    .crumb {
      position: absolute;
      width: 8px;
      height: 8px;
      border-radius: 2px;
      background: #e08612;
      opacity: 0;
      pointer-events: none;
    }
    #stage.in .crumb {
      animation: crumbFall 1.6s cubic-bezier(0.22,1,0.36,1) forwards;
      animation-delay: var(--d);
    }
    @keyframes crumbFall {
      0% { opacity: 0; transform: translate(0,-40px) rotate(0deg); }
      20% { opacity: 1; }
      100% { opacity: 0.85; transform: translate(var(--tx), var(--ty)) rotate(220deg); }
    }

    .burst {
      position: absolute;
      inset: 0;
      pointer-events: none;
      opacity: 0;
      background:
        radial-gradient(circle at 50% 48%, rgba(255,200,80,0.55), transparent 28%),
        radial-gradient(circle at 50% 48%, rgba(232,106,23,0.25), transparent 48%);
      transition: opacity 0.35s ease;
    }
    #stage.hot .burst { opacity: 1; animation: pulse 1.2s ease-in-out infinite; }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.7; }
      50% { transform: scale(1.06); opacity: 1; }
    }

    .floaters {
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
    }
    .floater {
      position: absolute;
      font-size: 1.4rem;
      filter: drop-shadow(0 6px 10px rgba(0,0,0,0.15));
      animation: floaty 5s ease-in-out infinite;
      opacity: 0.85;
    }
    @keyframes floaty {
      0%, 100% { transform: translateY(0) rotate(-6deg); }
      50% { transform: translateY(-16px) rotate(8deg); }
    }

    @media (prefers-reduced-motion: reduce) {
      .layer, .steam span, .crumb, .floater, .burst { animation: none !important; }
      #stage.in .layer { opacity: 1; transform: translateX(-50%) translateY(var(--y)) translateZ(var(--z)) scale(1); }
    }
  </style>
</head>
<body>
  <div id="stage">
    <div class="burst" aria-hidden="true"></div>
    <div class="label">
      <div class="kicker">Watch it build</div>
      <p class="title">Properly<br>loaded</p>
    </div>
    <div class="hint" id="hint">Hover to tilt</div>
    <div class="floaters" aria-hidden="true">
      <span class="floater" style="left:8%; top:28%; animation-delay:0s">🔥</span>
      <span class="floater" style="left:86%; top:34%; animation-delay:0.6s">🧀</span>
      <span class="floater" style="left:12%; top:68%; animation-delay:1.1s">🌶️</span>
      <span class="floater" style="left:82%; top:72%; animation-delay:1.7s">✨</span>
    </div>
    <div class="world">
      <div class="bite" id="bite">
        <div class="steam" aria-hidden="true"><span></span><span></span><span></span></div>
        <div class="layer bun-top"></div>
        <div class="layer lettuce"></div>
        <div class="layer cheese"></div>
        <div class="layer patty"></div>
        <div class="layer sauce"></div>
        <div class="layer bun-bot"></div>
        <div class="crumb" style="left:22%; top:30%; --tx:-40px; --ty:70px; --d:0.7s"></div>
        <div class="crumb" style="left:70%; top:24%; --tx:50px; --ty:80px; --d:0.85s; background:#f0b429"></div>
        <div class="crumb" style="left:48%; top:18%; --tx:10px; --ty:95px; --d:1s; background:#fff"></div>
      </div>
    </div>
  </div>

  <script>
    (() => {
      const stage = document.getElementById("stage");
      const bite = document.getElementById("bite");
      const hint = document.getElementById("hint");
      let hover = false;
      let mx = 0, my = 0;

      const fit = () => {
        try {
          if (window.frameElement) {
            window.frameElement.style.height = Math.max(380, stage.clientHeight) + "px";
          }
        } catch (_) {}
      };
      new ResizeObserver(fit).observe(stage);
      fit();

      new IntersectionObserver(
        (entries) => {
          entries.forEach((e) => {
            if (e.isIntersecting) stage.classList.add("in");
          });
        },
        { threshold: 0.28 }
      ).observe(stage);

      stage.addEventListener("pointerenter", () => {
        hover = true;
        stage.classList.add("hot");
        hint.textContent = "Move to orbit";
      });
      stage.addEventListener("pointerleave", () => {
        hover = false;
        stage.classList.remove("hot");
        hint.textContent = "Hover to tilt";
        mx = 0; my = 0;
      });
      stage.addEventListener("pointermove", (e) => {
        const r = stage.getBoundingClientRect();
        mx = ((e.clientX - r.left) / r.width) * 2 - 1;
        my = ((e.clientY - r.top) / r.height) * 2 - 1;
      });

      // Click = rebuild burst
      stage.addEventListener("click", () => {
        stage.classList.remove("in");
        void stage.offsetWidth;
        stage.classList.add("in");
      });

      let t = 0;
      const tick = () => {
        t += 0.016;
        const idleY = Math.sin(t * 0.9) * 4;
        const idleX = Math.cos(t * 0.7) * 3;
        const rx = 18 + (hover ? my * -18 : idleY * 0.3);
        const ry = -18 + (hover ? mx * 28 : idleX * 0.4);
        const rz = hover ? mx * -6 : 0;
        bite.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg) rotateZ(${rz}deg) translateY(${hover ? my * -8 : idleY}px)`;
        requestAnimationFrame(tick);
      };
      tick();
    })();
  </script>
</body>
</html>
'''



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
      @keyframes ftMarquee {
        from { transform: translateX(0); }
        to { transform: translateX(-50%); }
      }
      @keyframes ftWordIn {
        from { opacity: 0; transform: translateY(110%) rotateX(-40deg); filter: blur(8px); }
        to { opacity: 1; transform: translateY(0) rotateX(0); filter: blur(0); }
      }
      @keyframes ftGlowPulse {
        0%, 100% { text-shadow: 0 0 0 transparent; }
        50% { text-shadow: 0 0 28px rgba(232,106,23,0.35); }
      }

      .ft-marquee {
        position: relative;
        overflow: hidden;
        margin: 0.4rem 0 1.4rem;
        border-block: 1px solid rgba(232,106,23,0.2);
        background: linear-gradient(90deg, rgba(240,180,41,0.18), rgba(232,106,23,0.12), rgba(240,180,41,0.18));
        padding: 0.85rem 0;
        mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
      }
      .ft-marquee-track {
        display: flex;
        width: max-content;
        gap: 0;
        animation: ftMarquee 22s linear infinite;
      }
      .ft-marquee-track span {
        font-family: var(--ft-display);
        font-weight: 800;
        font-size: clamp(1rem, 2.2vw, 1.35rem);
        letter-spacing: -0.03em;
        text-transform: uppercase;
        white-space: nowrap;
        padding: 0 1.4rem;
        color: var(--ft-ink);
      }
      .ft-marquee-track span i {
        font-style: normal;
        color: var(--ft-orange);
        margin: 0 0.85rem;
      }

      .ft-headline .ft-word {
        display: inline-block;
        overflow: hidden;
        vertical-align: bottom;
        perspective: 600px;
      }
      .ft-headline .ft-word > span {
        display: inline-block;
        animation: ftWordIn 0.85s cubic-bezier(0.22, 1, 0.36, 1) both;
        animation-delay: var(--d, 0s);
      }
      .ft-headline {
        animation: ftGlowPulse 3.5s ease-in-out 1.2s infinite;
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
      .ft-in { animation: ftRise 0.85s cubic-bezier(0.22, 1, 0.36, 1) backwards; }
      .ft-section.ft-in { animation-name: ftSlideIn; }
      .ft-card.ft-in { animation-name: ftPop; }
      .ft-lead.ft-in, .ft-body.ft-in { animation-name: ftBlurIn; }
      @keyframes ftRise {
        from { opacity: 0; transform: translateY(36px) scale(0.98); }
      }
      @keyframes ftSlideIn {
        from { opacity: 0; transform: translateX(-28px) skewX(-4deg); filter: blur(6px); }
      }
      @keyframes ftPop {
        from { opacity: 0; transform: translateY(28px) scale(0.92); filter: blur(4px); }
      }
      @keyframes ftBlurIn {
        from { opacity: 0; filter: blur(10px); transform: translateY(18px); }
      }
      @media (prefers-reduced-motion: reduce) {
        .ft-reveal:not(.ft-in) { opacity: 1; }
        .ft-in, .ft-arrow, .ft-hero-glass::before, .ft-marquee-track, .ft-headline .ft-word > span, .ft-headline { animation: none; }
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
      <h1 class="ft-headline">
        <span class="ft-word"><span style="--d:0.05s">Future</span></span><br>
        <span class="ft-word"><span style="--d:0.18s">of</span></span><br>
        <span class="ft-word"><span style="--d:0.3s">street</span></span><br>
        <span class="ft-word"><span style="--d:0.42s">dining</span></span>
      </h1>
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
    <div class="ft-marquee" aria-hidden="true">
      <div class="ft-marquee-track">
        <span>Loaded bites <i>•</i> Hot sauce <i>•</i> Melted cheese <i>•</i> Bath streets <i>•</i> Cooked to order <i>•</i> Properly loaded <i>•</i></span>
        <span>Loaded bites <i>•</i> Hot sauce <i>•</i> Melted cheese <i>•</i> Bath streets <i>•</i> Cooked to order <i>•</i> Properly loaded <i>•</i></span>
      </div>
    </div>
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
        transform: translateY(-10px) scale(1.02) rotate(-0.4deg);
        box-shadow: 0 28px 56px rgba(120, 55, 10, 0.22), inset 0 1px 0 rgba(255, 240, 200, 0.85);
      }
      .bit.in .bit-words {
        animation: bitTitle 0.9s cubic-bezier(0.22, 1, 0.36, 1) both;
        animation-delay: inherit;
      }
      @keyframes bitTitle {
        from { opacity: 0; letter-spacing: 0.2em; transform: translateY(18px); filter: blur(8px); }
        to { opacity: 1; letter-spacing: -0.04em; transform: translateY(0); filter: blur(0); }
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

# --- TikTok-style loaded bite build (hover tilt, scroll assemble) ---
show_html(
    """
    <p class="ft-section">The loaded drop</p>
    <p class="ft-lead">
      Scroll in and watch a properly loaded bite assemble — hover to tilt it in 3D, click to rebuild.
    </p>
    """
)
components.html(
    bite_show_html(),
    height=400,
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
