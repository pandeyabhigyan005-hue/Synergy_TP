# Task 3: Manual CSV Parser and Pandas Comparison

## 1. Task Objective

The objective of this task is to build a CSV parser manually using Python file I/O, then repeat the same analysis using pandas. The purpose of this task is to understand how raw CSV text becomes structured Python data before relying on high-level libraries.

---

## 2. Folder Structure

task_3/
│
├── README.md
├── data/
│   └── submissions.csv
│
├── output/
│   ├── manual_summary.json
│   ├── pandas_summary.json
│   └── comparison_report.md
│
└── src/
    ├── manual_parser.py
    ├── pandas_parser.py
    └── main.py


---

## 3. Required Packages

The following package is required:

- pandas

Install it using:

```
pip install pandas
```

---

## 4. Setup Instructions

1. Open PowerShell or Command Prompt in the root directory of the `Synergy_TP` repository.

2. Install pandas if it is not already installed.

```
pip install pandas
```

3. Make sure that `submissions.csv` is present inside `task_3/data/`.

---

## 5. Exact Run Command

Run the program from the root directory of the repository using:

```
python task_3/src/main.py task_3/data/submissions.csv
```

---

## 6. Expected Output Files

After successful execution, the following files will be generated inside `task_3/output/`:

- `manual_summary.json`
- `pandas_summary.json`
- `comparison_report.md`

---

## 7. Short Explanation of the Implemented Logic

The CSV file is first read manually using Python file handling. Each row is converted into a dictionary, and the score and submission status values are converted into suitable data types. Summary statistics such as average score, highest scorer, domain-wise averages, and student lists are then calculated.

The same analysis is performed again using pandas. Both summaries are saved as JSON files and compared to check whether they produce the same results.