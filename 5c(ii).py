n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(0, n-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")

    print("")
