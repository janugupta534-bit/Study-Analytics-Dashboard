import streamlit as st

from modules.loader import load_sheet
from modules.data_cleaner import clean_data
from modules.metrics import show_metrics
from modules.charts import show_charts
from modules.sidebar import apply_filters
from modules.leaderboard import show_leaderboard
# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(
    page_title="Study Analytics Dashboard",
    page_icon="📚",
    layout="wide"
)

# ------------------------------------
# Load Data
# ------------------------------------

df = load_sheet()
df = clean_data(df)

df = apply_filters(df)
# ------------------------------------
# Dashboard
# ------------------------------------

st.title("📚 Study Analytics Dashboard")

st.markdown("---")

show_metrics(df)

st.markdown("---")

show_charts(df)
st.markdown("---")

leaderboard = show_leaderboard(df)

st.markdown("---")

st.subheader("Study Records")

st.dataframe(
    df,
    use_container_width=True
)