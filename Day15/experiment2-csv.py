import csv

with open("files/csvfile.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:  # for lists in list
    if row[0] == city:
        print(row[1])
