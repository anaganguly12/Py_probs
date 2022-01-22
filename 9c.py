class StLine():
    def __init__(self, l=None):
        if l is None:
            self.length = eval(input("Enter the length: "))
        else:
            self.length = l

    def show_len(self):
        print("Length is: ", self.length)

    def __del__(self):
        print("Straight line object destructred.")


class Square(StLine):
    def __init__(self, s=None):
        if s is None:
            super().__init__()
            self.side = self.length
        else:
            self.side = s
        print("A square is created with side ", self.side)

    def calc_area(self):
        return self.side * self.side

    def show_area(self):
        print("Area is: ", self.calc_area())

    def __del__(self):
        print("Square object destructed.")


class Cube(Square):
    def __init__(self, s=None, h=None):
        if s is None:
            super().__init__()
        else:
            super().__init__(s)
        self.edge = self.side
        if h is None:
            self.height = eval(input("Enter the height: "))
        else:
            self.height = h

    def calc_area(self):
        return 6*self.edge*self.height

    def show_cube_area(self):
        print("Area of cube is: ", self.calc_area())

    def __del__(self):
        print("Cube object destructed.")


o1 = Cube(2, 2)
o1.show_cube_area()
