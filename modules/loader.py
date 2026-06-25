import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SHEET_ID = "18__D2Of5hKvidG40RQiAy_2gEDmayrlg9-0Mn97W8HE"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

LOCAL_FILE = "modules/study-analytics-dashboard-fab5a1f8904e.json"


@st.cache_data(ttl=300)
def load_sheet():
    try:
        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=SCOPES,
        )

    except Exception:
        credentials = Credentials.from_service_account_file(
            LOCAL_FILE,
            scopes=SCOPES,
        )

    client = gspread.authorize(credentials)

    sheet = client.open_by_key(SHEET_ID).sheet1

    data = sheet.get_all_records()

    return pd.DataFrame(data)
