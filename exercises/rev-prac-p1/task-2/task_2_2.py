# initialise array
X = ['' for i in range(20)]
X[0] = 999
X[1] = 850
X[2] = 812
X[3] = 770
X[4] = 733
X[5] = 634
X[6] = 511
X[7] = 508
X[8] = 500
X[9] = 497
X[10] = 413
X[11] = 406
X[12] = 389
X[13] = 310
X[14] = 292
X[15] = 251
X[16] = 107
X[17] = 88
X[18] = 53
X[19] = 13


def quicksort(array, start, end):
    if start < end:
        p_index = partition(array, start, end)
        quicksort(array, start, p_index-1)
        quicksort(array, p_index+1, end)


def partition(array, start, end):
    pivot = array[end]
    p_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[p_index] = array[p_index], array[i]
            p_index += 1
    array[p_index], array[end] = array[end], array[p_index]
    return p_index


# quicksort(X, 0, len(X)-1)
# print(X)
