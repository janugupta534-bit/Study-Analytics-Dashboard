import streamlit as st


def apply_filters(df):

    st.sidebar.title("📊 Filters")

    # Date Filter
    dates = sorted(df["Date"].dropna().unique())
    selected_dates = st.sidebar.multiselect(
        "📅 Date",
        dates,
        default=dates
    )

    # Student Filter
    students = sorted(df["Name"].unique())
    selected_students = st.sidebar.multiselect(
        "👤 Student",
        students,
        default=students
    )

    # Subject Filter
    subjects = sorted(df["Subject"].unique())
    selected_subjects = st.sidebar.multiselect(
        "📚 Subject",
        subjects,
        default=subjects
    )

    # Session Type Filter
    session_types = sorted(df["Session Type"].unique())
    selected_sessions = st.sidebar.multiselect(
        "📝 Session Type",
        session_types,
        default=session_types
    )

    filtered_df = df[
        (df["Date"].isin(selected_dates))
        & (df["Name"].isin(selected_students))
        & (df["Subject"].isin(selected_subjects))
        & (df["Session Type"].isin(selected_sessions))
    ]

    return filtered_df