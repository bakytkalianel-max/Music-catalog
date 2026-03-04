#1
even=[x**2 for x in range(1,21) if x%2==0]
print(even)

#2
import math
matrix = [[1,2,3], [4,5,6], [7,8,9]]
a=[(lambda row: math.prod(row))(row) for row in matrix]
print(a)

#3
words = ["кот", "машина", "ананас", "дом", "спрей"]
a=[w for w in words if len(w)>4 and "а" not in w]
print(a)

#4
numbers = [1,2,3,4,5]
a={n: ("четное" if n%2 == 0 else "нечетное") for n in numbers}
print(a)