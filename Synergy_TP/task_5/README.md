# Task 5: Matplotlib Visualization from Cleaned Data

## 1. Task Objective

The objective of this task is to Generate three properly labeled plots from the cleaned dataset produced in Task 4. 

---

## 2. Folder Structure

```text
task_5/
│
├── README.md
│
├── output/
│   ├── domain_average_score.png
│   ├── attendance_vs_score.png
│   ├── submission_status_count.png
│   └── plot_summary.md
│
└── src/
    ├── visualize.py
    └── main.py
```

---

## 3. Required Packages

* pandas
* matplotlib

Install them using:

```powershell
pip install pandas matplotlib
```

---

## 4. Setup Instructions

1. Open PowerShell in the root directory of the repository.

2. Install the required packages if they are not already installed.

```powershell
pip install pandas matplotlib
```

3. Ensure that the cleaned dataset generated in Task 4 exists at:

```text
task_4/output/cleaned_students.csv
```

---

## 5. Exact Run Command

Run the following command from the root directory of the repository:

```powershell
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

---

## 6. Expected Output Files

After execution, the following files will be created:

```text
task_5/output/domain_average_score.png

task_5/output/attendance_vs_score.png

task_5/output/submission_status_count.png

task_5/output/plot_summary.md
```

---

## 7. Short Explanation of the Implemented Logic

The program loads the cleaned dataset from Task 4 and generates three plots using matplotlib.

* A bar chart showing the average score for each domain.
* A scatter plot showing the relationship between attendance percentage and score.
* A bar chart showing the number of students who submitted and did not submit their work.

Each plot is given a title, axis labels, and is saved as a PNG file. A short summary describing the plots is also generated.

---

## 8. Plot Summary Generation Instructions

The plot summary file is generated automatically when `main.py` is executed.

Final summary file:

```text
task_5/output/plot_summary.md
```
