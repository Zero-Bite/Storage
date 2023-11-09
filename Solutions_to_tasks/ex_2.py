# № по порядку, магическая вещь, размер, вес

class Magician:

    def __init__(self, name_of_source):
        self.name = name_of_source

    def add_thing(self, to_add: tuple):

        to_paste = ''
        for item in open(self.name).readlines():
            tmp = item.strip().split()

            number = int(tmp[0]) + 1
            tmp_to_add = str(to_add)
            to_paste = str(number) + tmp_to_add

        # with open(self.name, '+') as file:
        #     file.write(to_paste)

        with open(self.name, 'r+') as f:
            f.seek(0, 2)
            f.write(to_paste)

    def get_all(self):
        names = set()

        for item in open(self.name).readlines():
            tmp = item.strip().split()
            names.add(tmp[1])

        # with open(self.name, 'r', encoding='utf-8') as file:
        #     for item in file.readline():
        #         print(item)
        #         names += [item.split('  ')[1]]
        # names = sorted(names)

        return sorted(names)

    def get_thing(self, name):
        data = []
        for item in open(self.name).readlines():
            tmp = item.strip().split()
            if tmp[1] == name:
                res = tmp[2], tmp[3]
                data += [res]

        data = sorted(data)

        return data

    def min_size(self):
        # находим минимум -> потом сортируем по алфавиту

        sizes = []
        mini = float('inf')
        res = []

        for item in open(self.name).readlines():
            tmp = item.strip().split()

            size = int(tmp[2])
            sizes += [[tmp[1], size]]
            mini = min(mini, size)

        for element in sizes:
            if element[1] == mini:
                res += [element[0]]
            else:
                pass

        res = sorted(set(res))

        return res


#

mgc = Magician('/Users/anastasia/Desktop/Pytuhon/Parse/step_by_step/parser/Solutions_to_tasks/things1.txt')
print('Magic things:', *mgc.get_all())
print('Things of min size:')
print(*mgc.min_size(), sep='\n')
print()
mgc.add_thing(('crown', 49, 213))
print('Magic crowns:')
print(*mgc.get_thing('crown'), sep='\n')
