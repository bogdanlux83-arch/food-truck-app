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
        padding-top: 1.5rem;
        padding-bottom: 2.2rem;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1100px;
      }

      @keyframes ftHeroIn {
        from { opacity: 0; transform: translateY(24px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
      }

      .ft-hero {
        background: linear-gradient(125deg, #be123c 0%, #e11d48 32%, #fb7185 62%, #fde047 100%);
        border-radius: 24px;
        padding: 2.4rem 2rem 2.1rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 18px 40px rgba(225, 29, 72, 0.28);
        animation: ftHeroIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
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
      }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.5rem, 5.5vw, 3.6rem);
        font-weight: 700;
        margin: 0 0 0.45rem 0;
        line-height: 0.95;
        letter-spacing: -0.055em;
        color: #fff1f2;
      }
      .ft-sub {
        margin: 0;
        font-size: 1.15rem;
        max-width: 40rem;
        line-height: 1.4;
        color: #ffe4e6;
        font-weight: 500;
        letter-spacing: -0.02em;
      }
      .ft-scroll-hint {
        text-align: center;
        color: #9f1239;
        font-size: 0.95rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        margin: 0.4rem 0 0.2rem;
        opacity: 0.85;
      }
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(1.7rem, 3vw, 2.1rem);
        font-weight: 700;
        margin: 1.55rem 0 0.65rem;
        color: #be123c;
        letter-spacing: -0.05em;
        line-height: 1.05;
      }
      .ft-body {
        font-size: 1rem;
        line-height: 1.4;
        color: #57534e;
        letter-spacing: -0.02em;
        max-width: 44rem;
        margin: 0 0 0.55rem 0;
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
      }
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
      }
      div[data-testid="stButton"] button:hover,
      .stLinkButton a:hover {
        background: rgba(254, 240, 138, 0.85) !important;
        border-color: #e11d48 !important;
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
        Big flavour. Proper portions. Scroll down for a taste of what we do.
      </p>
    </div>
    <p class="ft-scroll-hint">↓ Scroll for three bites about the vend</p>
    """
)

# --- Scroll-triggered story bits ---
components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <style>
      html, body {
        margin: 0;
        background: transparent;
        font-family: "Outfit", sans-serif;
        color: #1c1917;
      }
      .track {
        display: flex;
        flex-direction: column;
        gap: 7.5rem;
        padding: 2.5rem 0.4rem 3rem;
      }
      .bit {
        max-width: 34rem;
        padding: 1.35rem 1.4rem 1.25rem;
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.82);
        border: 2px solid rgba(251, 113, 133, 0.55);
        box-shadow: 0 14px 34px rgba(225, 29, 72, 0.14);
        opacity: 0;
        will-change: transform, opacity;
      }
      .bit h3 {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.35rem;
        margin: 0 0 0.45rem;
        letter-spacing: -0.04em;
        color: #9f1239;
      }
      .bit p {
        margin: 0;
        font-size: 1.02rem;
        line-height: 1.45;
        letter-spacing: -0.02em;
        color: #57534e;
      }
      .bit-1 { align-self: flex-start; transform: translateX(-70px) rotate(-2deg); }
      .bit-2 { align-self: flex-end; transform: translateX(70px) rotate(2deg); }
      .bit-3 {
        align-self: center;
        transform: translateY(50px) scale(0.86);
      }

      .bit-1.in {
        animation: slideInLeft 0.75s cubic-bezier(0.22, 1, 0.36, 1) forwards;
      }
      .bit-2.in {
        animation: slideInRight 0.75s cubic-bezier(0.22, 1, 0.36, 1) forwards;
      }
      .bit-3.in {
        animation: popIn 0.8s cubic-bezier(0.34, 1.45, 0.64, 1) forwards;
      }

      @keyframes slideInLeft {
        0% { opacity: 0; transform: translateX(-70px) rotate(-2deg); }
        70% { opacity: 1; transform: translateX(8px) rotate(0.5deg); }
        100% { opacity: 1; transform: translateX(0) rotate(0deg); }
      }
      @keyframes slideInRight {
        0% { opacity: 0; transform: translateX(70px) rotate(2deg); }
        70% { opacity: 1; transform: translateX(-8px) rotate(-0.5deg); }
        100% { opacity: 1; transform: translateX(0) rotate(0deg); }
      }
      @keyframes popIn {
        0% { opacity: 0; transform: translateY(50px) scale(0.86); }
        60% { opacity: 1; transform: translateY(-8px) scale(1.04); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
      }
    </style>

    <div class="track">
      <div class="bit bit-1">
        <h3>Hot off the vend</h3>
        <p>
          LoadedBites GLA cooks to order — crispy, cheesy, saucy bites that land hot
          in your hands. No sad waiting-lamp food. Just fresh street energy in Bath.
        </p>
      </div>

      <div class="bit bit-2">
        <h3>Properly loaded</h3>
        <p>
          We stack flavour on flavour: bold seasoning, house sauces, and toppings piled high.
          Big portions, messy in the best way, made for lunch breaks and late-night cravings.
        </p>
      </div>

      <div class="bit bit-3">
        <h3>Find us &amp; get stuck in</h3>
        <p>
          Catch the food vend around Bath — city spots, events, weekend stops.
          Follow the stories for today’s pin, then come get loaded.
        </p>
      </div>
    </div>

    <script>
      const bits = document.querySelectorAll(".bit");
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("in");
            }
          });
        },
        { threshold: 0.4 }
      );
      bits.forEach((bit) => io.observe(bit));
    </script>
    """,
    height=980,
    scrolling=False,
)

# --- CTA ---
show_html('<p class="ft-section">Come get loaded</p>')
show_html(
    """
    <p class="ft-body">
      Message us for today’s spot, catering, or event bookings. We love feeding Bath.
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
