n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n-i):
        print(chr(j+65), end="")
    print(i*" ", end="")
    print("", end="")

    for k in range(j, -1, -1):
        print(chr(k+65), end="")
    print(" ")
