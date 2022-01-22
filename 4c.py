num = int(input("Enter a number: "))
copynum = num
rev = 0
while num > 0:
    lastdigit = num % 10
    rev = rev*10 + lastdigit
    num = num // 10

print("Reversed number is: ", rev)
if copynum == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
