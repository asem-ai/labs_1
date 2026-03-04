
f=open("shop_logs.txt","r",encoding="utf-8")
unique_users=set()
total_buys=0
total_sum=0
user_spending={}
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
    if user_spending[user]>max_spent:
        max_user=user
        max_spent=user_spending[user]
if total_buys>0:
    average_check=total_sum/total_buys
else:
    average_check=0
report=open("report.txt","w", encoding="utf-8")
report.write("Уникальных пользывателей: " +str(len(unique_users))+"\n")
report.write("Всего покупок: " +str(total_buys)+"\n")
report.write("Общая сумма: " + str(total_sum)+"\n")
report.write("Самый активный покупатель :" +max_user+"\n")
report.write("Средний чек: " +str(average_check) + "\n")
report.close()
print("Отчет прошел отлично")
