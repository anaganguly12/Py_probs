f1 = open("file1.txt", 'w')
n = int(input("Number of lines you want to insert: "))

i = 1
while i <= n:
    s = input("Enter the lines: ")
    f1.write(s + '\n')
    i = i + 1

f1.close()

f1 = open('file1.txt', 'r')
count = 0
s1 = input("Input the word: ")
lis = f1.readlines()

for i in lis:
    i.rstrip()
    count += i.count(s1)

print(count)
f1.close()
