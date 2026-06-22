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

    # Skip header row
    for row in data[1:]:

        if len(row) < 2:
            continue

        stored_username = str(row[0]).strip()
        stored_password = str(row[1]).strip()

        if (
            stored_username == username.strip()
            and stored_password == password.strip()
        ):
            return True

    return False


def login_page():

    st.title("🎯 GOALS MATTER")
    st.subheader("Login")

    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    if st.button("Login", use_container_width=True):

        if username == "" or password == "":
            st.warning("Please enter username and password")

        elif verify_user(username, password):

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Username or Password")


def logout():

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.rerun()
