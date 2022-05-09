import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

import random
import pandas as pd
import csv


df= pd.read_csv('temp.csv')
data=df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Population mean: ", population_mean)     # mean of the population
print("Standard deviation: ", std_deviation)    # standard deviation of the population

def show_fig(mean_list):
    df= mean_list
    fig = ff.create_distplot([data], ["Temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0,1], mode='lines', name="Mean"))
    fig.show()

show_fig(data)

dataset = []

for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean= statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("mean", mean)
print("std_deviation", std_deviation)

