import streamlit as st
from modules.calculations import (
    total_sessions,
    total_hours,
    total_subjects,
    total_students,
)


def show_metrics(df):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📖 Sessions", total_sessions(df))
    c2.metric("⏳ Hours", total_hours(df))
    c3.metric("📚 Subjects", total_subjects(df))
    c4.metric("👤 Students", total_students(df))