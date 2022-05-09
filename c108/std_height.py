import random
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data.csv')
weight = df["Weight(Pounds)"].tolist()
mean = sum(weight)/len(weight)
std_devietion = statistics.stdev(weight)
median=statistics.median(weight)
mode=statistics.mode(weight)

first_std_deviation_start, first_std_deviation_end = mean - std_devietion, mean + std_devietion
second_std_deviation_start, second_std_deviation_end = mean - (2*std_devietion), mean + (2*std_devietion)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_devietion), mean + (3*std_devietion)

list_of_data_within_1_std_deviation = [result for result in weight if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in weight if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in weight if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(weight)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(weight)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(weight)))

fig = ff.create_distplot([weight], ["Weight"], show_hist=False)



fig.show()

