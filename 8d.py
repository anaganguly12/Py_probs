def towerofHanoi(n, A, B, C):
    if n > 0:
        towerofHanoi(n-1, A, C, B)
        print("\nMove a Disk from", A, "To", C)
        towerofHanoi(n-1, B, A, C)


n = int(input("Enter the number of disks: "))
towerofHanoi(n, 'A', 'B', 'C')
