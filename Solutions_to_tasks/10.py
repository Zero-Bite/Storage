class Student:

    def __init__(self, name, unik, year=1):
        self.name = name
        self.university = unik
        self.year = year

    def get_name(self):
        return self.name

    def get_university(self):
        return self.university

    def get_year(self):
        return self.year

    def study(self):
        if self.year <= 5:
            self.year += 1
        else:
            self.year = 6


class Employee:

    def __init__(self, name, company, position="junior"):
        self.name = name
        self.company = company
        self.position = position

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def work(self):
        if self.position == "junior":
            self.position = "middle"
        elif self.position == "middle":
            self.position = 'senior'
        elif self.position == "senior":
            self.position = "lead"
        else:
            self.position = "lead"

    def get_position(self):
        return self.position


class Human:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# st_1 = Student("Petr", "MSU")
# st_2 = Student("Sonya", "Cambridge")
# h = Human("Shrek")
# empl_1 = Employee("Ivan", "Yandex")
# empl_2 = Employee("Ann", "Gazprom")
# people = [st_1, empl_2, st_2, h, empl_1]
# for person in people:
#     if isinstance(person, Student):
#         print(person.university)
#     elif isinstance(person, Employee):
#         print(person.company)
#     else:
#         print(person.name)
