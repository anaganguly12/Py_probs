class PowerSet():
    def __init__(self, x):
        if type(x) == set:
            self.x = x
        else:
            print("It's not a set.")

    def __add__(self, o):
        print("1st set: ", self.x)
        print("2nd set: ", o.x)
        print("Union: ", self.x.union(o.x))

    def __mul__(self, o):
        print("1st set: ", self.x)
        print("2nd set: ", o.x)
        print("Intersection: ", self.x.intersection(o.x))

    def __sub__(self, o):
        print("1st set: ", self.x)
        print("2nd set: ", o.x)
        print("Difference: ", self.x.difference(o.x))
