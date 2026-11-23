from textwrap import dedent

import streamlit as st


def show_html(content: str) -> None:
    st.html(dedent(content).strip())


st.set_page_config(
    page_title="LoadedBitesGLA",
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
        font-size: 22px;
        line-height: 1.65;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
        color: #1c1917;
      }

      .stApp {
        background:
          radial-gradient(1000px 520px at 8% -8%, #fef08a 0%, transparent 55%),
          radial-gradient(820px 460px at 92% 5%, #fdba74 0%, transparent 48%),
          radial-gradient(700px 400px at 50% 110%, #fde68a 0%, transparent 50%),
          #fffbeb;
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
        background: linear-gradient(125deg, #ea580c 0%, #f59e0b 40%, #fbbf24 75%, #fde68a 100%);
        border-radius: 28px;
        padding: 3.4rem 2.6rem 3rem;
        margin-bottom: 2rem;
        color: #1c1917;
        box-shadow: 0 18px 40px rgba(245, 158, 11, 0.28);
      }
      .ft-brand {
        font-family: var(--ft-display) !important;
        font-size: clamp(3.2rem, 7vw, 5rem);
        font-weight: 800;
        margin: 0 0 0.75rem 0;
        line-height: 0.96;
        letter-spacing: -0.04em;
        color: #431407;
      }
      .ft-sub {
        font-family: var(--ft-sans) !important;
        margin: 0;
        font-size: 1.5rem;
        max-width: 42rem;
        line-height: 1.65;
        color: #7c2d12;
        font-weight: 500;
        letter-spacing: -0.015em;
      }
      .ft-section {
        font-family: var(--ft-display) !important;
        font-size: clamp(2.2rem, 4vw, 2.85rem);
        font-weight: 700;
        margin: 2.2rem 0 1.1rem;
        color: #c2410c;
        letter-spacing: -0.035em;
        line-height: 1.1;
      }
      .ft-body {
        font-family: var(--ft-sans) !important;
        font-size: 1.28rem;
        line-height: 1.65;
        color: #57534e;
        font-weight: 400;
        letter-spacing: -0.01em;
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
        background: rgba(254, 243, 199, 0.65) !important;
        color: #9a3412 !important;
        border: 2px solid rgba(245, 158, 11, 0.8) !important;
      }
      div[data-testid="stButton"] button:hover {
        background: rgba(253, 230, 138, 0.85) !important;
        border-color: #ea580c !important;
      }
    </style>
    """
)

show_html(
    """
    <div class="ft-hero">
      <p class="ft-brand">LoadedBitesGLA</p>
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
show_html('<p class="ft-body">Phone / WhatsApp / Instagram can go here.</p>')
