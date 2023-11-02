

def merge_sort(line, start, end):

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(line, start, mid)
        merge_sort(line, mid, end)
        merge_list(line, start, mid, end)

def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

line = [100, 13, 8, 0, 21, 19, 123]
merge_sort(line, 0, len(line))
print('Sorted list: ', end='')
print(line)