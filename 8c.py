class HighRotation(Exception):
    pass


def rotatelist(l1, r=1, d="Left"):
    l2 = []
    try:
        if r > len(l1):
            raise HighRotation
        if d == "Right":
            l2 = l1[(len(l1) - r):len(l1)] + l1[0:(len(l1) - r)]
        if d == "Left":
            l2 = l1[r:len(l1)] + l1[0:r]
        return l2
    except HighRotation:
        print("Not Possible")
        return l1


l1 = [1, 2, 3, 4, 5]
l5 = rotatelist(l1, 3, "Right")
print(l5)
