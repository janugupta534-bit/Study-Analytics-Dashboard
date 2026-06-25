import streamlit as st
import pandas as pd


def show_leaderboard(df):

    leaderboard = (
        df.groupby("Name")
        .agg(
            Total_Hours=("Hours", "sum"),
            Sessions=("Hours", "count"),
            Average_Session=("Hours", "mean")
        )
        .reset_index()
    )

    leaderboard["Average_Session"] = leaderboard["Average_Session"].round(2)

    leaderboard["Effective Score"] = (
        leaderboard["Total_Hours"] * 0.6
        + leaderboard["Average_Session"] * 25
    ).round(2)

    leaderboard = leaderboard.sort_values(
        "Effective Score",
        ascending=False
    ).reset_index(drop=True)

    leaderboard["Rank"] = leaderboard.index + 1

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    leaderboard["Medal"] = leaderboard["Rank"].map(medals).fillna("🏅")

    st.subheader("🏆 Study Leaderboard")

    st.dataframe(
        leaderboard[
            [
                "Medal",
                "Rank",
                "Name",
                "Total_Hours",
                "Sessions",
                "Average_Session",
                "Effective Score"
            ]
        ],
        use_container_width=True
    )

    return leaderboard