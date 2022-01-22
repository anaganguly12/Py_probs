start = int(input("Enter start : "))
end = int(input("Enter end : "))

print("Automorphic numbers are: ")
for i in range(start, end+1):
    square = i**2
    rem = square % 100
    if i == rem:
        print(i, end=" ")
