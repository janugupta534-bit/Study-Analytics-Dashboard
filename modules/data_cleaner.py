import pandas as pd

def clean_data(df):

    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    df["Start Time"] = pd.to_datetime(
        df["Start Time"],
        format="mixed",
        errors="coerce"
    )

    df["End Time"] = pd.to_datetime(
        df["End Time"],
        format="mixed",
        errors="coerce"
    )

    df["Hours"] = (
        df["End Time"] - df["Start Time"]
    ).dt.total_seconds() / 3600

    return df