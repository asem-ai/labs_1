with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text) #1

with open("file.txt", "w", encoding="utf-8") as file:
    for i in range(1, 10):
        file.write(str(i) + "\n")#2

with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)#2

names = ["asem", "zhaniya", "adiya", "sholpan"]

with open("names.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip().capitalize())#3

with open("data.csv", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)#1

import csv

with open("file.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in range(1, 10):
        writer.writerow([i])

with open("file.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])#2

import csv

names = ["aliya", "askar", "dana", "marat"]

with open("names.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for name in names:
        writer.writerow([name])

with open("names.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0].capitalize())#3