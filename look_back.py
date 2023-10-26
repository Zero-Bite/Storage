
def merge(f_tuple, s_tuple):
    line1 = [x for x in f_tuple]
    line2 = [x for x in s_tuple]
    line = line1 + line2

    # вот он bubble-sort
    for i in range(len(line) - 1):
        for j in range(len(line) - 1 - i):
            if line[j] > line[j + 1]:
                line[j], line[j + 1] = line[j + 1], line[j]

    return tuple(line)