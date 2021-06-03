import csv
import pandas as pd
import plotly_express as pl

with open('files/data/standard_dev/class1.csv', newline="") as csv_file:
    data = list(csv.reader(csv_file))

data.pop(0)

def get_mean(data):
    total_sum = 0
    for marks in data:
        total_sum = total_sum + float(marks[1])
    
    mean_marks = total_sum / len(data)
    print("Average Marks in Class One: " + str(mean_marks))
    return mean_marks

mean_marks = get_mean(data)
    
pd_csv_file = pd.read_csv('files/data/standard_dev/class1.csv')
fig = pl.scatter(pd_csv_file, x="Student Number", y= "Marks")
fig.update_layout(shapes=[dict( type= 'line', y0= mean_marks, y1= mean_marks, x0= 0, x1= len(data))])

fig.show()
