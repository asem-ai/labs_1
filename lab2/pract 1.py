import csv

from lab2.tasks import departments, salaries

file=open("employees.csv","w",encoding="utf-8")
file.write("name,department,salary")
file.write("Ali,IT,500000\n")
file.write("Dana,HR,300000\n")
file.write("Arman,IT,600000\n")
file.write("Aruzhan,Marketing,400000\n")
file.write("Dias,IT,450000\n")
file.close()
with open("employees.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        names.append(row["name"])
        departments.append(row["department"])
        salaries.append(int(row["salary"]))
total=0
for s in salaries:
    total+=s
average=total/len(salaries)
dept_salaries={}
for i in range(len(departments)):
    dept=departments[i]
    salary=salaries[i]
    if dept not in dept_salaries:
        dept_salaries[dept]=[]
    else:
        dept_salaries[dept].append(salary)
