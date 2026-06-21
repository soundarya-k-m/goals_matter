import streamlit as st
from datetime import date

from sheets import get_logs_sheet
from reminders import show_reminder


def calculate_score(workout, study, water, sleep):

    score = 0

    if workout == "Yes":
        score += 20

    if study >= 4:
        score += 30

    if water >= 3:
        score += 20

    if sleep >= 7:
        score += 30

    return score


def show_dashboard(username):

    st.title("🎯 Goals Matter")

    show_reminder(username)

    # ==========================================
    # HERO BANNER
    # ==========================================

    st.markdown("""
    <div style="
        padding:25px;
        border-radius:20px;
        background:linear-gradient(135deg,#3B82F6,#6366F1,#8B5CF6);
        color:white;
        margin-bottom:25px;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">
        <h2>🚀 Welcome to Goals Matter</h2>
        <p>
        Track goals, build streaks, compete with friends,
        and level up every day.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader(f"👋 Welcome, {username}")

    # ==========================================
    # QUICK STATUS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Daily Goal",
            "100"
        )

    with col2:
        st.metric(
            "🔥 Tracking",
            "ON"
        )

    with col3:
        st.metric(
            "🏆 Team Mode",
            "ACTIVE"
        )

    st.divider()

    # ==========================================
    # INPUT FORM
    # ==========================================

    st.subheader("📝 Daily Goal Submission")

    with st.container():

        workout = st.selectbox(
            "🏋️ Workout Completed?",
            ["Yes", "No"]
        )

        study = st.number_input(
            "📚 Study Hours",
            min_value=0.0,
            max_value=24.0,
            step=0.5
        )

        water = st.number_input(
            "💧 Water Intake (Litres)",
            min_value=0.0,
            max_value=20.0,
            step=0.5
        )

        sleep = st.number_input(
            "😴 Sleep Hours",
            min_value=0.0,
            max_value=24.0,
            step=0.5
        )

        live_score = calculate_score(
            workout,
            study,
            water,
            sleep
        )

        st.progress(live_score / 100)

        st.write(
            f"Current Score Preview: **{live_score}/100**"
        )

        if st.button("✅ Save Today's Log"):

            sheet = get_logs_sheet()

            today = str(date.today())

            score = calculate_score(
                workout,
                study,
                water,
                sleep
            )

            data = sheet.get_all_values()

            row_to_update = None

            for idx, row in enumerate(
                data[1:],
                start=2
            ):

                if len(row) < 2:
                    continue

                sheet_date = row[0].strip()
                sheet_user = row[1].strip()

                if (
                    sheet_date == today
                    and
                    sheet_user.lower() == username.lower()
                ):
                    row_to_update = idx
                    break

            if row_to_update:

                sheet.update(
                    range_name=f"A{row_to_update}:G{row_to_update}",
                    values=[[
                        today,
                        username,
                        workout,
                        study,
                        water,
                        sleep,
                        score
                    ]]
                )

                st.success(
                    f"✅ Updated today's entry! Score: {score}/100"
                )

            else:

                sheet.append_row([
                    today,
                    username,
                    workout,
                    study,
                    water,
                    sleep,
                    score
                ])

                st.success(
                    f"🎉 New entry saved! Score: {score}/100"
                )

            st.rerun()