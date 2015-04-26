def linearsearch(array, item):
    for index, element in enumerate(array):
        if element == item:
            return index

    return -1  # not found
