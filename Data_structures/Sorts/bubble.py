

def bubble_sort(line_numbers):
    n = len(line_numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if line_numbers[j] > line_numbers[j + 1]:
                line_numbers[j], line_numbers[j + 1] = line_numbers[j + 1], line_numbers[j]

    return line_numbers

