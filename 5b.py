import math as m

print("Special numbers within range 100 to 999: ")

for i in range(100, 1000):
    sum = 0
    j = i
    while j > 0:
        rem = j % 10
        fact = m.factorial(rem)
        sum += fact
        j = j//10

    if i == sum:
        print(i, end=" ")
