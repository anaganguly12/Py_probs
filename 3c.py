a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

if a == 0:
    print("It is not a quadratic equation.")

else:
    d = (b*b) - (4*a*c)
    if d < 0:
        d = -1*d
        imaginary = ((d**0.5)/(2*a))
        real = (-b)/(2*a)
        rt1 = complex(real, imaginary)
        print(rt1)
        rt2 = rt1.conjugate()
        print(rt2)
    elif d == 0:
        root = -b/(2*a)
        print("The roots are equal and root is:{0:0.2f}".format(root))
    else:
        root1 = (((-b) + (d**0.5))/(2*a))
        root2 = (((-b) - (d**0.5))/(2*a))
        print("The first root is: {0:0.2f}".format(root1))
        print("The second root is: {0:0.2f}".format(root2))
