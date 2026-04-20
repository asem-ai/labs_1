#4
numbers = [1, 2, 3, 4, 5, 6]
mapped=map(lambda x: x**2 if x%2==0 else x*3,numbers)
print(list(mapped))

#2
def filter_words(words):
    filtered_words=[]
    for word in words:
        if len(word) > 4:
            yield word
            if 'a' in word:
                yield "c a"
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)



#2 esep
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda w: (len(w), w[0]))
print(sorted_words)


#6 esep
numbers = [0, -3, 5, -7, 8]
check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
result = [check(num) for num in numbers]
print(result)

#4 esep
def squares(n):
    for i in range(1,n):
        if (i**2)%2==0:
            yield "чётный квадрат"
        else:
            yield i**2
for x in squares(5):
    print(x)

#2 esep
from functools import reduce
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result = [reduce(lambda a, b: a * b, row) for row in matrix]
print(result)

#4 esep
numbers = [1,2,3,4,5]