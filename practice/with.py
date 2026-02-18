with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

with open("file.txt", "w", encoding="utf-8") as f:
    for i in range(1,11):
        f.write(str(i) + "\n")

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("names.txt", "w", encoding="utf-8") as f:
    f.write("anel\n")
    f.write("sholpan\n")
    f.write("amina\n")

with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip().capitalize())

import csv
data = [
    ['ID', 'Товар', 'Цена'],
    [1, 'Клавиатура', 1500],
]
with open("comp.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

import csv
nums= range(1,11)
with open("comp.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    for num in nums:
        writer.writerow([num])

import csv
names=["anel","samat","aisulu"]
with open("comp.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for name in names:
        writer.writerow([
            name,
            name.capitalize()])

data="""2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT
"""
with open("../lab 2/shop_logs.txt", "w", encoding="utf-8") as f:
    f.write(data)