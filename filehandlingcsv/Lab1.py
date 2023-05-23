import csv

with open("books.csv",'rt') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)