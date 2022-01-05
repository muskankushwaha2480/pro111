import pandas as pd 
import csv
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go
import random

df=pd.read_csv("medium_data.csv")
data = df['reading_time'].tolist()

#fig =ff.create_distplot([data], ['Math_score'], show_hist = False)
#fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean of Data = ", mean)
print("Std_deviation of the Data = " , std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

mean_list =[]
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)

print("Mean of Sampling Distribution  = ", mean)
print("Std_deviation of Sampling Distribution = " , std_deviation)

#fig =ff.create_distplot([mean_list], ['Student_marks'], show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode = 'lines' , name = 'MEAN'))
#fig.show()

first_std_deviation_start,first_std_deviation_end = mean-std_deviation , mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation) , mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation) , mean+(3*std_deviation)

print("std1 - " , first_std_deviation_start, first_std_deviation_end)
print("std2 - " , second_std_deviation_start , second_std_deviation_end)
print("std3 - " , third_std_deviation_start, third_std_deviation_end)

fig =ff.create_distplot([mean_list], ['Student_marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines' , name = 'MEAN'))
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start], y = [0,0.17], mode = 'lines' , name = 'std_deviation 1 start'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17], mode = 'lines' , name = 'std_deviation 1 end'))

fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start], y = [0,0.17], mode = 'lines' , name = 'std_deviation 2 start'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17], mode = 'lines' , name = 'std_deviation 2 end'))

fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start], y = [0,0.17], mode = 'lines' , name = 'std_deviation 3 start'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end], y = [0,0.17], mode = 'lines' , name = 'std_deviation 3 end'))

fig.show()


df=pd.read_csv("medium_data.csv")
data = df['reading_time'].tolist()

mean_of_sample1 = statistics.mean(data)
print("Mean of sample1  = ", mean_of_sample1)

fig =ff.create_distplot([mean_list], ['reading_time'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines' , name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_of_sample1,mean_of_sample1], y = [0,0.17], mode = 'lines' , name = 'mean of sample'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17], mode = 'lines' , name = 'std_deviation 2 end'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end], y = [0,0.17], mode = 'lines' , name = 'std_deviation 3 end'))

fig.show()

#Finding the z score using the formula

z_score = (mean_of_sample1-mean)/std_deviation
print("The z-score of sample1 is - " , z_score)