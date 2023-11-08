class ChairLeg:

    def __init__(self, length):
        self.length = length

    def __mul__(self, other):
        if isinstance(other, ChairLeg):
            self.length = (self.length * other.length)
        else:
            self.length = (other * self.length)

    def __rmul__(self, other):
        if isinstance(other, ChairLeg):
            self.length = (self.length * other.length)
        else:
            self.length = (other * self.length)

    def __floordiv__(self, other):
        self.length = self.length // other
        return self.length

    def __mod__(self, other):
        return self.length % other


chl = ChairLeg(15)
chl // 4
print(chl.length)
2 * chl
print(chl.length)
3 * chl
print(chl % 7)
