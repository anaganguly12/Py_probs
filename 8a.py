s1 = input("Enter the string: ")
d1 = {}

s2 = s1.split()
for word in s2:
    if word in d1:
        d1[word] += 1
    else:
        d1[word] = 1

print(d1)
