import plotly_express as px
import csv 
import numpy as np 

def getDataSource(data_path):
    size_of_tv = []
    avarage_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            print(row)
            avarage_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return { "x": size_of_tv, "y": avarage_time_spent }

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corelation between size of tv and avarage time spent: ", correlation[0,1])

def setup():
    data_path = "./data/tv.csv"
    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 

setup()

## incomplete disscussion or explain