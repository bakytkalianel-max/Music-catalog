with open("shop_logs.txt", "r", encoding="utf-8") as f:
    lines=f.readlines()
    print(lines)
users=set()
total_purchases=0
total_sum=0
user_spending={}
for line in lines:
    parts=line.strip().split(;)

    data=parts[0]
    user_id=parts[1]
    action=parts[2]
    amount=parts[3]

    users.add(user_id) #Уникальных пользователей
    if action == "BUY":
        amount=int(parts[3])
        total_purchases+=1 #Всего покупок
        total_sum+=amount #Общая сумма

        if user_id in user_spending:
            user_spending[user_id] += amount
        else:
            user_spending[user_id] = amount
if user_spending:
    top_user=max(user_spending,key=user_spending.get) #Самый активный покупатель
else:
    top_user=None
if total_purchases>0:
    avg_check=total_sum/total_purchases #Средний чек6
else:
    avg_check=0
with open("report.txt","w", encoding="utf-8") as f:
    f.write(f"Уникальных пользователей:{len(users)}\n")
    f.write(f"Всего покупок:{total_purchases}\n")
    f.write(f"Общая сумма:{total_sum}\n")
    f.write(f"Самый активный покупатель:{top_user}\n")
    f.write(f"Средний чек:{avg_check}\n")
