#1 esep
check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
print(check(5))
print(check(-3))
print(check(0))

#2 esep
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda w: (len(w), w[0]))
print(sorted_words)

#3 esep
numbers = [5, 12, 7, 20, 33, 8]
filtered = list(filter(lambda x: x > 10 and x % 2 == 0, numbers))
print(filtered)

#4 esep
numbers = [1, 2, 3, 4, 5, 6]
mapped = list(map(lambda x: x**2 if x % 2 == 0 else x * 3, numbers))
print(mapped)

#5 esep
compare = lambda a, b: "a больше" if a > b else ("b больше" if b > a else "равны")
print(compare(10, 7))
print(compare(3, 5))
print(compare(4, 4))

#6 esep
numbers = [0, -3, 5, -7, 8]
check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
result = [check(num) for num in numbers]
print(result)

#1 esep
def even_numbers(n):
    for i in range(2, n + 1, 2):
        if i % 4 == 0:
            yield "кратно 4"
        else:
            yield i
for x in even_numbers(10):
    print(x)

#2 esep
def filter_words(words):
    for w in words:
        if len(w) > 4:
            if 'а' in w:
                yield "с а"
            else:
                yield w
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)

#3 esep
def infinite_numbers():
    num = 1
    while True:
        if num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        elif num % 3 == 0:
            yield "Fizz"
        elif num % 5 == 0:
            yield "Buzz"
        else:
            yield num
        num += 1
gen = infinite_numbers()
for _ in range(15):
    print(next(gen))

#4 esep
def squares(n):
    for i in range(1, n + 1):
        sq = i ** 2
        if sq % 2 == 0:
            yield "чётный квадрат"
        else:
            yield sq
for x in squares(5):
    print(x)


#1 esep
result = [x**2 for x in range(1, 21) if x % 2 == 0]
print(result)

#2 esep
from functools import reduce
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result = [reduce(lambda a, b: a * b, row) for row in matrix]
print(result)

#3 esep
words = ["кот", "машина", "ананас", "дом"]
filtered = [w for w in words if len(w) > 4 and 'а' not in w]
print(filtered)

#4 esep
numbers = [1, 2, 3, 4, 5]
result = {x: ("чётное" if x % 2 == 0 else "нечётное") for x in numbers}
print(result)

#5 esep
matrix = [[1,2], [3,4], [5,6]]
flat = [num for row in matrix for num in row]
print(flat)

#6 esep
result = [
    "FizzBuzz" if x % 3 == 0 and x % 5 == 0
    else "Fizz" if x % 3 == 0
    else "Buzz" if x % 5 == 0
    else x
    for x in range(1, 21)
]
print(result)

#1 esep
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def special_numbers(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
for x in special_numbers(15):
    print(x)

#2 esep
words = ["кот", "машина", "арбуз", "дом", "ананас"]
result = [
    (lambda w:
        w.upper() + "*" if len(w) > 4 and 'а' in w else
        "short" if len(w) <= 4 else
        w.upper()
    )(word)
    for word in words
]
print(result)