class Square:
    def __init__(self, side=0):
        self.side = side

    def area(self):
        print("Area of Square ", self.side*self.side)


class Rectangle(Square):
    def __init__(self, side=0, width=0):
        super().__init__(side)
        # self.side = side
        self.width = width

    def area(self):
        super().area()
        print("Area of rectangle", self.side * self.width)


if __name__ == '__main__':
    sq = Square(10)
    sq.area()

    rect = Rectangle(12, 14)
    rect.area()
