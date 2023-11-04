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
                    maxim_value = abs(element)
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


data = [[0, 0, 1, 2],
        [3, 1, -1, -1],
        [0, 3, -1, 0]]
jw = JamesWebb(data)
print(jw.brightest_star())
print(jw.brightest_galaxy())
print(jw.stars())
print(jw.galaxies())
print(jw.voids())
