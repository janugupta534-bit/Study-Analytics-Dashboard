import streamlit as st
import plotly.express as px


def show_charts(df):

    # ----------------------------
    # Row 1
    # ----------------------------

    left, right = st.columns(2)

    with left:

        st.subheader("📚 Subject Wise Study Hours")

        subject = (
            df.groupby("Subject")["Hours"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            subject,
            x="Subject",
            y="Hours",
            color="Subject",
            text="Hours"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        st.subheader("📝 Session Distribution")

        fig = px.pie(
            df,
            names="Session Type",
            hole=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ----------------------------
    # Row 2
    # ----------------------------

    st.subheader("📈 Study Hours Trend")

    trend = (
        df.groupby("Date")["Hours"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    fig = px.line(
        trend,
        x="Date",
        y="Hours",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)