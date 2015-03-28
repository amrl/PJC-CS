def bubblesort(array):
    for loop in range(len(array) - 1):  # at most n-1 passes required
        for index in range(len(array) - 1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]


def efficient_bubblesort(array):
    isSorted = False

    for loop in range(len(array) - 1):
        if isSorted is True:
            break

        isSorted = True
        for index in range(len(array) - loop - 1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                isSorted = False
