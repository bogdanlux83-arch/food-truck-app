from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


def bite_show_html() -> str:
    return '''<!DOCTYPE html>
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
      border: 1px solid rgba(232, 106, 23, 0.28);
      background:
        radial-gradient(ellipse 70% 55% at 50% 78%, rgba(0,0,0,0.4), transparent 60%),
        radial-gradient(circle at 20% 20%, rgba(232,106,23,0.18), transparent 40%),
        linear-gradient(160deg, #140e0a 0%, #27180f 45%, #3d2414 100%);
      box-shadow: 0 20px 50px rgba(40, 20, 8, 0.28);
      cursor: grab;
      transform: translateY(48px) scale(0.94);
      opacity: 0;
      transition: opacity 0.9s cubic-bezier(0.22,1,0.36,1), transform 0.9s cubic-bezier(0.22,1,0.36,1), box-shadow 0.35s ease;
    }
    #stage.in { opacity: 1; transform: translateY(0) scale(1); }
    #stage:active { cursor: grabbing; }
    #stage.hot {
      box-shadow: 0 32px 70px rgba(232,106,23,0.42), 0 0 0 1px rgba(255,180,80,0.25) inset;
    }

    canvas#fx {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 6;
    }

    .label {
      position: absolute;
      left: 1.25rem;
      top: 1.15rem;
      z-index: 7;
      pointer-events: none;
      color: #fff8e8;
    }
    .label .kicker {
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(255,230,170,0.75);
      opacity: 0;
      transform: translateY(10px);
    }
    #stage.in .label .kicker {
      animation: textPop 0.7s 0.15s cubic-bezier(0.22,1,0.36,1) forwards;
    }
    .label .title {
      margin: 0.25rem 0 0;
      font-family: Syne, sans-serif;
      font-size: clamp(1.45rem, 3.2vw, 2.1rem);
      font-weight: 800;
      letter-spacing: -0.045em;
      text-transform: uppercase;
      line-height: 0.92;
    }
    .label .title span {
      display: inline-block;
      opacity: 0;
      transform: translateY(120%) rotateX(-50deg);
      filter: blur(8px);
    }
    #stage.in .label .title span {
      animation: wordSlam 0.85s cubic-bezier(0.22, 1.2, 0.36, 1) forwards;
      animation-delay: var(--d);
    }
    @keyframes wordSlam {
      to { opacity: 1; transform: translateY(0) rotateX(0); filter: blur(0); }
    }
    @keyframes textPop {
      to { opacity: 1; transform: translateY(0); }
    }

    .hint {
      position: absolute;
      right: 1.25rem;
      top: 1.25rem;
      z-index: 7;
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: rgba(255,230,170,0.45);
      pointer-events: none;
      transition: color 0.3s ease, transform 0.3s ease;
    }
    #stage.hot .hint {
      color: rgba(255,230,170,0.9);
      transform: scale(1.06);
    }

    .world {
      position: absolute;
      inset: 0;
      display: grid;
      place-items: center;
      perspective: 1200px;
      transform-style: preserve-3d;
    }

    .rig {
      position: relative;
      width: min(460px, 84vw);
      height: min(320px, 62vw);
      transform-style: preserve-3d;
      transform: rotateX(12deg) rotateY(-16deg);
    }

    .shock {
      position: absolute;
      left: 50%;
      top: 52%;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      border: 2px solid rgba(255,180,80,0.7);
      transform: translate(-50%, -50%) scale(0.2);
      opacity: 0;
      pointer-events: none;
      z-index: 5;
    }
    #stage.in .shock,
    #stage.boom .shock {
      animation: shockwave 0.9s cubic-bezier(0.22,1,0.36,1) forwards;
    }
    #stage.boom .shock { animation-delay: 0s; }
    @keyframes shockwave {
      0% { opacity: 0.9; transform: translate(-50%, -50%) scale(0.2); }
      100% { opacity: 0; transform: translate(-50%, -50%) scale(6.5); border-width: 0; }
    }

    .plate {
      position: absolute;
      left: 50%;
      bottom: 3%;
      width: 84%;
      height: 22%;
      transform: translateX(-50%) rotateX(72deg);
      border-radius: 50%;
      background: radial-gradient(ellipse at center, rgba(255,255,255,0.22), rgba(255,255,255,0.03) 55%, transparent 70%);
      box-shadow: 0 30px 40px rgba(0,0,0,0.5);
      opacity: 0;
    }
    #stage.in .plate {
      animation: fadeUp 0.85s 0.2s cubic-bezier(0.22,1,0.36,1) forwards;
    }

    .panini {
      position: absolute;
      inset: 12% 9% 22%;
      border-radius: 18px;
      overflow: hidden;
      transform-style: preserve-3d;
      box-shadow:
        0 28px 50px rgba(0,0,0,0.55),
        0 2px 0 rgba(255,200,120,0.15) inset;
      opacity: 0;
      transform: translateY(-120%) rotate(-8deg) scale(0.7);
      background:
        #111
        url("https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=1400&q=85")
        center 40% / cover no-repeat;
      z-index: 2;
    }
    #stage.in .panini {
      animation: paniniSlam 1.15s 0.25s cubic-bezier(0.18, 1.4, 0.3, 1) forwards;
    }
    #stage.hot .panini {
      filter: saturate(1.12) contrast(1.05) brightness(1.05);
      box-shadow:
        0 32px 60px rgba(0,0,0,0.6),
        0 0 40px rgba(255,140,40,0.25),
        0 2px 0 rgba(255,200,120,0.2) inset;
    }
    @keyframes paniniSlam {
      0% { opacity: 0; transform: translateY(-130%) rotate(-12deg) scale(0.65); filter: blur(10px); }
      55% { opacity: 1; filter: blur(0); transform: translateY(8%) rotate(2deg) scale(1.04); }
      75% { transform: translateY(-3%) rotate(-1deg) scale(0.99); }
      100% { opacity: 1; transform: translateY(0) rotate(0) scale(1); filter: blur(0); }
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateX(-50%) rotateX(72deg) scale(0.75); }
      to { opacity: 1; transform: translateX(-50%) rotateX(72deg) scale(1); }
    }

    .panini::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(180deg, rgba(255,200,120,0.14), transparent 30%),
        linear-gradient(120deg, transparent 40%, rgba(255,140,40,0.14), transparent 70%);
      pointer-events: none;
      mix-blend-mode: soft-light;
    }
    .panini::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(105deg, transparent 30%, rgba(255,255,255,0.28) 48%, transparent 62%);
      transform: translateX(-130%);
      animation: sheen 2.8s 1.1s ease-in-out infinite;
      pointer-events: none;
    }
    @keyframes sheen {
      0%, 100% { transform: translateX(-130%); }
      40%, 55% { transform: translateX(130%); }
    }

    .drip {
      position: absolute;
      width: 10px;
      height: 10px;
      border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
      background: linear-gradient(180deg, #f0b429, #e86a17);
      left: 58%;
      top: 68%;
      opacity: 0;
      z-index: 3;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.35));
    }
    #stage.in .drip {
      animation: sauceDrip 2.2s 1.1s ease-in infinite;
    }
    .drip:nth-child(2) { left: 46%; animation-delay: 1.45s !important; width: 8px; height: 8px; }
    .drip:nth-child(3) { left: 63%; animation-delay: 1.8s !important; width: 7px; height: 7px; }
    @keyframes sauceDrip {
      0% { opacity: 0; transform: translateY(0) scaleY(0.6); }
      15% { opacity: 1; }
      70% { opacity: 0.9; transform: translateY(42px) scaleY(1.6); }
      100% { opacity: 0; transform: translateY(70px) scaleY(0.4); }
    }

    .slice {
      position: absolute;
      width: 34%;
      aspect-ratio: 1 / 1.05;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 16px 32px rgba(0,0,0,0.45);
      background:
        url("https://images.pexels.com/photos/1893556/pexels-photo-1893556.jpeg?auto=compress&cs=tinysrgb&w=900")
        center / cover no-repeat;
      opacity: 0;
      z-index: 3;
    }
    .slice-a {
      left: -6%;
      top: 10%;
      --rest: rotate(-12deg) translateY(0) translateZ(36px) scale(1);
      transform: rotate(-28deg) translate(-40px, 60px) scale(0.7);
    }
    .slice-b {
      right: -6%;
      top: 20%;
      --rest: rotate(11deg) translateY(0) translateZ(24px) scale(1);
      transform: rotate(28deg) translate(40px, 70px) scale(0.7);
      background-position: 65% center;
    }
    #stage.in .slice-a {
      animation: sliceFly 1.05s 0.55s cubic-bezier(0.22,1.25,0.36,1) forwards;
    }
    #stage.in .slice-b {
      animation: sliceFly 1.05s 0.7s cubic-bezier(0.22,1.25,0.36,1) forwards;
    }
    @keyframes sliceFly {
      0% { opacity: 0; filter: blur(8px); }
      100% { opacity: 1; filter: blur(0); transform: var(--rest); }
    }

    .orbit {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 4;
    }
    .orb {
      position: absolute;
      font-size: 1.55rem;
      filter: drop-shadow(0 8px 12px rgba(0,0,0,0.35));
      opacity: 0;
      offset-path: path("M 80,160 C 40,40 420,40 380,160 C 420,280 40,280 80,160");
      offset-rotate: 0deg;
    }
    #stage.in .orb {
      animation: orbitSpin 8s linear infinite, orbIn 0.6s ease forwards;
      animation-delay: var(--d), var(--d);
    }
    @keyframes orbIn { to { opacity: 0.95; } }
    @keyframes orbitSpin {
      from { offset-distance: 0%; }
      to { offset-distance: 100%; }
    }
    @supports not (offset-path: path("M0,0")) {
      .orb { left: var(--x); top: var(--y); animation: floaty 4.5s ease-in-out infinite, orbIn 0.6s ease forwards !important; }
      @keyframes floaty {
        0%, 100% { transform: translateY(0) rotate(-8deg) scale(1); }
        50% { transform: translateY(-18px) rotate(10deg) scale(1.08); }
      }
    }

    .steam {
      position: absolute;
      left: 50%;
      top: 0;
      width: 180px;
      height: 110px;
      transform: translateX(-50%);
      pointer-events: none;
      opacity: 0;
      z-index: 4;
    }
    #stage.in .steam { opacity: 1; }
    .steam span {
      position: absolute;
      bottom: 0;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(255,240,210,0.5);
      filter: blur(9px);
      animation: steamUp 2.2s ease-in-out infinite;
    }
    .steam span:nth-child(1) { left: 14%; }
    .steam span:nth-child(2) { left: 38%; width: 32px; height: 32px; animation-delay: 0.35s; }
    .steam span:nth-child(3) { left: 58%; animation-delay: 0.7s; }
    .steam span:nth-child(4) { left: 74%; width: 20px; height: 20px; animation-delay: 1s; }
    @keyframes steamUp {
      0% { transform: translateY(16px) scale(0.5); opacity: 0; }
      25% { opacity: 0.75; }
      100% { transform: translateY(-90px) scale(1.7); opacity: 0; }
    }

    .haze {
      position: absolute;
      inset: 8% 12% 18%;
      border-radius: 24px;
      pointer-events: none;
      z-index: 3;
      background: linear-gradient(180deg, transparent, rgba(255,180,80,0.08), transparent);
      mix-blend-mode: screen;
      opacity: 0;
    }
    #stage.in .haze {
      opacity: 1;
      animation: hazeWave 3s ease-in-out infinite;
    }
    @keyframes hazeWave {
      0%, 100% { transform: translateY(0) scaleY(1); opacity: 0.35; }
      50% { transform: translateY(-8px) scaleY(1.08); opacity: 0.7; }
    }

    .glow {
      position: absolute;
      inset: 16% 12% 18%;
      border-radius: 40%;
      background: radial-gradient(circle, rgba(255,160,60,0.4), transparent 65%);
      filter: blur(20px);
      opacity: 0;
      pointer-events: none;
      z-index: 0;
      transition: opacity 0.35s ease;
    }
    #stage.hot .glow { opacity: 1; animation: pulse 1.15s ease-in-out infinite; }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.55; }
      50% { transform: scale(1.12); opacity: 1; }
    }

    .chip {
      position: absolute;
      bottom: 1.1rem;
      left: 1.25rem;
      z-index: 7;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(255,230,170,0.7);
      pointer-events: none;
      opacity: 0;
    }
    #stage.in .chip {
      animation: textPop 0.7s 0.9s cubic-bezier(0.22,1,0.36,1) forwards;
    }

    @media (max-width: 560px) {
      .slice { display: none; }
      .panini { inset: 14% 8% 24%; }
      .orb { font-size: 1.2rem; }
    }

    @media (prefers-reduced-motion: reduce) {
      .panini, .slice, .plate, .steam span, .panini::after, .glow, .shock, .drip, .orb, .haze,
      .label .title span, .label .kicker, .chip { animation: none !important; }
      #stage.in .panini, #stage.in .slice, #stage.in .plate, #stage.in .label .title span,
      #stage.in .label .kicker, #stage.in .chip, #stage.in .orb { opacity: 1; filter: none; transform: none; }
    }
  </style>
</head>
<body>
  <div id="stage">
    <canvas id="fx"></canvas>
    <div class="label">
      <div class="kicker">Properly loaded</div>
      <p class="title">
        <span style="--d:0.2s">Loaded</span><br>
        <span style="--d:0.38s">fries</span>
      </p>
    </div>
    <div class="hint" id="hint">Hover to tilt</div>
    <div class="chip">Slam-in · steam · sparks · click to rebuild</div>
    <div class="world">
      <div class="rig" id="rig">
        <div class="glow" aria-hidden="true"></div>
        <div class="shock" aria-hidden="true"></div>
        <div class="steam" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
        <div class="haze" aria-hidden="true"></div>
        <div class="plate" aria-hidden="true"></div>
        <div class="orbit" aria-hidden="true">
          <span class="orb" style="--d:0.8s; --x:10%; --y:30%">🍟</span>
          <span class="orb" style="--d:1.0s; --x:86%; --y:28%">🧀</span>
          <span class="orb" style="--d:1.15s; --x:12%; --y:70%">🥓</span>
          <span class="orb" style="--d:1.3s; --x:84%; --y:68%">✨</span>
          <span class="orb" style="--d:1.4s; --x:48%; --y:8%">🧂</span>
        </div>
        <div class="slice slice-a" aria-hidden="true"></div>
        <div class="slice slice-b" aria-hidden="true"></div>
        <div class="panini fries" role="img" aria-label="Loaded fries">
          <i class="drip"></i><i class="drip"></i><i class="drip"></i>
        </div>
      </div>
    </div>
  </div>
  <script>
    (() => {
      const stage = document.getElementById("stage");
      const rig = document.getElementById("rig");
      const hint = document.getElementById("hint");
      const canvas = document.getElementById("fx");
      const ctx = canvas.getContext("2d");
      let hover = false, mx = 0, my = 0;
      let particles = [];
      let w = 0, h = 0;

      const resize = () => {
        w = stage.clientWidth;
        h = stage.clientHeight;
        const dpr = window.devicePixelRatio || 1;
        canvas.width = Math.floor(w * dpr);
        canvas.height = Math.floor(h * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        try {
          if (window.frameElement) {
            window.frameElement.style.height = Math.max(420, h) + "px";
          }
        } catch (_) {}
      };
      new ResizeObserver(resize).observe(stage);
      resize();

      const burst = (count = 48, power = 1) => {
        const cx = w * 0.5;
        const cy = h * 0.52;
        for (let i = 0; i < count; i++) {
          const a = Math.random() * Math.PI * 2;
          const sp = (2.2 + Math.random() * 5.5) * power;
          particles.push({
            x: cx + (Math.random() - 0.5) * 40,
            y: cy + (Math.random() - 0.5) * 20,
            vx: Math.cos(a) * sp,
            vy: Math.sin(a) * sp - 1.5,
            life: 1,
            decay: 0.012 + Math.random() * 0.02,
            size: 2 + Math.random() * 4,
            color: Math.random() > 0.45
              ? `hsla(${28 + Math.random() * 28}, 95%, ${55 + Math.random() * 20}%, `
              : `hsla(${45 + Math.random() * 15}, 90%, ${65 + Math.random() * 15}%, `,
            spin: (Math.random() - 0.5) * 0.4,
            rot: Math.random() * Math.PI,
          });
        }
      };

      const crumbRain = () => {
        for (let i = 0; i < 18; i++) {
          particles.push({
            x: w * (0.25 + Math.random() * 0.5),
            y: h * 0.15,
            vx: (Math.random() - 0.5) * 1.5,
            vy: 1 + Math.random() * 2.5,
            life: 1,
            decay: 0.008 + Math.random() * 0.01,
            size: 2 + Math.random() * 3,
            color: `hsla(${30 + Math.random() * 20}, 80%, ${50 + Math.random() * 20}%, `,
            spin: (Math.random() - 0.5) * 0.3,
            rot: 0,
          });
        }
      };

      new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            stage.classList.add("in");
            setTimeout(() => burst(56, 1.15), 700);
            setTimeout(crumbRain, 900);
          }
        });
      }, { threshold: 0.25 }).observe(stage);

      stage.addEventListener("pointerenter", () => {
        hover = true;
        stage.classList.add("hot");
        hint.textContent = "Move to orbit";
        burst(14, 0.55);
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
        if (Math.random() > 0.82) {
          particles.push({
            x: e.clientX - r.left,
            y: e.clientY - r.top,
            vx: (Math.random() - 0.5) * 1.2,
            vy: -1 - Math.random(),
            life: 1,
            decay: 0.03,
            size: 1.5 + Math.random() * 2,
            color: `hsla(${35 + Math.random() * 25}, 95%, 60%, `,
            spin: 0.2,
            rot: 0,
          });
        }
      });
      stage.addEventListener("click", () => {
        stage.classList.remove("in", "boom");
        void stage.offsetWidth;
        stage.classList.add("in", "boom");
        burst(72, 1.35);
        setTimeout(crumbRain, 200);
        setTimeout(() => stage.classList.remove("boom"), 900);
      });

      let t = 0;
      const tick = () => {
        t += 0.016;
        const idleY = Math.sin(t * 0.9) * 3.5;
        const idleX = Math.cos(t * 0.7) * 2.8;
        const rx = 12 + (hover ? my * -18 : idleY * 0.3);
        const ry = -16 + (hover ? mx * 30 : idleX * 0.4);
        const rz = hover ? mx * -6 : Math.sin(t * 0.5) * 0.8;
        const ty = hover ? my * -8 : idleY;
        const sc = hover ? 1.03 : 1;
        rig.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg) rotateZ(${rz}deg) translateY(${ty}px) scale(${sc})`;

        ctx.clearRect(0, 0, w, h);
        particles = particles.filter((p) => p.life > 0);
        for (const p of particles) {
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.08;
          p.vx *= 0.99;
          p.rot += p.spin;
          p.life -= p.decay;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate(p.rot);
          ctx.fillStyle = p.color + Math.max(p.life, 0).toFixed(3) + ")";
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.7);
          ctx.restore();
        }
        requestAnimationFrame(tick);
      };
      tick();
    })();
  </script>
</body>
</html>
'''


