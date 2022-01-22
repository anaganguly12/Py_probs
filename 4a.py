n = int(input("Enter the number of terms: "))
t0 = 0
t1 = 1
if n == 0:
    print(t0)
elif n == 1:
    print(t1)
else:
    print("Fibonacci series upto n-terms --> ")
    for i in range(0, n):
        print(t0, end=' ')
        t2 = t0 + t1
        t0 = t1
        t1 = t2
