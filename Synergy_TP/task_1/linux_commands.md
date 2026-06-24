# Linux Commands(all are executed in bash)

## pwd:

### Command Used

pwd


### What It Does
Displays the current working directory.

### Output Observed

/C/Users/Admin/Documents/GitHub/Synergy_TP/Synergy_TP

## ls:

### Command Used
ls

### What It Does
Lists files and directories in the current directory.

### Output Observed
task_1  .gitignore

## ls -la:

### Command Used
ls -la

### What It Does
Lists all files including hidden files with detailed information.

### Output Observed
drwxr-xr-x task_1
-rw-r--r-- .gitignore

## cd:

### Command Used
cd task_1

### What It Does
Changes the current directory to task_1.

### Output Observed
No output

## mkdir:

### Command Used
mkdir test_folder


### What It Does
Creates a new directory named test_folder.

### Output Observed

No output


## touch:

### Command Used
touch file.txt


### What It Does
Creates an empty file.

### Output Observed

No output
## cat:

### Command Used

cat task_1/requirements.txt


### What It Does
Displays the contents of a file.

### Output Observed

numpy==2.5.0
pandas==3.0.3
python-dateutil==2.9.0.post0
six==1.17.0
tzdata==2026.2



## echo:

### Command Used

echo Hello World


### What It Does
Prints text to the terminal.

### Output Observed
Hello World

## cp:

### Command Used
cp file.txt copy.txt

### What It Does
Copies a file.

### Output Observed
No output


## mv:

### Command Used
mv copy.txt renamed.txt


### What It Does
Moves or renames a file.

### Output Observed
No output


---

## rm:

### Command Used

rm renamed.txt


### What It Does
Deletes a file.

### Output Observed
No output

## grep:

### Command Used

grep "Task" task_1/README.md


### What It Does
Searches for a pattern inside a file.

### Output Observed

# Task 1: GitHub, Virtual Environment, and Linux Basics


## find:

### Command Used

find . -name "*.py"


### What It Does
Searches for files matching a pattern.

### Output Observed

./task_1/src/hello.py


## head:

### Command Used
head task_1/requirements.txt

### What It Does
Displays the first 10 lines of a file.

### Output Observed
numpy==2.3.1


## tail:

### Command Used

tail task_1/requirements.txt


### What It Does
Displays the last 10 lines of a file.

### Output Observed

numpy==2.3.1


## wc:

### Command Used

wc task_1/requirements.txt


### What It Does
Counts lines, words, and characters in a file.

### Output Observed

1 1 13 task_1/requirements.txt




## chmod:

### Command Used

chmod +x script.sh


### What It Does
Changes file permissions.

### Output Observed

No output
