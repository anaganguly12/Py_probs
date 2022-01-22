basic = eval(input("Enter the basic pay of the employee: "))
agp = basic*0.5
merged = basic + agp
da = merged*0.5
hra = merged*0.15
total = agp + da + hra

print("Total salary of the employee is: {0:.2f}".format(total))
