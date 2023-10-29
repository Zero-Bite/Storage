import random

# медленно, слишком медленно

def bubble_sort(array):

    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
    return array

tmp_line = "2 14 15 21 24 28 30 35 36 42 50 54 55 58 59 74 77 79 91 95"
line = [int(x) for x in tmp_line.split()]
random.shuffle(line)

print(line)

result = bubble_sort(line)
print(f"New sequence: {result}")