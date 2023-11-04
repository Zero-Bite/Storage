# в data -> двумерный массив ()

class JamesWebb:

    def __init__(self, data):
        self.data = data

    def brightest_star(self) -> tuple:
        maxim_value = float('-inf')
        coor = ()
        for index in range(len(self.data)):
            for element in range(len(self.data[index])):
                if self.data[index][element] < 0 and abs(self.data[index][element]) > maxim_value:
                    maxim_value = abs(self.data[index][element])
                    coor = (index, element)

        return coor

    def brightest_galaxy(self) -> tuple:
        minimum = float('-inf')
        coor = ()
        for index in range(len(self.data)):
            for element in range(len(self.data[index])):
                if self.data[index][element] > 0 and abs(self.data[index][element]) > minimum:
                    minimum = abs(self.data[index][element])
                    coor = (index, element)

        return coor

    def stars(self) -> int:
        counter = 0
        for item in self.data:
            for element in item:
                if element < 0:
                    counter += 1

        return counter

    def galaxies(self) -> int:
        counter = 0
        for item in self.data:
            for element in item:
                if element > 0:
                    counter += 1

        return counter

    def voids(self) -> int:
        counter = 0
        for item in self.data:
            for element in item:
                if element == 0:
                    counter += 1

        return counter


data = [[4, -3, 6, -8, -7, -2, -1],
        [-5, 5, 4, 0, -8, 7, -6],
        [-5, 5, 1, 1, -2, -7, -1],
        [-6, 6, -1, -2, 3, 9, 1],
        [4, 3, -9, -5, -7, 0, -1],
        [0, 6, -9, -5, 0, -1, -5]]


jw = JamesWebb(data)
print(jw.stars())
print(jw.brightest_star())
print(jw.galaxies())

# 23
# (4, 2)
# (5, 6) - my response
# 15