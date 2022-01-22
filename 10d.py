f2 = open('test1.txt', 'r')
l = f2.readlines()
for i in l:
    print(i)
l1 = l[0].split()
for i in l1:
    print(i)
f2.close()
