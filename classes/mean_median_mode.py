import csv
from collections import Counter

def find_mean(data):
    sum_of_data = 0

    for i in data:
        sum_of_data = sum_of_data + i
    print("Total Sum Of Data: " + str(sum_of_data))

    mean = sum_of_data / len(data)
    print("Mean Of Data: " + str(mean))

def find_median(data):
    
    data.sort()
    data_length = len(data)
    if data_length % 2 == 0:
        first_num = float(data[data_length // 2])
        second_num = float(data[data_length // 2 - 1])
        
        median = (first_num + second_num) / 2
    else:
        median = float(data[data_length // 2])
    print("Median: " + str(median))

def find_mode(data):
    data.sort()
    count_data = Counter(data)
    mode_occurence = 0
    final_mode = 0
    mode_data_for_range = {"60-70": 0, "70-80": 0}

    for height, occurence in count_data.items():
        if 60 <= float(height) <= 70:
            mode_data_for_range["60-70"] += occurence
        elif 70 <= float(height) <= 80:
            mode_data_for_range["70-80"] += occurence

    for eachRange, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range = [int(eachRange.split("-")[0]), int(eachRange.split("-")[1])]
            mode_occurence = occurence
            final_mode = float((mode_range[0] + mode_range[1]) / 2)

    print('Mode Between Ranges: ' + str(mode_data_for_range))
    print('Final Mode: ' + str(final_mode))



with open("./files/data/SOCR-HeightWeight.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in file_data:
    new_data.append(float(i[1]))

find_mean(new_data)
find_median(new_data)
find_mode(new_data)