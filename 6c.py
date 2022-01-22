import numpy as np

n = int(input("Enter the number of rows of 1st matrix: "))
m = int(input("Enter the number of columns of 1st matrix: "))

mat1 = np.zeros([n, m])

x = int(input("Enter the number of rows of 2nd matrix: "))
y = int(input("Enter the number of columns of 2nd matrix: "))

mat2 = np.zeros([x, y])

if x == m:
    print("Enter the value of 1st matrix: ")
    for i in range(0, n):
        print('Enter ', m, 'integer for {}-row'.format(i))
        for j in range(0, m):
            mat1[i][j] = int(input())
    print("Enter the value of 2nd matrix: ")
    for i in range(0, x):
        print('Enter ', y, 'integer for {}-row'.format(i))
        for j in range(0, y):
            mat2[i][j] = int(input())

    res = mat1 @ mat2
    print(res)

else:
    print("Multiplication of this matrices isn't possible.")
