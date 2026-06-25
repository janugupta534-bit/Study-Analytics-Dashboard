def total_sessions(df):
    return len(df)


def total_hours(df):
    return round(df["Hours"].sum(), 2)


def total_subjects(df):
    return df["Subject"].nunique()


def total_students(df):
    return df["Name"].nunique()