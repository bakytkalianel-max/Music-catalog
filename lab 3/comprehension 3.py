#1
even=[x**2 for x in range(1,21) if x%2==0]
print(even)

#2
import math
matrix = [[1,2,3], [4,5,6], [7,8,9]]
a=[(lambda row: math.prod(row))(row) for row in matrix]
print(a)