
# OOP training 

class Point:

    def __init__(self, x_co, y_co):
        self.x = x_co
        self.y = y_co

    def move(self, new_co_x, new_co_y):
        self.x += new_co_x
        self.y += new_co_y

    def length(self, point):
        x_f, y_f = point.x, point.y
        x_s, y_s = self.x, self.y

        to_comp_x = [x_s, x_f]
        to_comp_x.sort()
        to_comp_y = [y_s, y_f]
        to_comp_y.sort()


        if (x_f > 0 and x_s > 0) or (x_f < 0 and x_s < 0):
            if (y_f > 0 and y_s > 0) or (y_f < 0 and y_s < 0):
                result = round(((abs(x_f) - abs(x_s))**2 + (abs(y_f) - abs(y_s))**2)**0.5, 2)
            else:
                result = round(((abs(x_f) - abs(x_s))**2 + (abs(y_f) + abs(y_s))**2)**0.5, 2)
        else:
            if (y_f > 0 and y_s > 0) or (y_f < 0 and y_s < 0):
                result = round(((abs(x_f) + abs(x_s))**2 + (abs(y_f) - abs(y_s))**2)**0.5, 2)
            else:
                result = round(((abs(x_f) + abs(x_s))**2 + (abs(y_f) + abs(y_s))**2)**0.5, 2)

        return result
    
class RedButton:

    def __init__(self):
        self.__counter = 0

    def click(self):
        print('Тревога')
        self.__counter += 1

    def count(self):
        return self.__counter 

