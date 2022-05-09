import plotly_express as px
import csv 

with open('data/student_marks.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Temperature", y="Ice-cream Sales( â‚¹ )")
    fig.show()