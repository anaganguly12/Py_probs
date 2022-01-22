class SqrArea():
    def cal_area(self, a):
        return a*a

    def __del__(self):
        print("SqrArea object destructed.")


class SqrPeri():
    def cal_per(self, p):
        return 4*p

    def __del__(self):
        print("SqrArea object destructed.")


class Sqr(SqrArea, SqrPeri):
    def __init__(self, s=None):
        if s is None:
            self.side = eval(input("Enter the length of square: "))
        else:
            self.side = s

    def show_area(self):
        print("The area of the Square is: ", super().cal_area(self.side))

    def show_peri(self):
        print("The peripheral of the square is: ", super().cal_per(self.side))
