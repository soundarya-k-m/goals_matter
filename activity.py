import streamlit as st
import pandas as pd

from sheets import get_logs_sheet


def show_activity_feed():

    st.title("🔥 Friend Activity")

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        st.info("No activity yet.")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    recent = df.tail(30)

    for _, row in recent.iloc[::-1].iterrows():

        username = row["Username"]
        score = row["Score"]

        workout = row["Workout"]
        study = float(row["Study"])
        water = float(row["Water Intake"])
        sleep = float(row["Sleep"])

        st.markdown("---")

        st.write(
            f"👤 **{username}** • {row['Date']}"
        )

        if workout == "Yes":
            st.success(
                f"🏋️ Completed workout"
            )

        st.info(
            f"📚 Studied {study} hours"
        )

        st.info(
            f"💧 Drank {water} L water"
        )

        st.info(
            f"😴 Slept {sleep} hours"
        )

        st.warning(
            f"⭐ Score: {score}"
        )