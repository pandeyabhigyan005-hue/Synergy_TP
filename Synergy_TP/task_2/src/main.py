import sys
from analyzer import *

try:

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    students = read_submissions(input_file)

    total_students = len(students)

    submitted_students = get_submitted_students(students)

    submitted_count = len(submitted_students)

    missing = get_missing_submissions(students)

    missing_count = len(missing)

    average_score = round(calculate_average_score(students), 2)

    highest = get_highest_scorer(students)

    lowest = get_lowest_submitted(students)

    domain_average = get_domain_wise_average(students)

    below_five = get_below_five(students)


    summary = {

        "total_students": total_students,

        "submitted_students": submitted_count,

        "missing_submissions": missing_count,

        "average_score": average_score,

        "highest_scorer": highest,

        "lowest_submitted_student": lowest,

        "domain_wise_average": domain_average,

        "students_missing_submission": missing,

        "students_below_five": below_five

    }


    write_summary(summary, output_file)



    print("Total Students :", total_students)

    print("Submitted :", submitted_count)

    print("Missing :", missing_count)

    print("Average Score :", average_score)

    print("Highest Scorer :", highest)

    print("Lowest Submitted Student :", lowest)

    print("Missing Submissions :", missing)

    print("Students Below 5 :", below_five)

    print(output_file, "written successfully")


except FileNotFoundError:
    print("Input file not found")


except ValueError:
    print("Invalid score value")


except IndexError:
    print("Please provide input and output filenames")


except Exception as e:
    print("Error :", e)
