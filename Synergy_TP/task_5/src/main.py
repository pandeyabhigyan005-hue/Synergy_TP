import sys

from visualize import *
input_file=sys.argv[1]

output_folder=sys.argv[2]
df=load_cleaned_data(

        input_file

)
plot_domain_average_score(


        df,


        output_folder+
        "/domain_average_score.png"

)


plot_attendance_vs_score(


        df,


        output_folder+
        "/attendance_vs_score.png"

)


plot_submission_status_count(


        df,


        output_folder+
        "/submission_status_count.png"

)
write_plot_summary(

output_folder+

"/plot_summary.md"

)