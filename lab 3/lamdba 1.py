#1
check= lambda x: "положительное" if x>0 else "ноль" if x == 0 else "отрицательное"
print(check(10))
print(check(-10))
print(check(0))

#2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda w: (len(w),w))
print(sorted_words)