from math import pi


class Square:

    def __init__(self, side):
        self.square = side ** 2

    def extrude(self, h):
        return self.square * h


class Rectangle:

    def __init__(self, a, b):
        self.square = a * b

    def extrude(self, h):
        return self.square * h


class Triangle:

    def __init__(self, side):
        p = (side * 3) / 2
        self.square = (p * (p - side) * (p - side) * (p - side)) ** 0.5

    def extrude(self, h):
        return self.square * h


class Circle:

    def __init__(self, r):
        self.square = pi * r ** 2

    def extrude(self, h):
        return self.square * h


sq = Square(1)
rec = Rectangle(1, 2)
tr = Triangle(1)
cir = Circle(1)
for item in (sq, rec, tr, cir):
    print(item.extrude(1))
