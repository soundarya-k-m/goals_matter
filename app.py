import streamlit as st

from auth import (
    initialize_session,
    login_page,
    logout
)

from dashboard import show_dashboard
from reports import show_reports
from leaderboard import show_leaderboard
from activity import show_activity_feed
from user_profile import show_profile
from achievements import show_achievements
from challenges import show_challenges
from levels import show_levels
from styles import load_css

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="🎯 Goals Matter",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# LOAD SPACE THEME
# ==================================================

load_css()

# ==================================================
# SESSION INITIALIZATION
# ==================================================

initialize_session()

# ==================================================
# LOGIN PAGE
# ==================================================

if not st.session_state.logged_in:

    login_page()

# ==================================================
# MAIN APP
# ==================================================

else:

    with st.sidebar:

        st.title("🎯 Goals Matter")

        st.write(
            f"👤 Logged in as: **{st.session_state.username}**"
        )

        st.divider()

        page = st.radio(
            "📌 Navigation",
            [
                "Dashboard",
                "Reports",
                "Leaderboard",
                "Activity",
                "Profile",
                "Achievements",
                "Challenges",
                "Levels"
            ]
        )

        st.divider()

        if st.button("🚪 Logout"):
            logout()

    # ==================================================
    # PAGE ROUTING
    # ==================================================

    if page == "Dashboard":

        show_dashboard(
            st.session_state.username
        )

    elif page == "Reports":

        show_reports()

    elif page == "Leaderboard":

        show_leaderboard()

    elif page == "Activity":

        show_activity_feed()

    elif page == "Profile":

        show_profile(
            st.session_state.username
        )

    elif page == "Achievements":

        show_achievements(
            st.session_state.username
        )

    elif page == "Challenges":

        show_challenges()

    elif page == "Levels":

        show_levels()