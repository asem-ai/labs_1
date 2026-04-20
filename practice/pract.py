check=lambda x: "положительное" if x>0 else("отрицательное" if x<0 else "ноль")
print(check(10))

words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words=sorted(words,key=lambda w: (len(w),w[0]))
print(sorted_words)



numbers = [5, 12, 7, 20, 33, 8]
filtered_word= filter(lambda x: x%2==0 and x>10, numbers)
print(list(filtered_word))

numbers = [1, 2, 3, 4, 5, 6]
mapped=map(lambda x: x**2 if x%2==0 else x*3,numbers)
print(list(mapped))

a=int(input("enter number:"))
b=int(input("enter number:"))
check=lambda a,b: "a больше" if a>b else("b больше" if b>a else "равны")
print(check(a,b))

def even_numbers(n):
    for i in range(2, n + 1, 2):
        if i % 4 == 0:
            yield "кратно 4"
        else:
            yield i
for x in even_numbers(10):
    print(x)

def infinite_numbers():
    i=1
    while True:
        if i%3==0:
            yield "Fizz"
        if i%5==0:
            yield "Buzz"
        if i%3==0 and i%5==0:
            yield "FizzBuzz"
        else:
            yield i
        i+=1

