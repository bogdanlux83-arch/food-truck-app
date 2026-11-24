from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


def _truck_scene_html() -> str:
    """Load the interactive Three.js food-truck street scene."""
    from pathlib import Path

    return (Path(__file__).resolve().parent / "truck_scene.html").read_text(encoding="utf-8")


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

# --- Interactive food truck (real 3D model) ---
show_html('<p class="ft-section" id="truck">Our food truck</p>')
show_html(
    """
    <p class="ft-lead">
      Scroll to watch the van pull in. Drag to look around, then open the hatch,
      order from the menu, switch the headlights, sound the horn, or send it for a lap.
    </p>
    """
)

components.html(
    _truck_scene_html(),
    height=720,
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
