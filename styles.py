import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* SPACE BACKGROUND */

    .stApp {

        background:
        linear-gradient(
            rgba(5,10,20,0.80),
            rgba(5,10,20,0.80)
        ),
        url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;

        color: white;
    }

    /* MAIN CONTENT */

    .block-container {

        padding-top: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {

        background:
        rgba(
            10,
            15,
            30,
            0.92
        );

        backdrop-filter: blur(12px);

        border-right:
        1px solid rgba(
            255,
            255,
            255,
            0.08
        );
    }

    /* METRIC CARDS */

    div[data-testid="metric-container"] {

        background:
        rgba(
            255,
            255,
            255,
            0.08
        );

        backdrop-filter: blur(12px);

        border:
        1px solid rgba(
            255,
            255,
            255,
            0.10
        );

        border-radius: 18px;

        padding: 18px;

        box-shadow:
        0px 4px 20px rgba(
            0,
            0,
            0,
            0.25
        );
    }

    /* BUTTONS */

    .stButton > button {

        width: 100%;
        height: 48px;

        border-radius: 14px;

        border: none;

        color: white;

        font-weight: bold;

        background:
        linear-gradient(
            135deg,
            #3B82F6,
            #8B5CF6
        );
    }

    .stButton > button:hover {

        transform: scale(1.02);

        transition: 0.2s;
    }

    /* TEXT */

    h1, h2 {

        color: #FFFFFF !important;
    }

    h3, p, label {

        color: #CBD5E1 !important;
    }

    /* DATAFRAMES */

    .stDataFrame {

        border-radius: 16px;

        overflow: hidden;
    }

    /* PROGRESS BAR */

    .stProgress > div > div > div {

        background:
        linear-gradient(
            90deg,
            #3B82F6,
            #8B5CF6
        );
    }

    </style>
    """, unsafe_allow_html=True)