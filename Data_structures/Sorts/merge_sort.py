
def merge(left, right):
    result_line = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_line += [left[i]]
            i += 1
        else:
            result_line += [right[j]]
            j += 1
    
    if j < len(right):
        result_line += right[j::]
    
    if i < len(left):
        result_line += left[i::]

    return result_line


def merge_sort(line_numbers):
    if len(line_numbers) == 1:
        return line_numbers

    n = len(line_numbers) // 2
    left_part = merge_sort(line_numbers[:n])
    right_part = merge_sort(line_numbers[n:])

    return merge(left_part, right_part)

# line = [100, -10, 0, 40, 2]
# print(line)
# print()
# print(merge_sort(line))