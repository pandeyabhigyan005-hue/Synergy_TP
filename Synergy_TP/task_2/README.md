# Task 2: Python Recap Assignment

## Description

This task reads student submission data from task_2/data/submissions.csv and generates a summary report in task_2/output/summary.json.

## Run Command

```powershell
 python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

## Output

The program generates:
```powershell
task_2/output/summary.json
Total Students : 7
Submitted : 5
Missing : 2
Average Score : 4.857142857142857
Highest Scorer : Isha
Lowest Submitted Student : Rohan
Missing Submissions : ['Kabir', 'Dev']
Students Below 5 : ['Rohan']