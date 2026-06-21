import streamlit as st
import pandas as pd

from sheets import get_logs_sheet
from xp_system import (
    calculate_xp,
    get_level
)


def show_levels():

    st.title("🎖️ XP & Levels")

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        st.warning("No data available.")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    users = sorted(
        df["Username"].unique()
    )

    ranking = []

    for user in users:

        xp = calculate_xp(user)

        level_name, level_num = get_level(xp)

        ranking.append(
            {
                "Username": user,
                "Level": level_name,
                "Level No": level_num,
                "XP": xp
            }
        )

    board = pd.DataFrame(
        ranking
    )

    board = board.sort_values(
        by="XP",
        ascending=False
    )

    st.dataframe(
        board,
        use_container_width=True
    )

    st.divider()

    for _, row in board.iterrows():

        st.subheader(
            f"{row['Level']} {row['Username']}"
        )

        st.write(
            f"XP: {row['XP']}"
        )

        progress = min(
            row["XP"] / 5000,
            1.0
        )

        st.progress(progress)

        st.markdown("---")