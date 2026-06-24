# Setup Log


# Creating folders
mkdir task_1
mkdir task_1\src
mkdir task_1\data

# Creating virtual environment
python -m venv task_1\venv

# Activating virtual environment
task_1\venv\Scripts\activate

# Installing package
pip install pandas

# Generating requirements.txt
pip freeze > task_1\requirements.txt

# Testing Python script
python task_1/src/hello.py

# repository was committed and pushed using github desktop

