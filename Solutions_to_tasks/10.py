from math import pi

class SquareIntoCircle:

    def __init__(self, side):
        self.side = side

    def size(self):
        return 0

    def area(self):
        return pi * self.side**2

class CircleIntoSquare:

    def __init__(self, radius):
        self.radius = radius

    def size(self):
        return 0

    def area(self):
        return pi * self.radius ** 2

sq = SquareIntoCircle(1)
print(sq.size(), sq.area(), sep='\n')
print()
circle = CircleIntoSquare(sq.size())
print(circle.size(), circle.area(), sep='\n')


