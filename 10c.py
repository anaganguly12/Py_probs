f2 = open('test2.txt', 'w')

x = 0
y = 1
n = int(input("Numbers of Fibonacci numbers you want: "))
f2.write("0"+" ")
f2.write("1"+" ")
for i in range(n - 2):
    some = x+y
    x = y
    y = some
    f2.write(str(some)+" ")
f2.close()
