lis = []

n = int(input("Enter the number of elements: "))

print("Enter the elements: ")
for i in range(0, n):
    j = int(input())
    lis.append(j)

print("Before removing elements: ", lis)

ans = []
for i in lis:
    if i not in ans:
        ans.append(i)

print("After removing duplicates: ", ans)
