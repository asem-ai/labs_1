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