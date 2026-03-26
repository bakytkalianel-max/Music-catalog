#2.1
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorteed_w=sorted(words, key=lambda w: (len(w), w))
print(sorteed_w)

#3.1
numbers = [5, 12, 7, 20, 33, 8]
result=list(filter(lambda x: x>10 and x%2==0,numbers))
print(result)

#2.2
def filter_words(words):
    for w in words:
        if len(w)>4:
            if "а" in w:
                yield "c a"
            else:
                yield w
words = ["кот", "машина", "арбуз", "дом","любовь"]
for w in filter_words(words):
    print(w)

#3.2
import math
matrix = [[1,2,3], [4,5,6], [7,8,9]]
a=[(lambda row:math.prod(row)) (row) for row in matrix]
print(a)

#4.2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
result=[(lambda w:
            (w.upper() if len(w)>4 else "short") + ("*" if "а" in w else ""))
            (w)for w in words
       ]
print(result)

#5.2
words=["anel","safe","book","python","dog"]
result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
print(result)