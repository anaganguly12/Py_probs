s1 = input("Enter the sentence: ")

lower = 0
upper = 0

for i in s1:
    if 97 <= ord(i) <= 122:
        lower += 1
    if 65 <= ord(i) <= 90:
        upper += 1

print("The number of uppercase letters are: ", upper)
print("The number of lowercase letters are: ", lower)
