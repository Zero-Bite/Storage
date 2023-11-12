


def qucik_sort(line):

    if len(line) <= 1:
        return line

    n = line[len(line) // 2]

    left = list(filter(lambda x: x < n, line))
    center = list(filter(lambda x: x == n, line))
    right = list(filter(lambda x: x > n, line))

    return qucik_sort(left) + center + qucik_sort(right)

line = [-100, 1, -102, 30, 888, 32, 900, 0]
print(line)
print(qucik_sort(line))

