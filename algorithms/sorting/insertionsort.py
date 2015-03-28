def insertionsort(array):
    for index in range(1, len(array)):
        current = array[index]

        while index > 0 and current < array[index-1]:
            array[index] = array[index-1]
            index -= 1

        array[index] = current
