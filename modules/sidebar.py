import streamlit as st


def apply_filters(df):

    st.sidebar.title("📚 Dashboard Filters")

    student = st.sidebar.selectbox(
        "👤 Select Student",
        ["All Students"] + sorted(df["Name"].unique())
    )

    if student != "All Students":
        df = df[df["Name"] == student]

    return df