def dome_show_html() -> str:
    """Igloo.inc-style cursor-reactive ice dome (Three.js)."""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
  <style>
    html, body {
      margin: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: transparent;
      font-family: "IBM Plex Mono", ui-monospace, monospace;
    }
    #wrap {
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 28px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,0.35);
      background:
        radial-gradient(ellipse 55% 40% at 50% 62%, rgba(255,255,255,0.55), transparent 55%),
        linear-gradient(180deg, #9ea4b0 0%, #b6bac5 42%, #8e94a0 100%);
      box-shadow:
        0 28px 60px rgba(40, 48, 70, 0.28),
        inset 0 1px 0 rgba(255,255,255,0.55),
        1px 0 0 rgba(255,80,80,0.12),
        -1px 0 0 rgba(80,180,255,0.12);
      cursor: crosshair;
    }
    canvas { display: block; width: 100%; height: 100%; }
    .hud {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 2;
      color: #111;
    }
    .hud-tl {
      position: absolute;
      top: 1.1rem;
      left: 1.2rem;
      font-size: 0.62rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-weight: 700;
      opacity: 0.75;
    }
    .hud-tr {
      position: absolute;
      top: 1.1rem;
      right: 1.2rem;
      text-align: right;
      font-size: 0.62rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-weight: 700;
      opacity: 0.7;
      max-width: 11rem;
      line-height: 1.45;
    }
    .hud-br {
      position: absolute;
      bottom: 1.15rem;
      right: 1.2rem;
      font-size: 0.62rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-weight: 700;
      opacity: 0.72;
    }
    .hud-bl {
      position: absolute;
      bottom: 1.15rem;
      left: 1.2rem;
      font-size: 0.62rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 700;
      opacity: 0.72;
    }
    .hud-bl em { font-style: normal; color: #c45a12; }
    .corner {
      position: absolute;
      width: 18px;
      height: 18px;
      border: 1.5px solid rgba(17,17,17,0.55);
      pointer-events: none;
    }
    .c-tl { top: 10px; left: 10px; border-right: 0; border-bottom: 0; }
    .c-tr { top: 10px; right: 10px; border-left: 0; border-bottom: 0; }
    .c-bl { bottom: 10px; left: 10px; border-right: 0; border-top: 0; }
    .c-br { bottom: 10px; right: 10px; border-left: 0; border-top: 0; }
    #nodes {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }
    .hint {
      position: absolute;
      left: 50%;
      top: 14%;
      transform: translateX(-50%);
      font-family: Syne, sans-serif;
      font-weight: 800;
      font-size: clamp(1.1rem, 2.4vw, 1.55rem);
      letter-spacing: -0.03em;
      text-transform: uppercase;
      color: rgba(17,17,17,0.88);
      text-shadow: 0 1px 0 rgba(255,255,255,0.4);
      z-index: 2;
      pointer-events: none;
      white-space: nowrap;
    }
  </style>
</head>
<body>
  <div id="wrap">
    <div class="corner c-tl"></div>
    <div class="corner c-tr"></div>
    <div class="corner c-bl"></div>
    <div class="corner c-br"></div>
    <div class="hint">Move cursor · lift blocks</div>
    <div class="hud">
      <div class="hud-tl">////// DOME_NODE_01</div>
      <div class="hud-tr">LoadedBites GLA<br>cursor-reactive ice</div>
      <div class="hud-bl">STATUS <em>LIVE</em></div>
      <div class="hud-br">[COOKED] [LOADED]</div>
    </div>
    <svg id="nodes" aria-hidden="true"></svg>
    <canvas id="c"></canvas>
  </div>
  <script type="importmap">
  {
    "imports": {
      "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js"
    }
  }
  </script>
  <script type="module">
    import * as THREE from "three";

    const wrap = document.getElementById("wrap");
    const canvas = document.getElementById("c");
    const nodesSvg = document.getElementById("nodes");

    const renderer = new THREE.WebGLRenderer({
      canvas,
      antialias: true,
      alpha: true,
      powerPreference: "high-performance",
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.15;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 80);
    camera.position.set(0, 2.35, 7.4);
    camera.lookAt(0, 0.85, 0);

    scene.add(new THREE.AmbientLight(0xc8cdd8, 0.55));
    const hemi = new THREE.HemisphereLight(0xe8ebf2, 0x6a7080, 0.85);
    scene.add(hemi);
    const key = new THREE.DirectionalLight(0xffffff, 1.05);
    key.position.set(4.5, 8, 3.5);
    scene.add(key);
    const rim = new THREE.DirectionalLight(0xb8d4ff, 0.45);
    rim.position.set(-5, 3, -4);
    scene.add(rim);
    const core = new THREE.PointLight(0xff9a3c, 3.2, 8, 1.6);
    core.position.set(0, 0.55, 0);
    scene.add(core);
    const core2 = new THREE.PointLight(0xffe8c0, 1.4, 5, 2);
    core2.position.set(0, 1.1, 0.2);
    scene.add(core2);

    // Ground frost disc
    const ground = new THREE.Mesh(
      new THREE.CircleGeometry(5.2, 64),
      new THREE.MeshStandardMaterial({
        color: 0x9aa1ad,
        roughness: 0.92,
        metalness: 0.05,
      })
    );
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -0.02;
    scene.add(ground);

    const R = 2.05;
    const blocks = [];
    const geo = new THREE.BoxGeometry(1, 1, 1);
    const matBase = {
      color: 0xaeb6c4,
      roughness: 0.28,
      metalness: 0.18,
      emissive: 0xffffff,
      emissiveIntensity: 0,
      transparent: true,
      opacity: 0.92,
    };

    function addBlock(x, y, z, sx, sy, sz, canMove) {
      const mat = new THREE.MeshStandardMaterial({ ...matBase });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.scale.set(sx, sy, sz);
      mesh.position.set(x, y, z);
      // Face outward slightly
      mesh.lookAt(x * 1.4, y, z * 1.4);
      mesh.rotation.x *= 0.15;
      const base = mesh.position.clone();
      const radial = new THREE.Vector3(x, y * 0.35, z).normalize();
      if (radial.lengthSq() < 0.01) radial.set(0, 1, 0);
      const phase = Math.random() * Math.PI * 2;
      const amp = 0.04 + Math.random() * 0.06;
      blocks.push({
        mesh,
        base,
        radial,
        phase,
        amp,
        canMove,
        target: 0,
        vel: 0,
        smooth: 0,
        rotAmp: (Math.random() - 0.5) * 0.12,
      });
      scene.add(mesh);
    }

    // Build hemispherical igloo of ice bricks
    const rings = [
      { y: 0.22, r: R * 0.98, n: 18, h: 0.38, d: 0.42, w: 0.55, move: false },
      { y: 0.58, r: R * 0.96, n: 17, h: 0.36, d: 0.4, w: 0.52, move: false },
      { y: 0.94, r: R * 0.9, n: 15, h: 0.34, d: 0.38, w: 0.5, move: true },
      { y: 1.28, r: R * 0.8, n: 13, h: 0.32, d: 0.36, w: 0.48, move: true },
      { y: 1.58, r: R * 0.66, n: 11, h: 0.3, d: 0.34, w: 0.46, move: true },
      { y: 1.84, r: R * 0.48, n: 9, h: 0.28, d: 0.32, w: 0.44, move: true },
      { y: 2.04, r: R * 0.28, n: 6, h: 0.26, d: 0.3, w: 0.4, move: true },
    ];
    rings.forEach((ring, ri) => {
      for (let i = 0; i < ring.n; i++) {
        // Door gap on front of lower rings
        const a0 = (i / ring.n) * Math.PI * 2 + ri * 0.12;
        if (ri < 2) {
          const front = Math.atan2(Math.sin(a0), Math.cos(a0));
          if (Math.abs(front) < 0.42) continue;
        }
        const x = Math.cos(a0) * ring.r;
        const z = Math.sin(a0) * ring.r;
        const jitter = (Math.random() - 0.5) * 0.04;
        addBlock(
          x + jitter,
          ring.y + (Math.random() - 0.5) * 0.03,
          z + jitter,
          ring.w * (0.9 + Math.random() * 0.2),
          ring.h * (0.9 + Math.random() * 0.15),
          ring.d * (0.9 + Math.random() * 0.2),
          ring.move
        );
      }
    });
    // Cap blocks
    for (let i = 0; i < 4; i++) {
      const a = (i / 4) * Math.PI * 2;
      addBlock(Math.cos(a) * 0.12, 2.22, Math.sin(a) * 0.12, 0.36, 0.22, 0.36, true);
    }
    addBlock(0, 2.38, 0, 0.42, 0.24, 0.42, true);

    // Inner warm glow orb
    const glow = new THREE.Mesh(
      new THREE.SphereGeometry(0.55, 24, 16),
      new THREE.MeshBasicMaterial({
        color: 0xffb060,
        transparent: true,
        opacity: 0.55,
        depthWrite: false,
      })
    );
    glow.position.set(0, 0.7, 0);
    scene.add(glow);

    // HUD node overlay
    const hudPts = [
      { x: 0.22, y: 0.28, n: "31" },
      { x: 0.72, y: 0.24, n: "29" },
      { x: 0.48, y: 0.38, n: "20" },
      { x: 0.34, y: 0.52, n: "14" },
      { x: 0.66, y: 0.48, n: "08" },
    ];
    function drawNodes() {
      const w = wrap.clientWidth;
      const h = wrap.clientHeight;
      let lines = "";
      for (let i = 0; i < hudPts.length - 1; i++) {
        const a = hudPts[i], b = hudPts[i + 1];
        lines += `<line x1="${a.x * w}" y1="${a.y * h}" x2="${b.x * w}" y2="${b.y * h}" stroke="rgba(17,17,17,0.28)" stroke-width="1"/>`;
      }
      const dots = hudPts.map((p) => `
        <g transform="translate(${p.x * w},${p.y * h})">
          <circle r="2.2" fill="rgba(17,17,17,0.55)"/>
          <text x="6" y="3" font-size="9" font-family="IBM Plex Mono, monospace" fill="rgba(17,17,17,0.55)">${p.n}</text>
        </g>`).join("");
      nodesSvg.setAttribute("viewBox", `0 0 ${w} ${h}`);
      nodesSvg.innerHTML = lines + dots;
    }

    const mouse = new THREE.Vector2(999, 999);
    const follow = new THREE.Vector3(0, 1.4, 2.2);
    const followTarget = new THREE.Vector3(0, 1.4, 2.2);
    const plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0);
    const raycaster = new THREE.Raycaster();
    const hit = new THREE.Vector3();
    // Interaction plane through igloo center, facing camera
    plane.setFromNormalAndCoplanarPoint(
      new THREE.Vector3(0, 0.15, 1).normalize(),
      new THREE.Vector3(0, 1.1, 0)
    );

    function onPointer(e) {
      const rect = canvas.getBoundingClientRect();
      mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
      raycaster.setFromCamera(mouse, camera);
      if (raycaster.ray.intersectPlane(plane, hit)) {
        followTarget.copy(hit);
      }
    }
    function onLeave() {
      followTarget.set(0, 1.2, 2.5);
    }
    wrap.addEventListener("pointermove", onPointer);
    wrap.addEventListener("pointerleave", onLeave);
    wrap.addEventListener("pointerdown", () => {
      blocks.forEach((b) => {
        if (!b.canMove) return;
        b.target = Math.max(b.target, 0.55 + Math.random() * 0.85);
      });
    });

    function resize() {
      const w = wrap.clientWidth;
      const h = wrap.clientHeight;
      renderer.setSize(w, h, false);
      camera.aspect = w / Math.max(h, 1);
      camera.updateProjectionMatrix();
      drawNodes();
    }
    resize();
    window.addEventListener("resize", resize);

    const clock = new THREE.Clock();
    function animate() {
      requestAnimationFrame(animate);
      const t = clock.getElapsedTime();
      follow.lerp(followTarget, 0.08);

      // Pulse core light
      core.intensity = 2.6 + Math.sin(t * 2.2) * 0.55;
      glow.material.opacity = 0.42 + Math.sin(t * 2.2) * 0.12;
      glow.scale.setScalar(1 + Math.sin(t * 1.6) * 0.06);

      blocks.forEach((b) => {
        let push = 0;
        if (b.canMove) {
          const dist = b.base.distanceTo(follow);
          if (dist < 1.05) push = 1;
          else if (dist < 2.85) push = 1 - (dist - 1.05) / 1.8;
          push = Math.max(0, push);
        }
        const idle = b.canMove ? (0.5 + 0.5 * Math.sin(t * 1.35 + b.phase + b.base.x * 0.8)) * b.amp * 2.2 : 0;
        const desired = Math.max(idle, push * (0.55 + b.amp * 4));
        // Double smoothing (igloo-like lag)
        b.vel += (desired - b.target) * 0.12;
        b.vel *= 0.82;
        b.target += b.vel;
        b.smooth += (b.target - b.smooth) * 0.16;

        const disp = b.radial.clone().multiplyScalar(b.smooth * 1.35);
        b.mesh.position.copy(b.base).add(disp);
        b.mesh.rotation.z = b.smooth * b.rotAmp;
        b.mesh.rotation.x = b.smooth * b.rotAmp * 0.6;
        b.mesh.material.emissiveIntensity = Math.min(1.4, b.smooth * 1.8);
        b.mesh.material.color.setRGB(
          0.68 + b.smooth * 0.28,
          0.72 + b.smooth * 0.22,
          0.78 + b.smooth * 0.18
        );
      });

      // Subtle camera drift toward follow
      camera.position.x += (follow.x * 0.08 - camera.position.x + 0) * 0.04;
      camera.position.y += (2.35 + follow.y * 0.04 - camera.position.y) * 0.04;
      camera.lookAt(0, 0.9, 0);

      renderer.render(scene, camera);
    }
    animate();
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
      @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Syne:wght@700;800&display=swap");

      :root {
        --ft-display: "Syne", sans-serif;
        --ft-sans: "IBM Plex Mono", ui-monospace, monospace;
        --ft-ink: #2a3040;
        --ft-muted: #5c6478;
        --ft-line: rgba(56, 62, 78, 0.18);
        --ft-paper: #b6bac5;
        --ft-panel: rgba(232, 235, 242, 0.55);
        --ft-orange: #e86a17;
        --ft-yellow: #f0b429;
        --ft-amber: #ff9f1c;
        --ft-ice: #e8ebf2;
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
          url("https://images.pexels.com/photos/2788792/pexels-photo-2788792.jpeg?auto=compress&cs=tinysrgb&w=2400")
          center 35% / cover no-repeat;
        transform: scale(1.1);
        filter: blur(var(--ft-sky-blur, 14px)) saturate(1.15) brightness(0.95) sepia(0.22) hue-rotate(-12deg);
        opacity: 0.34;
        will-change: filter, opacity;
      }
      .ft-sky-tint {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background:
          linear-gradient(180deg, rgba(182,186,197,0.55) 0%, rgba(182,186,197,0.82) 48%, #b6bac5 100%),
          radial-gradient(900px 480px at 70% 0%, rgba(255,255,255,0.35), transparent 55%),
          radial-gradient(700px 420px at 20% 60%, rgba(232,106,23,0.12), transparent 50%);
      }
      ::selection {
        background: #383e4e;
        color: #e8ebf2;
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

      /* Igloo-style instrument HUD */
      .ft-ghost {
        position: fixed;
        right: -2%;
        top: 18%;
        z-index: 0;
        pointer-events: none;
        font-family: var(--ft-sans);
        font-size: clamp(4rem, 14vw, 11rem);
        font-weight: 700;
        letter-spacing: -0.06em;
        text-transform: uppercase;
        color: rgba(255,255,255,0.08);
        transform: rotate(-12deg);
        white-space: nowrap;
        user-select: none;
      }
      .ft-frame {
        position: relative;
      }
      .ft-frame::before,
      .ft-frame::after {
        content: "";
        position: absolute;
        width: 14px;
        height: 14px;
        border: 1px solid rgba(42,48,64,0.55);
        pointer-events: none;
        z-index: 2;
      }
      .ft-frame::before {
        top: 10px; left: 10px;
        border-right: 0; border-bottom: 0;
      }
      .ft-frame::after {
        top: 10px; right: 10px;
        border-left: 0; border-bottom: 0;
      }
      .ft-frame .ft-corners-bl,
      .ft-frame .ft-corners-br {
        position: absolute;
        width: 14px;
        height: 14px;
        border: 1px solid rgba(42,48,64,0.55);
        pointer-events: none;
        z-index: 2;
      }
      .ft-frame .ft-corners-bl {
        bottom: 10px; left: 10px;
        border-right: 0; border-top: 0;
      }
      .ft-frame .ft-corners-br {
        bottom: 10px; right: 10px;
        border-left: 0; border-top: 0;
      }
      .ft-readout {
        font-family: var(--ft-sans) !important;
        font-size: 0.68rem;
        font-weight: 500;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--ft-muted);
      }
      .ft-readout em {
        font-style: normal;
        color: var(--ft-ink);
      }
      .ft-slash {
        opacity: 0.45;
        letter-spacing: 0.08em;
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
        border-block: 1px solid var(--ft-line);
        background: rgba(232,235,242,0.35);
        padding: 0.7rem 0;
        mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
      }
      .ft-marquee-track {
        display: flex;
        width: max-content;
        gap: 0;
        animation: ftMarquee 22s linear infinite;
      }
      .ft-marquee-track span {
        font-family: var(--ft-sans);
        font-weight: 600;
        font-size: 0.78rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        white-space: nowrap;
        padding: 0 1.4rem;
        color: var(--ft-ink);
      }
      .ft-marquee-track span i {
        font-style: normal;
        color: var(--ft-muted);
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
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.6rem;
        animation: ftHeroIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
      }
      .ft-top .ft-nav { justify-content: center; }
      .ft-top .ft-readout { justify-self: end; text-align: right; margin: 0; }
      .ft-logo {
        font-family: var(--ft-display) !important;
        font-style: normal;
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        text-transform: uppercase;
        color: var(--ft-ink);
        margin: 0;
        display: inline-block;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1), text-shadow 0.28s ease;
        transform-origin: left center;
        cursor: default;
      }
      .ft-logo:hover {
        transform: scale(1.04);
        text-shadow: 1px 0 0 rgba(255,80,80,0.45), -1px 0 0 rgba(80,180,255,0.45);
      }

      .ft-section,
      .ft-lead,
      .ft-body,
      .ft-card h3,
      .ft-card p,
      .ft-headline-aside,
      .ft-brand,
      .ft-sub,
      .ft-tag,
      .ft-footer,
      .ft-points span {
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
        transform-origin: left center;
      }
      .ft-section:hover,
      .ft-lead:hover,
      .ft-body:hover,
      .ft-card h3:hover,
      .ft-card p:hover,
      .ft-headline-aside:hover,
      .ft-brand:hover,
      .ft-sub:hover,
      .ft-tag:hover,
      .ft-footer:hover,
      .ft-points span:hover {
        transform: scale(1.045);
      }
      .ft-headline .ft-word > span {
        transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1);
        transform-origin: left bottom;
        cursor: default;
      }
      .ft-headline .ft-word > span:hover {
        transform: scale(1.06);
      }
      .ft-nav {
        display: flex;
        gap: 1.1rem;
        font-size: 0.72rem;
        font-weight: 500;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--ft-muted);
        font-family: var(--ft-sans) !important;
      }
      .ft-nav span { color: var(--ft-ink); }
      .ft-nav span::before { content: "["; opacity: 0.4; margin-right: 0.15rem; }
      .ft-nav span::after { content: "]"; opacity: 0.4; margin-left: 0.15rem; }

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
        font-size: 0.78rem;
        line-height: 1.65;
        color: var(--ft-muted);
        font-weight: 500;
        margin: 0 0 0.4rem;
        max-width: 18rem;
        letter-spacing: 0.02em;
        border-left: 1px solid var(--ft-line);
        padding-left: 1rem;
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
          linear-gradient(180deg, rgba(232,106,23,0.18) 0%, rgba(28,20,14,0.55) 100%),
          url("https://images.pexels.com/photos/2788792/pexels-photo-2788792.jpeg?auto=compress&cs=tinysrgb&w=2400")
          center 42% / cover no-repeat;
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
        background: linear-gradient(165deg, rgba(232,235,242,0.55), rgba(182,186,197,0.22));
        border: 1px solid rgba(255, 255, 255, 0.45);
        box-shadow:
          0 18px 40px rgba(20, 24, 40, 0.22),
          inset 0 1px 0 rgba(255, 255, 255, 0.65),
          1px 0 0 rgba(255,80,80,0.15), -1px 0 0 rgba(80,180,255,0.15);
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
        font-family: var(--ft-display) !important;
        font-size: clamp(1.7rem, 3.2vw, 2.4rem);
        font-weight: 800;
        font-style: normal;
        margin: 0 0 0.45rem 0;
        line-height: 1;
        letter-spacing: -0.04em;
        text-transform: uppercase;
        color: #ffffff;
        text-shadow: 1px 0 0 rgba(255,80,80,0.35), -1px 0 0 rgba(80,180,255,0.35);
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
        font-family: var(--ft-sans) !important;
        font-size: clamp(0.95rem, 1.6vw, 1.15rem);
        font-weight: 600;
        margin: 2.8rem 0 0.85rem;
        color: var(--ft-ink);
        letter-spacing: 0.14em;
        line-height: 1.2;
        text-transform: uppercase;
        display: block;
        padding: 0;
        border: 0;
        background: none;
        box-shadow: none;
        backdrop-filter: none;
      }
      .ft-section::before {
        content: "////// ";
        opacity: 0.35;
        letter-spacing: 0.02em;
      }
      .ft-section::after {
        content: "";
        display: block;
        width: 100%;
        max-width: 220px;
        height: 1px;
        background: linear-gradient(90deg, var(--ft-ink), transparent);
        margin-top: 0.65rem;
        opacity: 0.35;
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
        background: var(--ft-panel);
        border: 1px solid var(--ft-line);
        border-radius: 0;
        padding: 1.15rem 1.1rem 1.05rem;
        margin-bottom: 0.55rem;
        box-shadow: none;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: transform 0.25s ease, border-color 0.25s ease, background 0.25s ease;
      }
      .ft-card::before {
        content: "";
        position: absolute;
        top: 8px; left: 8px;
        width: 8px; height: 8px;
        border-top: 1px solid rgba(42,48,64,0.45);
        border-left: 1px solid rgba(42,48,64,0.45);
      }
      .ft-card:hover {
        transform: translateY(-2px);
        border-color: rgba(42,48,64,0.4);
        background: rgba(232,235,242,0.72);
        box-shadow: 1px 0 0 rgba(255,80,80,0.2), -1px 0 0 rgba(80,180,255,0.2);
      }
      .ft-card h3 {
        font-family: var(--ft-sans) !important;
        font-size: 0.82rem;
        font-weight: 700;
        margin: 0 0 0.45rem 0;
        padding: 0;
        color: var(--ft-ink);
        letter-spacing: 0.12em;
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
        font-family: var(--ft-display);
        font-size: 1.05rem;
        font-style: normal;
        font-weight: 800;
        letter-spacing: -0.03em;
        text-transform: uppercase;
        color: var(--ft-ink);
      }

      div[data-testid="stButton"] button,
      .stLinkButton a {
        border-radius: 2px !important;
        font-weight: 600 !important;
        font-size: 0.72rem !important;
        padding: 0.85rem 1.25rem !important;
        letter-spacing: 0.14em !important;
        text-transform: uppercase !important;
        background: rgba(232,235,242,0.65) !important;
        color: var(--ft-ink) !important;
        border: 1px solid rgba(42,48,64,0.45) !important;
        box-shadow: none !important;
        backdrop-filter: blur(8px) !important;
        transition: transform 0.25s ease, background 0.25s ease, color 0.25s ease, box-shadow 0.25s ease !important;
      }
      div[data-testid="stButton"] button p,
      .stLinkButton a p {
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        color: var(--ft-ink) !important;
        letter-spacing: 0.14em !important;
      }
      div[data-testid="stButton"] button:hover,
      .stLinkButton a:hover {
        background: #2a3040 !important;
        color: #e8ebf2 !important;
        border-color: #2a3040 !important;
        box-shadow: 1px 0 0 rgba(255,80,80,0.5), -1px 0 0 rgba(80,180,255,0.5) !important;
        transform: translateY(-1px) !important;
      }
      div[data-testid="stButton"] button:hover p,
      .stLinkButton a:hover p {
        color: #e8ebf2 !important;
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
        .ft-section:hover, .ft-lead:hover, .ft-body:hover, .ft-card h3:hover, .ft-card p:hover,
        .ft-headline-aside:hover, .ft-brand:hover, .ft-sub:hover, .ft-tag:hover, .ft-footer:hover,
        .ft-points span:hover, .ft-logo:hover, .ft-headline .ft-word > span:hover {
          transform: none;
        }
      }
      @media (max-width: 800px) {
        .ft-headline-row { grid-template-columns: 1fr; }
        .ft-nav, .ft-top .ft-readout { display: none; }
        .ft-top { grid-template-columns: 1fr; }
        .ft-hero { min-height: 54vh; border-radius: 26px; }
        .ft-ghost { opacity: 0.5; font-size: 4rem; }
      }
    </style>
    """
)

# --- Estato-style hero: big type + rounded Bath photo with glass title ---
show_html(
    """
    <div class="ft-sky" aria-hidden="true"></div>
    <div class="ft-sky-tint" aria-hidden="true"></div>
    <div class="ft-ghost" aria-hidden="true">LOADED</div>
    <div class="ft-top">
      <p class="ft-logo">LoadedBites</p>
      <div class="ft-nav">
        <span>Home</span>
        <span>Menu</span>
        <span>Bath</span>
        <span>Contact</span>
      </div>
      <p class="ft-readout">TEMP <em>68.4°F</em> · VENDOR_01</p>
    </div>
    <div class="ft-headline-row">
      <h1 class="ft-headline">
        <span class="ft-word"><span style="--d:0.05s">Future</span></span><br>
        <span class="ft-word"><span style="--d:0.18s">of</span></span><br>
        <span class="ft-word"><span style="--d:0.3s">street</span></span><br>
        <span class="ft-word"><span style="--d:0.42s">dining</span></span>
      </h1>
      <p class="ft-headline-aside">
        <span class="ft-slash">///</span> Scroll to discover<br><br>
        We craft generous, carefully prepared bites that bring lively energy to Bath’s streets.
      </p>
    </div>
    <p class="ft-scroll-hint"><span class="ft-arrow">↓</span> Move the cursor on the dome · scroll to discover</p>
    <div class="ft-marquee" aria-hidden="true">
      <div class="ft-marquee-track">
        <span>Loaded bites <i>•</i> Hot sauce <i>•</i> Melted cheese <i>•</i> Bath streets <i>•</i> Cooked to order <i>•</i> Properly loaded <i>•</i></span>
        <span>Loaded bites <i>•</i> Hot sauce <i>•</i> Melted cheese <i>•</i> Bath streets <i>•</i> Cooked to order <i>•</i> Properly loaded <i>•</i></span>
      </div>
    </div>
    """
)

# --- Igloo.inc-style interactive ice dome ---
components.html(
    dome_show_html(),
    height=560,
    scrolling=False,
)

# --- Three glass feature boxes ---
components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
    <style>
      html, body {
        margin: 0;
        background: transparent;
        font-family: "IBM Plex Mono", ui-monospace, monospace;
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
        border: 1px solid rgba(255, 255, 255, 0.4);
        background:
          linear-gradient(165deg, rgba(232,235,242,0.42), rgba(42,48,64,0.28)),
          url("https://images.pexels.com/photos/14494034/pexels-photo-14494034.jpeg?auto=compress&cs=tinysrgb&w=1200")
          center 40% / cover no-repeat;
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
          linear-gradient(165deg, rgba(232,235,242,0.42), rgba(42,48,64,0.28)),
          url("https://images.pexels.com/photos/14494034/pexels-photo-14494034.jpeg?auto=compress&cs=tinysrgb&w=1200")
          center 40% / cover no-repeat;
      }
      .bit-3 .bit-inner {
        background:
          linear-gradient(165deg, rgba(232,235,242,0.42), rgba(42,48,64,0.28)),
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
        font-family: "IBM Plex Mono", monospace;
        font-size: 0.62rem;
        font-weight: 600;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: rgba(232, 235, 242, 0.85);
        display: inline-block;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
        transform-origin: left center;
      }
      .bit-inner:hover .bit-kicker { transform: scale(1.05); }
      .bit-words {
        font-family: "Syne", sans-serif;
        font-size: clamp(1.35rem, 2vw, 1.75rem);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.05;
        text-transform: uppercase;
        color: #ffffff;
        margin: 0;
        display: inline-block;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
        transform-origin: left center;
      }
      .bit-inner:hover .bit-words { transform: scale(1.06); }
      .bit-sub {
        margin: 0;
        font-size: 0.9rem;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.85);
        letter-spacing: -0.01em;
        max-width: 22rem;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
        transform-origin: left center;
      }
      .bit-inner:hover .bit-sub { transform: scale(1.04); }
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

        // Igloo-style scramble on section hover
        if (!page.__ftScramble) {
          const glyphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_/";
          const scrambleEl = (el) => {
            if (el.dataset.scrambling) return;
            const original = el.dataset.original || el.textContent;
            el.dataset.original = original;
            el.dataset.scrambling = "1";
            let frame = 0;
            const total = 12;
            const tick = () => {
              frame += 1;
              el.textContent = original.split("").map((ch, i) => {
                if (ch === " " || ch === "\\n") return ch;
                if (frame / total > i / Math.max(original.length, 1)) return original[i];
                return glyphs[Math.floor(Math.random() * glyphs.length)];
              }).join("");
              if (frame < total) requestAnimationFrame(tick);
              else { el.textContent = original; delete el.dataset.scrambling; }
            };
            tick();
          };
          const bind = () => {
            doc.querySelectorAll(".ft-section, .ft-logo, .ft-card h3").forEach((el) => {
              if (el.dataset.scrambleBound) return;
              el.dataset.scrambleBound = "1";
              el.addEventListener("mouseenter", () => scrambleEl(el));
            });
          };
          const mo = new page.MutationObserver(bind);
          mo.observe(doc.body, { childList: true, subtree: true });
          page.__ftScramble = true;
          bind();
        }


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
    <p class="ft-section">The loaded fries</p>
    <p class="ft-lead">
      Scroll in for the slam — loaded fries, steam, sparks, and orbiting toppings. Hover to tilt, click to rebuild the drop.
    </p>
    """
)
components.html(
    bite_show_html(),
    height=440,
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
