import pandas as pd
import json


def read_csv_pandas(file_path: str):

    return pd.read_csv(file_path)



def calculate_summary_pandas(df) -> dict:


    df["submitted"] = df["submitted"].str.lower()



    total_students = len(df)


    submitted_students = len(

        df[df["submitted"] == "yes"]

    )



    missing_submissions = len(

        df[df["submitted"] == "no"]

    )



    average_score = round(

        df["score"].mean(),

        2

    )



    highest_scorer = df.loc[

        df["score"].idxmax(),

        "name"

    ]



    submitted = df[

        df["submitted"] == "yes"

    ]



    lowest_scorer = submitted.loc[

        submitted["score"].idxmin(),

        "name"

    ]



    domain_average = {}


    grouped = df.groupby("domain")["score"].mean()


    for domain in grouped.index:


        domain_average[domain] = round(

            grouped[domain],

            2

        )



    not_submitted = df[

        df["submitted"] == "no"

    ]["name"].tolist()



    below_5 = df[

        df["score"] < 5

    ]["name"].tolist()



    summary = {


        "total_students": total_students,

        "submitted_students": submitted_students,

        "missing_submissions": missing_submissions,

        "average_score": average_score,

        "highest_scorer": highest_scorer,

        "lowest_scorer_among_submitted": lowest_scorer,

        "domain_average_score": domain_average,

        "students_not_submitted": not_submitted,

        "students_below_5": below_5

    }


    return summary



def write_json(data: dict, output_path: str) -> None:


    with open(output_path, "w") as file:


        json.dump(data, file, indent=4)