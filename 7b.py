s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

l1 = s1.split()
l2 = s2.split()

set1 = set(l1)
set2 = set(l2)

ans = set1.intersection(set2)
print(' '.join(ans))
