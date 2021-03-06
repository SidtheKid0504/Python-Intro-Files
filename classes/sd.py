import csv
import math

with open('files/data/standard_dev/data.csv', newline="") as csv_file:
    data = list(csv.reader(csv_file))

data = data[0]
print(data)

def get_mean(data):
    total_sum = 0
    for i in data:
        total_sum = total_sum + float(i)
    
    return total_sum / len(data)

def calc_standard_dev(data):
    mean = get_mean(data)
    sqr_list = []
    total_sqr_sum = 0

    for eachNum in data:
        x = float(eachNum) - mean
        x = x**2
        sqr_list.append(x)
    
    for eachSqr in sqr_list:
        total_sqr_sum = total_sqr_sum + eachSqr
    
    final_sd = math.sqrt(total_sqr_sum / (len(data) - 1))
    print("Standard Deviation: " + str(final_sd))
calc_standard_dev(data)
