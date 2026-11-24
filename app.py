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

show_html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
      :root {
        --ft-display: "Space Grotesk", sans-serif;
        --ft-sans: "Outfit", sans-serif;
      }

      html, body, .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"],
      [data-testid="stCaption"], [data-testid="stAlert"],
      div[data-testid="stButton"] button, .stLinkButton a {
        font-family: var(--ft-sans) !important;
      }

      html, body, .stApp {
        font-size: 18px;
        line-height: 1.4;
        -webkit-font-smoothing: antialiased;
        color: #1c1917;
      }

      .stApp {
        background:
          radial-gradient(1000px 520px at 8% -8%, #fef08a 0%, transparent 55%),
          radial-gradient(820px 460px at 92% 5%, #f9a8d4 0%, transparent 48%),
          radial-gradient(700px 400px at 50% 110%, #fecdd3 0%, transparent 50%),
          #fff1f2;
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2.2rem;
        padding-left: 1.4rem !important;
        padding-right: 1.4rem !important;
        max-width: 1400px;
      }

      @keyframes ftHeroIn {
        from { opacity: 0; transform: translateY(24px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
      }

      .ft-hero {
        background: linear-gradient(125deg, #be123c 0%, #e11d48 32%, #fb7185 62%, #fde047 100%);
        border-radius: 28px;
        padding: 3.2rem 2.8rem 2.8rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 18px 40px rgba(225, 29, 72, 0.28);
        animation: ftHeroIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
      }
      .ft-hero:hover {
        transform: scale(1.015);
        box-shadow: 0 22px 48px rgba(225, 29, 72, 0.34);
      }
      .ft-tag {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        background: #881337;
        color: #fef08a;
        padding: 0.4rem 0.8rem;
        border-radius: 999px;
        margin-bottom: 0.7rem;
        transition: transform 0.25s ease;
      }
      .ft-tag:hover { transform: scale(1.12); }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.5rem, 5.5vw, 3.6rem);
        font-weight: 700;
        margin: 0 0 0.45rem 0;
        line-height: 0.95;
        letter-spacing: -0.055em;
        color: #fff1f2;
        display: inline-block;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
      }
      .ft-brand:hover { transform: scale(1.08); }
      .ft-sub {
        margin: 0;
        font-size: 1.15rem;
        max-width: 40rem;
        line-height: 1.4;
        color: #ffe4e6;
        font-weight: 500;
        letter-spacing: -0.02em;
        transition: transform 0.28s ease;
        transform-origin: left center;
      }
      .ft-sub:hover { transform: scale(1.05); }
      .ft-scroll-hint {
        text-align: center;
        color: #9f1239;
        font-size: 0.95rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        margin: 0.4rem 0 0.2rem;
        opacity: 0.85;
        transition: transform 0.25s ease, opacity 0.25s ease;
      }
      .ft-scroll-hint:hover {
        transform: scale(1.1);
        opacity: 1;
      }
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(1.7rem, 3vw, 2.1rem);
        font-weight: 700;
        margin: 1.55rem 0 0.65rem;
        color: #be123c;
        letter-spacing: -0.05em;
        line-height: 1.05;
        display: inline-block;
        transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1);
      }
      .ft-section:hover { transform: scale(1.08); }
      .ft-lead {
        font-size: 1.12rem;
        line-height: 1.4;
        color: #44403c;
        font-weight: 400;
        letter-spacing: -0.02em;
        max-width: 56rem;
        margin: 0 0 0.65rem 0;
        transition: transform 0.28s ease;
        transform-origin: left top;
      }
      .ft-lead:hover { transform: scale(1.045); }
      .ft-body {
        font-size: 1.05rem;
        line-height: 1.4;
        color: #57534e;
        letter-spacing: -0.02em;
        max-width: 56rem;
        margin: 0 0 0.55rem 0;
        transition: transform 0.28s ease;
        transform-origin: left top;
      }
      .ft-body:hover { transform: scale(1.045); }
      .ft-card {
        background: rgba(255, 255, 255, 0.78);
        border: 2px solid rgba(251, 113, 133, 0.55);
        border-radius: 16px;
        padding: 1.05rem 1.1rem 0.9rem;
        margin-bottom: 0.7rem;
        box-shadow: 0 10px 28px rgba(225, 29, 72, 0.12);
        transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s ease;
      }
      .ft-card:hover {
        transform: scale(1.05);
        box-shadow: 0 16px 36px rgba(225, 29, 72, 0.2);
      }
      .ft-card h3 {
        font-family: var(--ft-display) !important;
        font-size: 1.2rem;
        font-weight: 700;
        margin: 0 0 0.3rem 0;
        color: #9f1239;
        letter-spacing: -0.04em;
      }
      .ft-card p {
        font-size: 0.95rem;
        line-height: 1.4;
        color: #57534e;
        margin: 0;
        letter-spacing: -0.02em;
      }
      .ft-footer {
        text-align: center;
        color: #9f1239;
        font-size: 0.92rem;
        margin-top: 2rem;
        padding-top: 1.1rem;
        border-top: 2px solid rgba(251, 113, 133, 0.45);
        font-weight: 500;
        line-height: 1.4;
        transition: transform 0.25s ease;
      }
      .ft-footer:hover { transform: scale(1.06); }
      div[data-testid="stButton"] button,
      .stLinkButton a {
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 1.02rem !important;
        padding: 0.65rem 1.15rem !important;
        letter-spacing: -0.02em !important;
        background: rgba(255, 228, 230, 0.7) !important;
        color: #9f1239 !important;
        border: 2px solid rgba(244, 63, 94, 0.75) !important;
        transition: transform 0.25s ease, background 0.25s ease !important;
      }
      div[data-testid="stButton"] button:hover,
      .stLinkButton a:hover {
        background: rgba(254, 240, 138, 0.85) !important;
        border-color: #e11d48 !important;
        transform: scale(1.06) !important;
      }
    </style>
    """
)

# --- Hero ---
show_html(
    """
    <div class="ft-hero">
      <div class="ft-tag">Bath food vend</div>
      <p class="ft-brand">LoadedBites GLA</p>
      <p class="ft-sub">
        Big flavour. Proper portions. Street food worth queuing for —
        cooked fresh at the vend and served with a smile across Bath.
      </p>
    </div>
    <p class="ft-scroll-hint">↓ Drive the truck · scroll the advert</p>
    """
)

# --- Interactive truck + scroll ads ---
components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <style>
      html, body {
        margin: 0;
        background: transparent;
        font-family: "Outfit", sans-serif;
        color: #1c1917;
        width: 100%;
      }

      .truck-zone {
        margin: 0.4rem 0 1.4rem;
        padding: 1rem 1rem 1.1rem;
        border-radius: 18px;
        background: linear-gradient(180deg, #fff1f2 0%, #fecdd3 55%, #fda4af 100%);
        border: 2px solid rgba(244, 63, 94, 0.35);
        box-shadow: 0 12px 28px rgba(225, 29, 72, 0.12);
        user-select: none;
      }
      .truck-hint {
        text-align: center;
        font-size: 0.92rem;
        font-weight: 600;
        color: #9f1239;
        margin: 0 0 0.7rem;
        letter-spacing: -0.02em;
      }
      .road {
        position: relative;
        height: 120px;
        border-radius: 14px;
        background: linear-gradient(180deg, #57534e 0%, #292524 100%);
        overflow: hidden;
        cursor: grab;
      }
      .road:active { cursor: grabbing; }
      .road-line {
        position: absolute;
        left: 0;
        right: 0;
        top: 50%;
        height: 4px;
        background: repeating-linear-gradient(
          90deg,
          #fde047 0 28px,
          transparent 28px 48px
        );
        transform: translateY(-50%);
        opacity: 0.85;
      }
      .truck {
        position: absolute;
        bottom: 14px;
        left: 8%;
        width: 150px;
        cursor: pointer;
        transform-origin: center bottom;
        transition: filter 0.2s ease;
        touch-action: none;
      }
      .truck:hover { filter: drop-shadow(0 8px 14px rgba(0,0,0,0.35)); }
      .truck.driving .wheel {
        animation: spinWheel 0.35s linear infinite;
      }
      .truck.driving .truck-flip {
        animation: bounceDrive 0.45s ease-in-out infinite;
      }
      .truck-flip {
        position: relative;
        width: 150px;
        height: 58px;
        transform-origin: center bottom;
      }
      .cab {
        position: absolute;
        left: 0;
        bottom: 18px;
        width: 48px;
        height: 36px;
        background: #e11d48;
        border-radius: 8px 10px 4px 4px;
        border: 2px solid #881337;
      }
      .cab-window {
        position: absolute;
        top: 6px;
        left: 8px;
        width: 22px;
        height: 14px;
        background: #e0f2fe;
        border-radius: 3px;
        border: 1px solid #881337;
      }
      .box {
        position: absolute;
        left: 44px;
        bottom: 18px;
        width: 92px;
        height: 42px;
        background: linear-gradient(135deg, #fb7185, #f43f5e);
        border-radius: 6px 10px 6px 4px;
        border: 2px solid #881337;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff1f2;
        font-family: "Space Grotesk", sans-serif;
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-align: center;
        line-height: 1.1;
        padding: 0 4px;
      }
      .wheel {
        position: absolute;
        bottom: 2px;
        width: 22px;
        height: 22px;
        background: #1c1917;
        border-radius: 50%;
        border: 3px solid #a8a29e;
        box-sizing: border-box;
      }
      .wheel::after {
        content: "";
        position: absolute;
        inset: 5px;
        border-radius: 50%;
        background: #78716c;
      }
      .wheel-f { left: 14px; }
      .wheel-b { right: 18px; }
      .honk {
        position: absolute;
        top: -8px;
        left: 10px;
        font-size: 0.85rem;
        opacity: 0;
        transform: translateY(4px);
        pointer-events: none;
      }
      .truck.beep .honk {
        animation: honkPop 0.7s ease forwards;
      }
      @keyframes spinWheel {
        to { transform: rotate(360deg); }
      }
      @keyframes bounceDrive {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
      }
      @keyframes honkPop {
        0% { opacity: 0; transform: translateY(6px) scale(0.8); }
        30% { opacity: 1; transform: translateY(-2px) scale(1.15); }
        100% { opacity: 0; transform: translateY(-14px) scale(1); }
      }
      .truck-btns {
        display: flex;
        gap: 0.55rem;
        justify-content: center;
        margin-top: 0.75rem;
      }
      .truck-btns button {
        font-family: "Outfit", sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        border-radius: 999px;
        border: 2px solid #be123c;
        background: rgba(255, 241, 242, 0.9);
        color: #9f1239;
        padding: 0.4rem 0.9rem;
        cursor: pointer;
      }
      .truck-btns button:hover {
        background: #fde047;
        transform: scale(1.05);
      }

      .track {
        display: flex;
        flex-direction: column;
        gap: 1.75rem;
        padding: 0.6rem 0.2rem 1.2rem;
        width: 100%;
        box-sizing: border-box;
      }
      .bit {
        width: 100%;
        opacity: 0;
        filter: blur(10px);
        will-change: transform, opacity, filter;
      }
      .bit-1 { transform: translateX(-110%) rotate(-8deg); }
      .bit-2 { transform: translateX(110%) rotate(8deg); }
      .bit-3 { transform: translateY(80px) scale(0.88) rotate(-4deg); }

      .bit-inner {
        width: 100%;
        box-sizing: border-box;
        border-radius: 18px;
        padding: 2.1rem 2rem 1.85rem;
        display: flex;
        flex-direction: column;
        gap: 0.45rem;
        justify-content: center;
        min-height: 120px;
        border: 2px solid rgba(255, 255, 255, 0.35);
        box-shadow: 0 18px 42px rgba(136, 19, 55, 0.22);
        transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.35s ease;
        cursor: default;
        position: relative;
        overflow: hidden;
      }
      .bit-inner::after {
        content: "AD";
        position: absolute;
        top: 0.85rem;
        right: 1rem;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.16em;
        color: rgba(255, 255, 255, 0.75);
      }
      .bit-1 .bit-inner {
        background: linear-gradient(115deg, #be123c 0%, #e11d48 55%, #fb7185 100%);
      }
      .bit-2 .bit-inner {
        background: linear-gradient(115deg, #9f1239 0%, #f43f5e 50%, #fde047 100%);
      }
      .bit-3 .bit-inner {
        background: linear-gradient(115deg, #881337 0%, #fb7185 45%, #fef08a 100%);
      }
      .bit-inner:hover {
        transform: scale(1.035);
        box-shadow: 0 24px 50px rgba(136, 19, 55, 0.3);
      }
      .bit-kicker {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: rgba(255, 241, 242, 0.85);
      }
      .bit-words {
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(2rem, 5vw, 3.1rem);
        font-weight: 700;
        letter-spacing: -0.05em;
        line-height: 1.05;
        color: #fff1f2;
        margin: 0;
        transition: transform 0.3s ease;
        transform-origin: left center;
      }
      .bit-inner:hover .bit-words {
        transform: scale(1.08);
      }
      .bit-sub {
        margin: 0;
        font-size: 1.05rem;
        font-weight: 500;
        color: rgba(255, 241, 242, 0.9);
        letter-spacing: -0.02em;
        max-width: 36rem;
      }

      .bit-1.in { animation: adSweepLeft 0.95s cubic-bezier(0.22, 1, 0.36, 1) forwards; }
      .bit-2.in { animation: adSweepRight 0.95s cubic-bezier(0.22, 1, 0.36, 1) forwards; }
      .bit-3.in { animation: adDropSpin 1.05s cubic-bezier(0.34, 1.3, 0.64, 1) forwards; }

      @keyframes adSweepLeft {
        0% { opacity: 0; filter: blur(12px); transform: translateX(-110%) rotate(-10deg); }
        70% { opacity: 1; filter: blur(0); transform: translateX(2%) rotate(2deg); }
        100% { opacity: 1; filter: blur(0); transform: translateX(0) rotate(0); }
      }
      @keyframes adSweepRight {
        0% { opacity: 0; filter: blur(12px); transform: translateX(110%) rotate(10deg); }
        70% { opacity: 1; filter: blur(0); transform: translateX(-2%) rotate(-2deg); }
        100% { opacity: 1; filter: blur(0); transform: translateX(0) rotate(0); }
      }
      @keyframes adDropSpin {
        0% { opacity: 0; filter: blur(14px); transform: translateY(90px) scale(0.9) rotate(-12deg); }
        60% { opacity: 1; filter: blur(0); transform: translateY(-10px) scale(1.03) rotate(3deg); }
        100% { opacity: 1; filter: blur(0); transform: translateY(0) scale(1) rotate(0); }
      }
    </style>

    <div class="truck-zone">
      <p class="truck-hint">Click the truck to drive · drag it along the road · honk for fun</p>
      <div class="road" id="road">
        <div class="road-line"></div>
        <div class="truck" id="truck" title="Click to drive">
          <div class="truck-flip" id="truckFlip">
            <div class="honk">🔊 beep!</div>
            <div class="cab"><div class="cab-window"></div></div>
            <div class="box">LOADED<br>BITES</div>
            <div class="wheel wheel-f"></div>
            <div class="wheel wheel-b"></div>
          </div>
        </div>
      </div>
      <div class="truck-btns">
        <button type="button" id="driveBtn">Drive / Stop</button>
        <button type="button" id="honkBtn">Honk</button>
        <button type="button" id="resetBtn">Reset</button>
      </div>
    </div>

    <div class="track">
      <div class="bit bit-1">
        <div class="bit-inner">
          <div class="bit-kicker">LoadedBites GLA</div>
          <p class="bit-words">Fresh Hot Bites</p>
          <p class="bit-sub">Cooked to order at the food vend.</p>
        </div>
      </div>
      <div class="bit bit-2">
        <div class="bit-inner">
          <div class="bit-kicker">Now serving Bath</div>
          <p class="bit-words">Properly Loaded Food</p>
          <p class="bit-sub">Big portions. Bold flavour. Worth the queue.</p>
        </div>
      </div>
      <div class="bit bit-3">
        <div class="bit-inner">
          <div class="bit-kicker">Catch the vend</div>
          <p class="bit-words">Bath Food Vend</p>
          <p class="bit-sub">Follow for today’s spot — then come get loaded.</p>
        </div>
      </div>
    </div>

    <script>
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

      const road = document.getElementById("road");
      const truck = document.getElementById("truck");
      const truckFlip = document.getElementById("truckFlip");
      const driveBtn = document.getElementById("driveBtn");
      const honkBtn = document.getElementById("honkBtn");
      const resetBtn = document.getElementById("resetBtn");

      let driving = false;
      let dir = 1;
      let x = road.clientWidth * 0.08;
      let raf = null;
      let dragging = false;
      let dragOffset = 0;
      let moved = false;

      function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }
      function face() {
        truckFlip.style.transform = dir < 0 ? "scaleX(-1)" : "scaleX(1)";
      }
      function place() {
        const maxX = road.clientWidth - truck.offsetWidth - 8;
        x = clamp(x, 8, maxX);
        truck.style.left = x + "px";
      }
      place();
      face();

      function tick() {
        if (!driving) return;
        const maxX = road.clientWidth - truck.offsetWidth - 8;
        x += dir * 2.4;
        if (x >= maxX) { x = maxX; dir = -1; face(); }
        if (x <= 8) { x = 8; dir = 1; face(); }
        truck.style.left = x + "px";
        raf = requestAnimationFrame(tick);
      }

      function setDriving(on) {
        driving = on;
        truck.classList.toggle("driving", on);
        if (on) {
          cancelAnimationFrame(raf);
          raf = requestAnimationFrame(tick);
        } else {
          cancelAnimationFrame(raf);
          face();
        }
      }

      function honk() {
        truck.classList.remove("beep");
        void truck.offsetWidth;
        truck.classList.add("beep");
      }

      truck.addEventListener("click", () => {
        if (moved) { moved = false; return; }
        setDriving(!driving);
      });
      driveBtn.addEventListener("click", () => setDriving(!driving));
      honkBtn.addEventListener("click", honk);
      resetBtn.addEventListener("click", () => {
        setDriving(false);
        dir = 1;
        x = road.clientWidth * 0.08;
        face();
        place();
      });

      truck.addEventListener("pointerdown", (e) => {
        dragging = true;
        moved = false;
        setDriving(false);
        dragOffset = e.clientX - truck.getBoundingClientRect().left;
        truck.setPointerCapture(e.pointerId);
      });
      truck.addEventListener("pointermove", (e) => {
        if (!dragging) return;
        moved = true;
        const roadRect = road.getBoundingClientRect();
        x = e.clientX - roadRect.left - dragOffset;
        place();
      });
      truck.addEventListener("pointerup", () => { dragging = false; });
      truck.addEventListener("pointercancel", () => { dragging = false; });
      window.addEventListener("resize", place);
    </script>
    """,
    height=980,
    scrolling=False,
)

# --- Full writing ---
show_html('<p class="ft-section">Hungry in Bath?</p>')
show_html(
    """
    <p class="ft-lead">
      LoadedBites GLA is a Bath food vend built for people who want more than a rushed sandwich.
      We load every order with bold seasoning, generous toppings, and the kind of comfort food
      that turns a quick stop into the best part of your day.
    </p>
    <p class="ft-body">
      Whether you catch us at lunch, after work, or on a weekend wander, the mission stays the same:
      honest food, cooked to order, packed with flavour, and ready when you are.
      No fancy dining room — just a food vend, a grill, and bites that hit every time.
    </p>
    """
)

show_html('<p class="ft-section">Why LoadedBites GLA</p>')
left, right = st.columns(2, gap="large")
with left:
    show_html(
        """
        <div class="ft-card">
          <h3>Loaded for real</h3>
          <p>
            We don’t do sad, half-filled trays. Every bite is stacked with flavour —
            sauces, toppings, and extras chosen to make the meal feel special.
          </p>
        </div>
        <div class="ft-card">
          <h3>Cooked fresh</h3>
          <p>
            Your order starts when you ask for it. Hot from the vend, not sitting under a lamp
            waiting for someone else to change their mind.
          </p>
        </div>
        """
    )
with right:
    show_html(
        """
        <div class="ft-card">
          <h3>Bath energy</h3>
          <p>
            Made for this city — quick enough for a lunch break, good enough for a night out,
            friendly enough that you’ll want to come back with mates.
          </p>
        </div>
        <div class="ft-card">
          <h3>Fair prices</h3>
          <p>
            Street food should feel worth it. Big portions, strong taste, and prices that make
            sense when you’re feeding yourself or the whole crew.
          </p>
        </div>
        """
    )

show_html('<p class="ft-section">What we cook</p>')
show_html(
    """
    <p class="ft-lead">
      LoadedBites GLA is all about big, bold comfort food — the kind you can smell before you
      see the queue. Think crispy bases, rich fillings, melted cheese, house sauces, and toppings
      piled high until the tray actually feels loaded.
    </p>
    <p class="ft-body">
      We lean into warm wraps with seasoned protein and fresh crunch, cheesy stacks that get
      messy in the best way, and spicy options when you want a kick. Everything is cooked to
      order at the food vend, so it lands hot, fresh, and ready to eat on the go.
    </p>
    <p class="ft-body">
      Some days we’re smoky. Some days we’re sweet. Specials rotate with the spot and the mood,
      but the idea never changes: generous portions, strong flavour, and food that turns a quick
      stop into something you talk about later. Ask at the window — if we can make it loaded, we will.
    </p>
    """
)

show_html('<p class="ft-section">Find the food vend</p>')
show_html(
    """
    <p class="ft-lead">
      LoadedBites GLA sets up around Bath — city centre lunch runs, local spots, events,
      and weekend stops. We post where the food vend is so you can plan the detour.
    </p>
    <p class="ft-body">
      Typical hours lean lunch through early evening, with later finishes when the crowd is out.
      Weather happens. Traffic happens. Flavour still shows up.
    </p>
    <p class="ft-body">
      <strong>Tip:</strong> check our Instagram story before you travel — that’s the fastest way
      to see today’s pin, opening time, and sold-out warnings.
    </p>
    """
)

show_html('<p class="ft-section">Made for your kind of hunger</p>')
c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    show_html(
        """
        <div class="ft-card">
          <h3>Office lunch</h3>
          <p>Fast enough for your break. Good enough that you won’t miss the cafeteria.</p>
        </div>
        """
    )
with c2:
    show_html(
        """
        <div class="ft-card">
          <h3>Night out fuel</h3>
          <p>After the gig, before the next plan — grab something hot and properly filling.</p>
        </div>
        """
    )
with c3:
    show_html(
        """
        <div class="ft-card">
          <h3>Family &amp; friends</h3>
          <p>Easy to order for a group. Mix the menu, share sauces, argue about favourites.</p>
        </div>
        """
    )

# --- CTA ---
show_html('<p class="ft-section">Come get loaded</p>')
show_html(
    """
    <p class="ft-lead">
      Looking for the food vend, booking us for a private stop, or just want today’s specials?
      Reach out — we love feeding Bath.
    </p>
    <p class="ft-body">
      Message us on Instagram or WhatsApp for location updates, catering enquiries,
      and custom orders for events. If you’ve got a birthday, office lunch, or market day,
      LoadedBites GLA can set up and feed the crowd.
    </p>
    """
)

col_a, col_b = st.columns(2, gap="large")
with col_a:
    st.link_button(
        "Follow @loadedbitesgla",
        "https://instagram.com/loadedbitesgla",
        use_container_width=True,
    )
with col_b:
    st.link_button(
        "WhatsApp the food vend",
        "https://wa.me/",
        use_container_width=True,
    )

show_html(
    """
    <div class="ft-footer">
      LoadedBites GLA · Bath food vend<br>
      Fresh · Loaded · Worth the queue
    </div>
    """
)
