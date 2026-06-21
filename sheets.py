import streamlit as st

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connect_sheet():

    creds_dict = dict(st.secrets["gcp_service_account"])

    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=SCOPES
    )
    
    client = gspread.authorize(creds)

    spreadsheet = client.open("GOALS MATTER")

    return spreadsheet


def get_users_sheet():
    return connect_sheet().worksheet("Users")


def get_logs_sheet():
    return connect_sheet().worksheet("DailyLogs")
