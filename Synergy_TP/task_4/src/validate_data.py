import pandas as pd
def validate_cleaned_data(df):


    if df["student_id"].duplicated().any():
        return False


    if not df["attendance_percent"].between(0,100).all():
        return False


    if not pd.api.types.is_numeric_dtype(df["score"]):
        return False


    if not pd.api.types.is_numeric_dtype(df["study_hours"]):
        return False


    if not pd.api.types.is_numeric_dtype(df["height_cm"]):
        return False


    if not pd.api.types.is_numeric_dtype(df["weight_kg"]):
        return False


    allowed=["yes","no"]


    if not df["submitted"].isin(allowed).all():
        return False


    allowed_domains=[

        "ML",

        "Web",

        "Electronics",

        "Mechanical"

    ]


    if not df["domain"].isin(

            allowed_domains

    ).all():

        return False


    critical=[

        "student_id",

        "domain",

        "score"

    ]


    if df[critical].isnull().any().any():

        return False


    return True