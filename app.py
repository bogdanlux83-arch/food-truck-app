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
        background: #9f1239;
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
        margin-bottom: 0.35rem;
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
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        margin: 0.15rem 0 0.1rem;
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
      <div class="ft-tag">Bath food vendor</div>
      <p class="ft-brand">LoadedBites GLA</p>
      <p class="ft-sub">
        Refined street dining in Bath — generous portions, carefully prepared dishes,
        and fresh service from our food vendor throughout the city.
      </p>
    </div>
    <p class="ft-scroll-hint">↓ Explore the showcase below</p>
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
        color: #1c1917;
        width: 100%;
      }
      .track {
        display: flex;
        flex-direction: column;
        gap: 1.1rem;
        padding: 0.15rem 0.2rem 0.8rem;
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
        padding: 1.7rem 1.8rem 1.5rem;
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
        justify-content: center;
        min-height: 110px;
        border: 2px solid rgba(255, 255, 255, 0.35);
        box-shadow: 0 18px 42px rgba(136, 19, 55, 0.22);
        transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.35s ease;
        cursor: default;
        position: relative;
        overflow: hidden;
      }
      .bit-inner::after {
        content: "FEATURED";
        position: absolute;
        top: 0.85rem;
        right: 1rem;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.14em;
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

    <div class="track">
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
    </script>
    """,
    height=620,
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
      LoadedBites GLA · Bath food vendor<br>
      Freshly prepared · Generously served · Professionally run
    </div>
    """
)
