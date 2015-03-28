def linearsearch(array, item):
    for index in range(len(array)):
        if array[index] == item:
            return index

    return -1  # not found
