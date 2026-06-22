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

        stored_username = str(row[0]).strip()
        stored_password = str(row[1]).strip()

        if (
            stored_username.lower() == username.strip().lower()
            and stored_password == password.strip()
        ):
            return True

    return False

def user_exists(username):
    users_sheet = get_users_sheet()

    data = users_sheet.get_all_values()

    for row in data[1:]:
        if len(row) < 1:
            continue

        if row[0].strip().lower() == username.strip().lower():
            return True

    return False

def create_user(username, password):
    users_sheet = get_users_sheet()

    users_sheet.append_row([
        username.strip(),
        password.strip()
    ])

def login_page():

st.title("🎯 GOALS MATTER")

tab1, tab2 = st.tabs(
    ["🔑 Login", "🆕 Sign Up"]
)

# LOGIN TAB

with tab1:

    st.subheader("Login")

    username = st.text_input(
        "Username",
        key="login_user"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        if username == "" or password == "":

            st.warning(
                "Please enter username and password"
            )

        elif verify_user(
            username,
            password
        ):

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(
                "Login Successful"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )

# SIGNUP TAB

with tab2:

    st.subheader("Create New Account")

    new_username = st.text_input(
        "Choose Username",
        key="signup_user"
    )

    new_password = st.text_input(
        "Choose Password",
        type="password",
        key="signup_pass"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        key="signup_confirm"
    )

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        if (
            new_username == ""
            or new_password == ""
        ):

            st.warning(
                "Please fill all fields"
            )

        elif user_exists(
            new_username
        ):

            st.error(
                "Username already exists"
            )

        elif (
            new_password
            != confirm_password
        ):

            st.error(
                "Passwords do not match"
            )

        else:

            create_user(
                new_username,
                new_password
            )

            st.success(
                "Account created successfully. Please login."
            )

def logout():

st.session_state.logged_in = False
st.session_state.username = ""

st.rerun()