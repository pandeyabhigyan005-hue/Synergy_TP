import pandas as pd
import matplotlib.pyplot as plt
def load_cleaned_data(file_path):

    return pd.read_csv(file_path)
def plot_domain_average_score(df, output_path):

    avg_scores = (
        df.groupby("domain")["score"]
        .mean()
    )

    plt.figure(figsize=(6,4))

    bars = plt.bar(
        avg_scores.index,
        avg_scores.values
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.1,
            f"{height:.1f}",
            ha="center"
        )

    plt.title("Average Score by Domain")

    plt.xlabel("Domain")

    plt.ylabel("Average Score")

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()
def plot_attendance_vs_score(df, output_path):



    plt.figure(

        figsize=(6,4)

    )


    plt.scatter(

        df["attendance_percent"],

        df["score"]

    )



    plt.title(

        "Attendance vs Score"

    )


    plt.xlabel(

        "Attendance (%)"

    )


    plt.ylabel(

        "Score"

    )


    plt.tight_layout()



    plt.savefig(

        output_path

    )


    plt.close()
def plot_submission_status_count(df,output_path):

    counts=(

        df["submitted"]

        .value_counts()

    )



    plt.figure(

        figsize=(6,4)

    )


    plt.bar(

        counts.index,

        counts.values

    )



    plt.title(

        "Submission Status"

    )


    plt.xlabel(

        "Submitted"

    )


    plt.ylabel(

        "Count"

    )


    plt.tight_layout()



    plt.savefig(

        output_path

    )


    plt.close()
def write_plot_summary(output_path):



    summary="""


# Plot Summary


domain_average_score.png


Shows the average score obtained by students in each domain.



attendance_vs_score.png


Shows the relationship between attendance and score.



submission_status_count.png


Shows the number of students who submitted and did not submit.



"""


    with open(

            output_path,

            "w"

    ) as file:


        file.write(summary)