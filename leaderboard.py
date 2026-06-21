import streamlit as st
import pandas as pd

from sheets import get_logs_sheet
from streaks import (
    current_streak,
    longest_streak,
    last_active
)


def show_leaderboard():

    st.title("🏆 Friend Leaderboard")

    sheet = get_logs_sheet()
    data = sheet.get_all_values()

    if len(data) <= 1:
        st.warning("No data found.")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    df["Score"] = pd.to_numeric(
        df["Score"],
        errors="coerce"
    ).fillna(0)

    leaderboard = []

    for user in sorted(df["Username"].unique()):

        leaderboard.append(
            {
                "Username": user,
                "Score": int(
                    df[df["Username"] == user]["Score"].sum()
                ),
                "Current Streak": current_streak(user),
                "Longest Streak": longest_streak(user),
                "Last Active": last_active(user)
            }
        )

    board = pd.DataFrame(leaderboard)

    board = board.sort_values(
        by="Score",
        ascending=False
    )

    st.subheader("🏅 Rankings")

    board.index = range(
        1,
        len(board) + 1
    )

    st.dataframe(
        board,
        use_container_width=True
    )

    if len(board) > 0:

        winner = board.iloc[0]

        st.success(
            f"""
🏆 Top Performer: {winner['Username']}

⭐ Score: {winner['Score']}

🔥 Current Streak: {winner['Current Streak']}
"""
        )