import csv
import numpy as np

first_names = []
last_names = []
exam1 = []
exam2 = []
exam3 = []
grades = [first_names, last_names, exam1, exam2, exam3]

with open('grades.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    for i in range(3):
        print(next(csvreader))

    csvfile.seek(0)
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        for i in range(5):
            if i == 0:
                first_names.append(row[i])
            elif i == 1:
                last_names.append(row[i])
            elif i == 2:
                exam1.append(int(row[i]))
            elif i == 3:
                exam2.append(int(row[i]))
            else:
                exam3.append(int(row[i]))

    print(grades)
