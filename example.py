# Factorial calculation
# fact = 1
# num = int(input("Enter a number : "))
# if num < 0:
#     print("Factorial of -ve interger isn't possible.")
# elif num == 0:
#     print("The factorial of 0 is: 1")
# else:
#     for i in range(1, num+1):
#         fact = fact*i
#     print("The factorial of ", num, " is: ", fact)


# Reversing a number
# num1 = int(input("Enter a number : "))
# rev = 0
# while num1 > 0:
#     ldigit = num1 % 10
#     rev = rev*10 + ldigit
#     num1 = num1 // 10

# print("Reverse of ", num1, " is: ", rev)


# Check Palindrome
# num2 = int(input("Enter a number: "))
# temp = num2
# reverse = 0
# while num2 > 0:
#     ldigit = num2 % 10
#     reverse = reverse*10 + ldigit
#     num2 = num2 // 10

# if reverse == temp:
#     print("It is a palidrome.")
# else:
#     print("Not palindrome.")


# Fibonacci Number
# num3 = int(input("Enter a number: "))
# a = 0
# b = 1
# if num3 < 0:
#     print("Incorrect input")
# elif num3 == 0:
#     print(a)
# elif num3 == 1:
#     print(b)
# else:
#     for i in range(2, num3):
#         c = a + b
#         a = b
#         b = c
#     print(b)


# Pattern
# for num in range(10):
#     for i in range(num):
#         print(num, end=" ")
#     print("\n")
