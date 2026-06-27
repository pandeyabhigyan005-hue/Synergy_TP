import pandas as pd
import json
def load_data(file_path: str):
    return pd.read_csv(file_path)
def generate_summary(df):

    summary = {

        "rows": len(df),

        "missing_values":
        df.isnull().sum().to_dict(),

        "duplicates":
        int(df.duplicated().sum()),

        "domains":
        df["domain"].unique().tolist()

    }

    # Only calculate average_score if score is numeric
    try:
        score_numeric = pd.to_numeric(df["score"], errors="coerce")

        summary["average_score"] = float(score_numeric.mean())

    except:
        summary["average_score"] = None


    return summary
def remove_duplicates(df):

    return df.drop_duplicates()
def standardize_domains(df):


    mapping={


        "ml":"ML",
        "machine learning":"ML",

        "web":"Web",
        "web dev":"Web",
        "web development":"Web",

        "electronics":"Electronics",

        "mechanical":"Mechanical"

    }


    df["domain"]=df["domain"].str.lower().str.strip()


    df["domain"]=df["domain"].replace(mapping)



    return df
def clean_attendance(df):


    df["attendance_percent"]=(

        df["attendance_percent"]

        .astype(str)

        .str.replace("%","")

    )


    df["attendance_percent"]=pd.to_numeric(

        df["attendance_percent"],

        errors="coerce"

    )


    df["attendance_percent"]=(
        df["attendance_percent"]
        .clip(0,100)
    )


    return df
def clean_scores(df):


    replace={

"zero":0,
"one":1,
"two":2,
"three":3,
"four":4,
"five":5,
"six":6,
"seven":7,
"eight":8,
"nine":9,
"ten":10

}


    df["score"]=df["score"].replace(replace)


    df["score"]=pd.to_numeric(

        df["score"],

        errors="coerce"

    )


    return df
def clean_study_hours(df):


    replace={

"zero":0,
"one":1,
"two":2,
"three":3,
"four":4,
"five":5,
"six":6,
"seven":7,
"eight":8

}

    df["study_hours"]=df["study_hours"].replace(replace)


    df["study_hours"]=pd.to_numeric(

        df["study_hours"],

        errors="coerce"

    )


    return df
def clean_height(df):

    heights=[]

    for value in df["height"]:

        if pd.isna(value):
            heights.append(None)
            continue


        value=str(value).strip()


        try:

            if "m" in value and "cm" not in value:

                number=float(value.replace("m",""))

                heights.append(number*100)

            else:

                number=float(value.replace("cm",""))

                heights.append(number)

        except:

            heights.append(None)



    df["height_cm"]=heights

    df.drop(columns=["height"],inplace=True)

    return df
def clean_weight(df):


    weights=[]


    for value in df["weight"]:


        if pd.isna(value):

            weights.append(None)

            continue


        value=str(value).strip()


        try:

            number=float(

                value.replace("kg","")

            )

            weights.append(number)


        except:


            weights.append(None)



    df["weight_kg"]=weights


    df.drop(columns=["weight"],inplace=True)


    return df
def clean_submitted(df):


    mapping={


        "yes":"yes",
        "y":"yes",

        "no":"no",
        "n":"no"


    }


    df["submitted"]=(

        df["submitted"]

        .str.lower()

        .map(mapping)

    )


    return df
def handle_missing_values(df):


    df["attendance_percent"].fillna(

        df["attendance_percent"].median(),

        inplace=True

    )


    df["score"].fillna(

        df["score"].median(),

        inplace=True

    )


    df["study_hours"].fillna(

        df["study_hours"].median(),

        inplace=True

    )


    df["height_cm"].fillna(

        df["height_cm"].median(),

        inplace=True

    )


    df["weight_kg"].fillna(

        df["weight_kg"].median(),

        inplace=True

    )


    df["submitted"].fillna(

        "no",

        inplace=True

    )


    return df
def save_cleaned_data(df, output_path):


    df.to_csv(

        output_path,

        index=False

    )
def write_report(report_path):

    report = """
# Cleaning Report

Removed duplicate rows.

Standardized domains.

Converted attendance values.

Converted text numbers.

Converted heights to centimeters.

Converted weights to kilograms.

Missing values filled using median.

Attendance values clipped between 0 and 100.

"""

    with open(report_path, "w") as f:
        f.write(report)