from textwrap import dedent

import streamlit as st


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


st.set_page_config(
    page_title="Uncle's Food Truck",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

show_html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;700;800&family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
      :root {
        --ft-display: "Fraunces", Georgia, serif;
        --ft-sans: "Sora", sans-serif;
      }

      html, body, .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"],
      [data-testid="stCaption"], [data-testid="stAlert"],
      .stTextInput input, .stTextArea textarea,
      div[data-testid="stButton"] button, .stLinkButton a {
        font-family: var(--ft-sans) !important;
      }

      html, body, .stApp {
        font-size: 20px;
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
        color: #1c1917;
      }

      .stApp {
        background:
          radial-gradient(900px 480px at 10% -10%, #fde68a 0%, transparent 55%),
          radial-gradient(700px 420px at 95% 0%, #fb923c 0%, transparent 45%),
          #fff7ed;
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        padding-top: 1.6rem;
        padding-bottom: 2.5rem;
        max-width: 1100px;
      }

      .ft-hero {
        background: linear-gradient(125deg, #9a3412 0%, #c2410c 45%, #ea580c 100%);
        border-radius: 24px;
        padding: 2.8rem 2.2rem 2.4rem;
        margin-bottom: 1.6rem;
        color: #fff7ed;
        box-shadow: 0 18px 40px rgba(194, 65, 12, 0.25);
      }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.8rem, 6vw, 4.2rem);
        font-weight: 800;
        margin: 0 0 0.6rem 0;
        line-height: 0.98;
        letter-spacing: -0.04em;
        color: #fff7ed;
      }
      .ft-sub {
        font-family: var(--ft-sans) !important;
        margin: 0;
        font-size: 1.35rem;
        max-width: 38rem;
        line-height: 1.65;
        color: #ffedd5;
        font-weight: 400;
        letter-spacing: -0.015em;
      }
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(1.9rem, 3.5vw, 2.4rem);
        font-weight: 700;
        margin: 1.8rem 0 0.9rem;
        color: #9a3412;
        letter-spacing: -0.035em;
        line-height: 1.1;
      }
      .ft-body {
        font-family: var(--ft-sans) !important;
        font-size: 1.15rem;
        line-height: 1.6;
        color: #44403c;
        font-weight: 400;
        letter-spacing: -0.01em;
      }

      [data-testid="stAlert"] p,
      [data-testid="stMarkdownContainer"] p {
        font-family: var(--ft-sans) !important;
        font-size: 1.12rem !important;
        letter-spacing: -0.01em;
      }
      div[data-testid="stButton"] button {
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 0.7rem 1.25rem !important;
        letter-spacing: -0.015em !important;
        background: rgba(255, 247, 237, 0.55) !important;
        color: #7c2d12 !important;
        border: 2px solid rgba(194, 65, 12, 0.75) !important;
      }
    </style>
    """
)

show_html(
    """
    <div class="ft-hero">
      <p class="ft-brand">Uncle's Food Truck</p>
      <p class="ft-sub">
        Fresh street food, made to order. Menu, stop times, and contact — coming together here.
      </p>
    </div>
    """
)

show_html('<p class="ft-section">Today\'s menu</p>')
st.info("Add dishes here next — name, price, and a short description.")

show_html('<p class="ft-section">Find the truck</p>')
show_html('<p class="ft-body">Location and hours can go here.</p>')

show_html('<p class="ft-section">Contact</p>')
show_html('<p class="ft-body">Phone / WhatsApp / Instagram for your uncle can go here.</p>')
