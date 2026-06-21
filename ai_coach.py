import streamlit as st
import pandas as pd

from sheets import get_logs_sheet


def show_ai_coach(username):

    st.subheader("🤖 AI Coach")

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        st.info("No data available.")
        return

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    user_df = df[
        df["Username"].astype(str).str.lower()
        == str(username).lower()
    ]

    if len(user_df) == 0:
        st.info("No logs available.")
        return

    user_df["Study"] = pd.to_numeric(
        user_df["Study"],
        errors="coerce"
    ).fillna(0)

    user_df["Water Intake"] = pd.to_numeric(
        user_df["Water Intake"],
        errors="coerce"
    ).fillna(0)

    user_df["Sleep"] = pd.to_numeric(
        user_df["Sleep"],
        errors="coerce"
    ).fillna(0)

    workout_days = len(
        user_df[
            user_df["Workout"] == "Yes"
        ]
    )

    avg_study = round(
        user_df["Study"].mean(),
        1
    )

    avg_water = round(
        user_df["Water Intake"].mean(),
        1
    )

    avg_sleep = round(
        user_df["Sleep"].mean(),
        1
    )

    advice = []

    if workout_days >= 5:
        advice.append(
            "💪 Excellent workout consistency."
        )
    else:
        advice.append(
            "🏃 Try exercising more regularly."
        )

    if avg_study >= 5:
        advice.append(
            "📚 Great study discipline."
        )
    else:
        advice.append(
            "📖 Increase study time by 1-2 hours daily."
        )

    if avg_water >= 3:
        advice.append(
            "💧 Hydration is on track."
        )
    else:
        advice.append(
            "🚰 Drink more water daily."
        )

    if avg_sleep >= 7:
        advice.append(
            "😴 Sleep schedule looks healthy."
        )
    else:
        advice.append(
            "🛌 Aim for at least 7 hours of sleep."
        )

    st.success(
        "Personalized recommendations generated."
    )

    for item in advice:
        st.write(item)