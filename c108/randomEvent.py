import random
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go

print('start')

count = []
dice_result = []

for i in range(0, 1000):
    print('it', i)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

mean = sum(dice_result)/len(dice_result)
std_devietion = statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)


first_std_deviation_start, first_std_deviation_end = mean - std_devietion, mean + std_devietion
second_std_deviation_start, second_std_deviation_end = mean - (2*std_devietion), mean + (2*std_devietion)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_devietion), mean + (3*std_devietion)

list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))
print(mean)
print(std_devietion)
print(median)
print(mode)


#Normal distribution - Gaussian Distribution
fig = ff.create_distplot([dice_result], ["Dice Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode='lines', name='mean'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode='lines', name='first_std_deviation'))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode='lines', name='first_std_deviation'))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode='lines', name='second_std_deviation'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode='lines', name='second_std_deviation'))
fig.show()

#py randomEvent.py