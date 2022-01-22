n = eval(input("Enter a Integer: "))
f1 = open('test1.txt', 'w')

for i in range(2, n):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        f1.write(str(i)+" ")
f1.close()
