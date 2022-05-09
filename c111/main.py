import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df= pd.read_csv('studentMarks.csv')

data = df["Math_score"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Mean: ", mean)
print("Standard Deviation: ", std_deviation)



fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
fig.show()

def random_set_of_mean(counter): 
    dataset= []
    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean of sampling distribution: ", mean)
# the mean of sampling distribution is the same as the mean of the original distribution
print("Standard Deviation of sampling distribution: ", std_deviation)
# the standard deviation of the sampling distribution = standard deviation of the population 
# divided by the square root of the sample size (100)


first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)

print("First Standard Deviation: ", first_std_deviation_start, " - ", first_std_deviation_end)
print("Second Standard Deviation: ", second_std_deviation_start, " - ", second_std_deviation_end)
print("Third Standard Deviation: ", third_std_deviation_start, " - ", third_std_deviation_end)


fig = ff.create_distplot([mean_list], ["Student marks"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode='lines', name="mean"))

fig.show()

