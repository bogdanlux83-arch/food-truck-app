from textwrap import dedent

import streamlit as st


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
      .stTextInput input, .stTextArea textarea,
      div[data-testid="stButton"] button, .stLinkButton a {
        font-family: var(--ft-sans) !important;
      }

      html, body, .stApp {
        font-size: 22px;
        line-height: 1.65;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
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
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 2.2rem !important;
        padding-right: 2.2rem !important;
        max-width: 1240px;
      }

      .ft-hero {
        background: linear-gradient(125deg, #be123c 0%, #e11d48 32%, #fb7185 62%, #fde047 100%);
        border-radius: 28px;
        padding: 3.4rem 2.6rem 3rem;
        margin-bottom: 2rem;
        color: #1c1917;
        box-shadow: 0 18px 40px rgba(225, 29, 72, 0.28);
      }
      .ft-tag {
        display: inline-block;
        font-family: var(--ft-sans) !important;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        background: #881337;
        color: #fef08a;
        padding: 0.5rem 0.95rem;
        border-radius: 999px;
        margin-bottom: 1rem;
      }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(3.2rem, 7vw, 5rem);
        font-weight: 700;
        margin: 0 0 0.75rem 0;
        line-height: 0.96;
        letter-spacing: -0.05em;
        color: #fff1f2;
      }
      .ft-sub {
        font-family: var(--ft-sans) !important;
        margin: 0;
        font-size: 1.5rem;
        max-width: 42rem;
        line-height: 1.65;
        color: #ffe4e6;
        font-weight: 500;
        letter-spacing: -0.015em;
      }
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.2rem, 4vw, 2.85rem);
        font-weight: 700;
        margin: 2.4rem 0 1.1rem;
        color: #be123c;
        letter-spacing: -0.045em;
        line-height: 1.1;
      }
      .ft-lead {
        font-family: var(--ft-sans) !important;
        font-size: 1.28rem;
        line-height: 1.7;
        color: #44403c;
        font-weight: 400;
        letter-spacing: -0.01em;
        max-width: 46rem;
        margin: 0 0 1.1rem 0;
      }
      .ft-body {
        font-family: var(--ft-sans) !important;
        font-size: 1.2rem;
        line-height: 1.7;
        color: #57534e;
        font-weight: 400;
        letter-spacing: -0.01em;
        max-width: 46rem;
        margin: 0 0 0.9rem 0;
      }
      .ft-card {
        background: rgba(255, 255, 255, 0.78);
        border: 2px solid rgba(251, 113, 133, 0.55);
        border-radius: 20px;
        padding: 1.45rem 1.4rem 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 10px 28px rgba(225, 29, 72, 0.12);
      }
      .ft-card h3 {
        font-family: var(--ft-display) !important;
        font-size: 1.55rem;
        font-weight: 700;
        margin: 0 0 0.45rem 0;
        color: #9f1239;
        letter-spacing: -0.03em;
      }
      .ft-card p {
        font-family: var(--ft-sans) !important;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #57534e;
        margin: 0;
      }
      .ft-price {
        font-family: var(--ft-display) !important;
        color: #e11d48;
        font-weight: 800;
        font-size: 1.25rem;
      }
      .ft-footer {
        text-align: center;
        color: #9f1239;
        font-family: var(--ft-sans) !important;
        font-size: 1.05rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 2px solid rgba(251, 113, 133, 0.45);
        font-weight: 500;
        line-height: 1.6;
      }

      [data-testid="stAlert"] p,
      [data-testid="stMarkdownContainer"] p {
        font-family: var(--ft-sans) !important;
        font-size: 1.22rem !important;
        letter-spacing: -0.01em;
      }
      div[data-testid="stButton"] button {
        border-radius: 16px !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 0.85rem 1.45rem !important;
        letter-spacing: -0.015em !important;
        background: rgba(255, 228, 230, 0.7) !important;
        color: #9f1239 !important;
        border: 2px solid rgba(244, 63, 94, 0.75) !important;
      }
      div[data-testid="stButton"] button:hover {
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
        Big flavour. Proper portions. Street food worth queuing for —
        cooked fresh at the vend and served with a smile across Bath.
      </p>
    </div>
    """
)

# --- Intro ---
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

# --- Why us ---
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

# --- Food description ---
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

# --- Where ---
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

# --- Who it's for ---
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

# --- CTA / contact ---
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
