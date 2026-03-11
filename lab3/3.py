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