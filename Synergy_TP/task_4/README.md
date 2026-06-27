# Task 4: Messy CSV Cleaning

## 1. Task Objective

The objective of this task is to clean a messy CSV dataset using pandas and produce a clean dataset, validation checks, and a written cleaning report.

## 2. Folder Structure


task_4/
│
├── README.md
├── data/
│   └── messy_students.csv
│
├── output/
│   ├── cleaned_students.csv
│   ├── summary_before.json
│   ├── summary_after.json
│   └── cleaning_report.md
│
└── src/
    ├── clean_data.py
    ├── validate_data.py
    └── main.py
```

---

## 3. Required Packages

* pandas

Install it using:

```powershell
pip install pandas
```

---

## 4. Setup Instructions

1. Open PowerShell in the root directory of the repository.
2. Install pandas if it is not already installed.

```powershell
pip install pandas
```

3. Ensure that the input file exists at:


task_4/data/messy_students.csv


---

## 5. Exact Run Command

Run the following command from the root directory of the repository:

```powershell
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
```

---

## 6. Expected Output Files

After execution, the following files will be created:


task_4/output/cleaned_students.csv
task_4/output/summary_before.json
task_4/output/summary_after.json
task_4/output/cleaning_report.md


---

## 7. Short Explanation of the Implemented Logic

The program loads the CSV file and removes duplicate rows. Domain names are standardized, percentages and text values are converted to numbers, heights and weights are converted to consistent units, and submitted values are normalized. Missing and invalid values are handled using predefined rules. The cleaned data is validated and saved along with summaries and a cleaning report.

---

## 8. Report Generation Instructions

The cleaning report is generated automatically when `main.py` is executed.

Final report file:

task_4/output/cleaning_report.md

