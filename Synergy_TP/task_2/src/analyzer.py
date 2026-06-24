import csv
import json
def read_submissions(filename: str) -> list:
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["score"] = int(row["score"])
            data.append(row)

    return data
def get_submitted_students(data: list) -> list:
    submitted = []

    for student in data:
        if student["submitted"] == "yes":
            submitted.append(student)

    return submitted
def calculate_average_score(data: list) -> float:
    total = 0

    for student in data:
        total += student["score"]

    return total / len(data)
def get_domain_wise_average(data: list) -> dict:
    domain_scores = {}

    for student in data:
        domain = student["domain"]
        score = student["score"]

        if domain not in domain_scores:
            domain_scores[domain] = []

        domain_scores[domain].append(score)

    averages = {}

    for domain in domain_scores:
        averages[domain] = sum(domain_scores[domain]) / len(domain_scores[domain])

    return averages
def get_missing_submissions(data: list) -> list:
    missing = []

    for student in data:
        if student["submitted"] == "no":
            missing.append(student["name"])

    return missing
import os
def write_summary(summary: dict, filename: str) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        json.dump(summary, file, indent=4)
        
def get_highest_scorer(data: list) -> str:
    highest = data[0]

    for student in data:
        if student["score"] > highest["score"]:
            highest = student

    return highest["name"]
def get_lowest_submitted(data: list) -> str:
    submitted = get_submitted_students(data)

    lowest = submitted[0]

    for student in submitted:
        if student["score"] < lowest["score"]:
            lowest = student

    return lowest["name"]
def get_below_five(data: list) -> list:
    below_five = []

    for student in data:
        if student["submitted"] == "yes" and student["score"] < 5:
            below_five.append(student["name"])

    return below_five