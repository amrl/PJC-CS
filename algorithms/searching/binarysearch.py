# note: array to be searched has to be sorted in non-decreasing order


def binarysearch(array, item):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == item:
            return mid
        elif array[mid] > item:
            end = mid - 1
        else:
            start = mid + 1

    return -1  # not found


def recursive_binarysearch(array, item, start, end):
    if start > end:
        return -1  # not found

    mid = (start + end) // 2
    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return recursive_binarysearch(array, item, start, mid - 1)
    else:
        return recursive_binarysearch(array, item, mid + 1, end)
