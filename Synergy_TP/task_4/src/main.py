import sys
import json

from clean_data import *
from validate_data import *


if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    input_file = "task_4/data/messy_students.csv"
    output_file = "task_4/output/cleaned_students.csv"


df=load_data(input_file)


before=generate_summary(df)


df=remove_duplicates(df)

df=standardize_domains(df)

df=clean_attendance(df)

df=clean_scores(df)

df=clean_study_hours(df)

df=clean_height(df)

df=clean_weight(df)

df=clean_submitted(df)

df=handle_missing_values(df)



after=generate_summary(df)



save_cleaned_data(

    df,

    output_file

)



with open(

"task_4/output/summary_before.json",

"w"

) as f:


    json.dump(

        before,

        f,

        indent=4

    )



with open(

"task_4/output/summary_after.json",

"w"

) as f:


    json.dump(

        after,

        f,

        indent=4

    )



write_report(

"task_4/output/cleaning_report.md"

)



if validate_cleaned_data(df):


    print("Validation Passed")


else:


    print("Validation Failed")