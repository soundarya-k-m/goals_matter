import streamlit as st
import pandas as pd
from datetime import date

from sheets import get_logs_sheet
from streaks import current_streak


def show_reminder(username):

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    today = str(date.today())

    user_df = df[
        df["Username"].astype(str).str.lower()
        == str(username).lower()
    ]

    if len(user_df) == 0:

        st.warning(
            "⚠️ No logs submitted yet."
        )

        return

    today_log = user_df[
        user_df["Date"] == today
    ]

    if len(today_log) == 0:

        streak = current_streak(
            username
        )

        st.error(
            f"""
⚠️ You have not submitted today's goals.

🔥 Current Streak: {streak}

Submit today's goals to protect your streak.
"""
        )

    else:

        st.success(
            "✅ Today's goals already submitted."
        )