import streamlit as st
import pandas as pd
import plotly.express as px
from sheets import get_logs_sheet


def show_reports():

    st.header("📊 Group Reports")

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        st.warning("No logs found")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    df["Score"] = pd.to_numeric(
        df["Score"],
        errors="coerce"
    ).fillna(0)

    st.subheader("🏆 Total Scores")

    leaderboard = (
        df.groupby("Username")["Score"]
        .sum()
        .reset_index()
        .sort_values(
            by="Score",
            ascending=False
        )
    )

    st.dataframe(
        leaderboard,
        use_container_width=True
    )

    st.divider()

    st.subheader("📈 Score Comparison")

    fig = px.bar(
        leaderboard,
        x="Username",
        y="Score",
        text="Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("🔥 Daily Progress")

    daily = (
        df.groupby(["Date", "Username"])["Score"]
        .sum()
        .reset_index()
    )

    fig2 = px.line(
        daily,
        x="Date",
        y="Score",
        color="Username",
        markers=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    st.subheader("📋 All Logs")

    st.dataframe(
        df.sort_values(
            by="Date",
            ascending=False
        ),
        use_container_width=True
    )