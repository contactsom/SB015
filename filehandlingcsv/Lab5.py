import csv


with open('teacher.csv', mode='r') as file:
    reader= csv.reader(file)

    for i in reader:
       print(i)

