#1
check= lambda x: "положительное" if x>0 else "ноль" if x == 0 else "отрицательное"
print(check(10))
print(check(-10))
print(check(0))