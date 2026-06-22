import streamlit as st
from sheets import get_users_sheet


def initialize_session():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""


def verify_user(username, password):

    users_sheet = get_users_sheet()

    data = users_sheet.get_all_values()

    for row in data[1:]:

        if len(row) < 2:
            continue

        if (
            row[0].strip().lower() == username.strip().lower()
            and row[1].strip() == password.strip()
        ):
            return True

    return False


def login_page():

    st.title("🎯 GOALS MATTER")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if verify_user(username, password):

            st.session_state.logged_in = True
            st.session_state.username = username

            st.rerun()

        else:

            st.error("Invalid Username or Password")


def logout():

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.rerun()