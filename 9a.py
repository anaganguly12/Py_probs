class Circle():
    def __init__(self, rad=None):
        if rad is None:
            self.radius = eval(input("Enter the radius: "))
        else:
            self.radius = rad

    def get_radius(self):
        return self.radius

    def calc_area(self):
        return 3.14*self.radius**2

    def __del__(self):
        print("Operator has been destructed.")


class Cylinder(Circle):
    def __init__(self, h=None, rad=None):
        if h is None:
            self.height = eval(input("Enter the height: "))
        else:
            self.height = h
        if rad is None:
            super().__init__()
        else:
            super().__init__(rad)
        print("A cylinder has been created.")

    def calc_area(self):
        return 2*3.14*self.radius*(self.height+self.radius)
