import csv
with open("employees.csv","w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name","department","salary"])
    writer.writerow(["Ali","IT", 500000])
    writer.writerow(["Dana","HR", 300000])
    writer.writerow(["Arman","IT", 600000])
    writer.writerow(["Aruzhan","Marketing", 400000])
    writer.writerow(["Dias","IT", 450000])

employees =[]
total_salary = 0
departments = {}
with open("employees.csv","r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name=row["name"]
        department=row["department"]
        salary=int(row["salary"])

        employees.append(row)
        total_salary+=salary
        if department not in departments:
            departments[department]=[]
        departments[department].append(salary)
avg_salary = total_salary/len(employees)
department_avg={}
for dept in departments:
    department_avg[dept] = sum(departments[dept])/len(departments[dept])
top_department=max(department_avg,key=department_avg.get)
highest_paid= max(employees, key=lambda x: int(x["salary"]))
high_salary_employees=[
    emp for emp in employees if int(emp["salary"])> avg_salary
]
with open("high_salary.csv","w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["name","department","salary"])
    writer.writeheader()
    writer.writerows(high_salary_employees)
