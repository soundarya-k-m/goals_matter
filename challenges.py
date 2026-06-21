import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

from sheets import get_logs_sheet


def show_challenges():

    st.title("🏆 Weekly Challenges")

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        st.warning("No data found.")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    df["Study"] = pd.to_numeric(
        df["Study"],
        errors="coerce"
    ).fillna(0)

    df["Water Intake"] = pd.to_numeric(
        df["Water Intake"],
        errors="coerce"
    ).fillna(0)

    today = datetime.today()

    week_start = today - timedelta(days=7)

    weekly_df = df[
        df["Date"] >= week_start
    ]

    users = sorted(
        weekly_df["Username"].unique()
    )

    st.subheader(
        "🏋️ Workout Challenge"
    )

    for user in users:

        workouts = len(
            weekly_df[
                (weekly_df["Username"] == user)
                &
                (weekly_df["Workout"] == "Yes")
            ]
        )

        st.write(
            f"**{user}**"
        )

        st.progress(
            min(workouts / 5, 1.0)
        )

        st.caption(
            f"{workouts}/5 workout days"
        )

    st.divider()

    st.subheader(
        "📚 Study Challenge"
    )

    for user in users:

        study_hours = (
            weekly_df[
                weekly_df["Username"] == user
            ]["Study"]
            .sum()
        )

        st.write(
            f"**{user}**"
        )

        st.progress(
            min(study_hours / 20, 1.0)
        )

        st.caption(
            f"{round(study_hours,1)}/20 study hours"
        )

    st.divider()

    st.subheader(
        "💧 Hydration Challenge"
    )

    for user in users:

        water = (
            weekly_df[
                weekly_df["Username"] == user
            ]["Water Intake"]
            .sum()
        )

        st.write(
            f"**{user}**"
        )

        st.progress(
            min(water / 21, 1.0)
        )

        st.caption(
            f"{round(water,1)}/21 Litres"
        )