#1
def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            if i % 4 == 0:
                yield "кратно 4"
            else:
                yield i
for x in even_numbers(14):
    print(x)

#2
def filter_words(words):
    for w in words:
        if len(w) > 4:
            if "а" in w:
                yield "c a"
            else:
                yield w
words = ["кот", "машина", "арбуз", "дом","цветы"]
for w in filter_words(words):
    print(w)
