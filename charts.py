import streamlit as st
import plotly.express as px


def show_charts(df):

    st.header("📊 Student Comparison Dashboard")

    # ===========================
    # Total Study Hours
    # ===========================

    total_hours = (
        df.groupby("Name")["Hours"]
        .sum()
        .reset_index()
        .sort_values("Hours", ascending=False)
    )

    fig1 = px.bar(
        total_hours,
        x="Name",
        y="Hours",
        color="Name",
        text_auto=".1f",
        title="🏆 Total Study Hours"
    )

    fig1.update_layout(showlegend=False)

    st.plotly_chart(fig1, use_container_width=True)

    # ===========================
    # Number of Sessions
    # ===========================

    sessions = (
        df.groupby("Name")
        .size()
        .reset_index(name="Sessions")
        .sort_values("Sessions", ascending=False)
    )

    fig2 = px.bar(
        sessions,
        x="Name",
        y="Sessions",
        color="Name",
        text_auto=True,
        title="📚 Number of Study Sessions"
    )

    fig2.update_layout(showlegend=False)

    st.plotly_chart(fig2, use_container_width=True)

    # ===========================
    # Average Session Duration
    # ===========================

    average = (
        df.groupby("Name")["Hours"]
        .mean()
        .reset_index()
        .sort_values("Hours", ascending=False)
    )

    fig3 = px.bar(
        average,
        x="Name",
        y="Hours",
        color="Name",
        text_auto=".2f",
        title="⏱ Average Session Duration"
    )

    fig3.update_layout(showlegend=False)

    st.plotly_chart(fig3, use_container_width=True)

    # ===========================
    # Daily Progress
    # ===========================

    daily = (
        df.groupby(["Date", "Name"])["Hours"]
        .sum()
        .reset_index()
    )

    fig4 = px.line(
        daily,
        x="Date",
        y="Hours",
        color="Name",
        markers=True,
        title="📈 Daily Study Trend"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ===========================
    # Contribution Pie Chart
    # ===========================

    contribution = (
        df.groupby("Name")["Hours"]
        .sum()
        .reset_index()
    )

    fig5 = px.pie(
        contribution,
        names="Name",
        values="Hours",
        hole=0.55,
        title="🎯 Share of Total Study Hours"
    )

    st.plotly_chart(fig5, use_container_width=True)

    # ===========================
    # Cumulative Progress
    # ===========================

    cumulative = (
        df.groupby(["Date", "Name"])["Hours"]
        .sum()
        .groupby(level=1)
        .cumsum()
        .reset_index()
    )

    fig6 = px.line(
        cumulative,
        x="Date",
        y="Hours",
        color="Name",
        markers=True,
        title="🚀 Cumulative Study Hours"
    )

    st.plotly_chart(fig6, use_container_width=True)
