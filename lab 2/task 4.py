import csv
import json

transaction=[]
user_counts={}

with open("transactions.csv","r", encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        user_id=row["user_id"].strip()
        amount=int(row["amount"])

        transaction.append({"user_id":user_id,"amount":amount})
        user_counts[user_id]=user_counts.get(user_id,0)+1
suspicious_transactions=[t for t in transaction if t["amount"]>500000]
suspicious_users=sorted([u for u, cnt in user_counts.items() if cnt>3])
total_suspicious_amount=sum(t["amount"] for t in suspicious_transactions)
all_users = sorted(user_counts.keys())

with open("fraud_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write("Список пользователей: " + ", ".join(all_users) + "\n")
    f.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")

with open("fraud_users.json", "w", encoding="utf-8") as f:
    json.dump(suspicious_users, f, ensure_ascii=False, indent=4)