import streamlit as st
import pandas as pd
import plotly.express as px
from xp_system import (
    calculate_xp,
    get_level
)
from ai_coach import show_ai_coach
from sheets import get_logs_sheet
from streaks import (
    current_streak,
    longest_streak,
    last_active
)

from pdf_report import generate_report


def show_profile(username):

    st.divider()

    show_ai_coach(username)
    st.title("👤 My Profile")
    xp = calculate_xp(username)

    level_name, level_num = get_level(xp)

    st.success(
        f"{level_name} | Level {level_num}"
    )

    st.progress(
        min(xp / 5000, 1.0)
    )

    st.write(
        f"XP: {xp}"
    )

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:

        st.warning("No data available.")

        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    df = df[
        df["Username"].astype(str).str.lower()
        == str(username).lower()
    ]

    if len(df) == 0:

        st.warning("No logs found.")

        return

    df["Score"] = pd.to_numeric(
        df["Score"],
        errors="coerce"
    ).fillna(0)

    total_logs = len(df)

    average_score = round(
        df["Score"].mean(),
        1
    )

    best_score = int(
        df["Score"].max()
    )

    current = current_streak(
        username
    )

    longest = longest_streak(
        username
    )

    active = last_active(
        username
    )

    # ==========================================
    # TOP METRICS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🔥 Current Streak",
            current
        )

    with col2:

        st.metric(
            "🏆 Longest Streak",
            longest
        )

    with col3:

        st.metric(
            "⭐ Average Score",
            average_score
        )

    st.divider()

    col4, col5 = st.columns(2)

    with col4:

        st.metric(
            "📝 Total Logs",
            total_logs
        )

    with col5:

        st.metric(
            "🥇 Best Score",
            best_score
        )

    st.info(
        f"📅 Last Active: {active}"
    )

    st.divider()

    # ==========================================
    # SCORE GRAPH
    # ==========================================

    st.subheader(
        "📈 Score Progress"
    )

    chart_df = df.copy()

    chart_df["Date"] = pd.to_datetime(
        chart_df["Date"]
    )

    chart_df = chart_df.sort_values(
        by="Date"
    )

    fig = px.line(
        chart_df,
        x="Date",
        y="Score",
        markers=True,
        title="Score Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # PDF REPORT
    # ==========================================

    st.subheader(
        "📄 Weekly Report"
    )

    if st.button(
        "Generate Weekly Report"
    ):

        pdf_file = generate_report(
            username
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download PDF",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )

    st.divider()

    # ==========================================
    # LOG HISTORY
    # ==========================================

    st.subheader(
        "📋 My Log History"
    )

    display_df = chart_df.sort_values(
        by="Date",
        ascending=False
    )

    st.dataframe(
        display_df,
        use_container_width=True
    )