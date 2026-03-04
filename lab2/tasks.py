f=open("shop_logs.txt","r", encoding="utf-8")
unique_users = set()
total_buys = 0
total_sum = 0
user_spending = {}
for line in f:
    parts=line.strip().split(";")
    user_id=parts[1]
    action=parts[2]
    unique_users.add(user_id)
    if action=="BUY":
        amount=int(parts[3])
        total_buys+=1
        total_sum+=amount
        if user_id not in user_spending:
            user_spending[user_id]=amount
        else:
            user_spending[user_id]+=amount
max_user=""
max_spent=0
for user in user_spending:
    if user_spending[user] > max_spent:
        max_user=user
        max_spent=user_spending[user]
if total_buys>0:
    average_check=total_sum/total_buys
else:
    average_check=0
report=open("report.txt","w", encoding="utf-8")
report.write("Уникальных пользователей: " + str(len(unique_users)) + "\n")
report.write("Всего покупок: " + str(total_buys) + "\n")
report.write("Общая сумма: " + str(total_sum) + "\n")
report.write("Самый активный покупатель: " + max_user + "\n")
report.write("Средний чек: " + str(average_check) + "\n")
report.close()
print("Отчет успешно создан!")

import csv #2
file = open("employees.csv", "w", encoding="utf-8")
file.write("name,department,salary\n")
file.write("Ali,IT,500000\n")
file.write("Dana,HR,300000\n")
file.write("Arman,IT,600000\n")
file.write("Aruzhan,Marketing,400000\n")
file.write("Dias,IT,450000\n")
file.close()

names = []
departments = []
salaries = []

file = open("employees.csv", "r", encoding="utf-8")
reader = csv.DictReader(file)

for row in reader:
    names.append(row["name"])
    departments.append(row["department"])
    salaries.append(int(row["salary"]))

file.close()

total = 0
for s in salaries:
    total += s

average = total / len(salaries)

dept_salaries = {}

for i in range(len(departments)):
    dept = departments[i]
    salary = salaries[i]

    if dept not in dept_salaries:
        dept_salaries[dept] = []

    dept_salaries[dept].append(salary)

dept_average = {}
for dept, salary_list in dept_salaries.items():
    total = 0
    for s in salary_list:
        total += s
    avg = total / len(salary_list)
    dept_average[dept] = avg

best_dept = ""
highest_avg = 0
for dept, avg in dept_average.items():
    if avg > highest_avg:
        highest_avg = avg
        best_dept = dept

max_salary = 0
max_name = ""
for i in range(len(salaries)):
    if salaries[i] > max_salary:
        max_salary = salaries[i]
        max_name = names[i]

high_employees = []
for i in range(len(salaries)):
    if salaries[i] > average:
        high_employees.append([names[i], departments[i], salaries[i]])


file2 = open("high_salary.csv", "w", encoding="utf-8")
file2.write("name,department,salary\n")
for emp in high_employees:
    file2.write(f"{emp[0]},{emp[1]},{emp[2]}\n")
file2.close()

import json  #3
with open("orders.json", "r", encoding="utf-8") as f:
    orders = json.load(f)

total_revenue = 0
user_order_count = {}
item_counts = {}

most_expensive_order = max(orders, key=lambda x: x["total"])

for order in orders:
    user = order["user"]
    total = order["total"]
    items = order["items"]
    total_revenue += total
    if user not in user_order_count:
        user_order_count[user] = 0
    user_order_count[user] += 1
    for item in items:
        if item not in item_counts:
            item_counts[item] = 0
        item_counts[item] += 1

top_user = most_expensive_order["user"]

most_popular_item = max(item_counts, key=item_counts.get)

summary = {
    "total_revenue": total_revenue,
    "top_user": top_user,
    "most_popular_item": most_popular_item,
    "total_orders": len(orders)
}

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=4)

print("Общая сумма:", total_revenue)
print("Заказы по пользователям:", user_order_count)
print("Всего товаров продано:", sum(item_counts.values()))
print("Пользователь с самым дорогим заказом:", top_user)
print("Самый популярный товар:", most_popular_item)

import csv   #4
import json

suspicious_transactions = []
user_operations = {}
suspicious_users = set()
suspicious_total = 0
with open("transactions.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        user = row["user_id"]
        amount = int(row["amount"])

        if user not in user_operations:
            user_operations[user] = 0
        user_operations[user] += 1

        if amount > 500000:
            suspicious_transactions.append(row)
            suspicious_users.add(user)
            suspicious_total += amount
for user, count in user_operations.items():
    if count > 3:
        suspicious_users.add(user)
with open("fraud_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write(f"Список пользователей: {', '.join(suspicious_users)}\n")
    f.write(f"Общая сумма подозрительных операций: {suspicious_total}\n")

with open("fraud_users.json", "w", encoding="utf-8") as f:
    json.dump(list(suspicious_users), f, indent=4)

print("Подозрительные транзакции:", suspicious_transactions)
print("Подозрительные пользователи:", suspicious_users)
print("Общая сумма подозрительных операций:", suspicious_total)