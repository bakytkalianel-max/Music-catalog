#1
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def special_numbers(n):
    for i in range(1, n+1):
        if i % 3 ==0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif is_prime(i):
            yield "Простое"
        else:
            yield i

for x in special_numbers(15):
    print(x)

#2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
result=[
    (lambda w:
        (w.upper() if len(w) > 4 else "short") + ("*" if "а" in w else "")
    )(w)
    for w in words
]
print(result)

#3
def process_numbers(numbers):
    a=[x for x in numbers]
    filt=filter(lambda x: x >= 0, a)
    mapp=map(lambda x: x/2 if x % 2 == 0 else x*3+1, filt)
    for num  in mapp:
        yield num
numbers = [5, -2, 8, 0, -7, 3]
for x in process_numbers(numbers):
    print(x)

#4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
result={
    name:(lambda x: "Отлично" if x >= 90 else "Хорошо" if x>=70 else "Удовлетворительно")(grade)
    for name, grade in students
}
print(result)

#5
def matrix_transform(matrix):
    for row in matrix:
        for x in row:
            if x % 2 == 0 and x % 3 == 0:
                yield "Кратно 6"
            elif x % 2 == 0:
                yield "четное"
            elif x % 3 == 0:
                yield "кратно 3"
            else:
                yield x
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
for x in matrix_transform(matrix):
    print(x)
