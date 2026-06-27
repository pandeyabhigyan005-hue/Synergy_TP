import json


def read_csv_manual(file_path: str) -> list[dict]:

    rows = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    header = lines[0].strip().split(",")

    for line in lines[1:]:

        line = line.strip()

        if line == "":
            continue

        values = line.split(",")

        if len(values) != len(header):
            continue

        row = {}

        for i in range(len(header)):
            row[header[i]] = values[i]

        rows.append(row)

    return rows


def convert_types(rows: list[dict]) -> list[dict]:

    for row in rows:

        row["score"] = int(row["score"])

        row["submitted"] = row["submitted"].lower()

    return rows


def calculate_summary(rows: list[dict]) -> dict:

    total_students = len(rows)

    submitted_students = 0
    missing_submissions = 0
    total_score = 0

    highest_score = -1
    highest_scorer = ""

    lowest_score = 100
    lowest_scorer = ""

    domain_scores = {}

    not_submitted = []

    below_5 = []


    for row in rows:

        total_score += row["score"]


        if row["submitted"] == "yes":

            submitted_students += 1

            if row["score"] < lowest_score:

                lowest_score = row["score"]

                lowest_scorer = row["name"]

        else:

            missing_submissions += 1

            not_submitted.append(row["name"])



        if row["score"] > highest_score:

            highest_score = row["score"]

            highest_scorer = row["name"]



        if row["score"] < 5:

            below_5.append(row["name"])



        domain = row["domain"]


        if domain not in domain_scores:

            domain_scores[domain] = []


        domain_scores[domain].append(row["score"])



    domain_average = {}


    for domain in domain_scores:


        avg = sum(domain_scores[domain])


        avg = avg / len(domain_scores[domain])


        domain_average[domain] = round(avg, 2)



    average_score = round(total_score / total_students, 2)



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