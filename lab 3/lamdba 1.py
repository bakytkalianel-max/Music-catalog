#1
check= lambda x: "положительное" if x>0 else "ноль" if x == 0 else "отрицательное"
print(check(10))
print(check(-10))
print(check(0))

#2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda w: (len(w),w))
print(sorted_words)

#3
numbers = [5, 12, 7, 20, 33, 8]
filter_numbers = list(filter(lambda n: n>10 and n%2==0, numbers))
print(filter_numbers)