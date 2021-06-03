import csv
from collections import Counter

data = "hello"
new_data = Counter(data)
print(new_data.values())

numbers = [23,25,26,30,35,23,46,55]

def find_mean(number_list):
    num_sum = 0
    for i in number_list:
        num_sum = num_sum + i

    print(num_sum)
    mean = num_sum / len(numbers)
    print('Mean: ' + str(mean))



with open("./files/data/data.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)
    # print(file_data)