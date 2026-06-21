import streamlit as st
import pandas as pd

from sheets import get_logs_sheet
from streaks import (
    current_streak,
    longest_streak
)


def show_achievements(username):

    st.title("🏅 Achievements")

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        st.info("No achievements yet.")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    df = df[
        df["Username"].str.lower()
        == username.lower()
    ]

    if len(df) == 0:
        st.info("No achievements yet.")
        return

    df["Score"] = pd.to_numeric(
        df["Score"],
        errors="coerce"
    ).fillna(0)

    df["Study"] = pd.to_numeric(
        df["Study"],
        errors="coerce"
    ).fillna(0)

    df["Water Intake"] = pd.to_numeric(
        df["Water Intake"],
        errors="coerce"
    ).fillna(0)

    badges = []

    # First Log
    if len(df) >= 1:
        badges.append("🏅 First Log")

    # 3 Day Streak
    if current_streak(username) >= 3:
        badges.append("🔥 3 Day Streak")

    # 7 Day Streak
    if current_streak(username) >= 7:
        badges.append("🔥 7 Day Streak")

    # Longest Streak
    if longest_streak(username) >= 10:
        badges.append("🏆 Consistency Master")

    # Perfect Score
    if (df["Score"] >= 100).any():
        badges.append("⭐ Perfect Day")

    # Study Warrior
    if len(df[df["Study"] >= 5]) >= 5:
        badges.append("📚 Study Warrior")

    # Hydration Hero
    if len(df[df["Water Intake"] >= 3]) >= 5:
        badges.append("💧 Hydration Hero")

    if len(badges) == 0:
        st.warning("No badges unlocked yet.")
        return

    st.success(
        f"{len(badges)} badges unlocked!"
    )

    for badge in badges:

        st.markdown(
            f"### {badge}"
        )