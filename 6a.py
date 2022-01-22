# for 1D list
# l = []
# n = int(input("Enter the number of elements: "))
# print("Enter the elements of the list: ")
# for i in range(0, n):
#     j = int(input())
#     l.append(j)

# print("Largest element: ", max(l))
# print("Smallest element: ", min(l))

# for 2D list

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of column: "))
lis = []

print("Enter the elements: ")
for i in range(row):
    a = []
    for j in range(col):
        k = int(input())
        a.append(k)
    lis.append(a)

max1 = []
min1 = []

for i in lis:
    max1 = max1 + [max(i)]
    min1 = min1 + [min(i)]

print("Largest element: ", max(max1))
print("Smallest element: ", min(min1))
