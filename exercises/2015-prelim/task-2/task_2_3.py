test_array = [435, 646, 344, 54, 23, 98, 789, 212, 847, 201, 733]
test_array2 = [999, 854, 643, 321, 289, 111, 95, 47, 12, 0]


def Quicksort(ThisArray, First, Last):
    ThisArray[-1] = ThisArray[-1] + 1  # increment function call count

    Low = First
    High = Last
    Pivot = ThisArray[Low]

    while Low <= High:
        while ThisArray[Low] < Pivot:
            Low += 1
        while ThisArray[High] > Pivot:
            High -= 1
        if Low <= High:
            ThisArray[Low], ThisArray[High] = ThisArray[High], ThisArray[Low]
            Low += 1
            High -= 1

    if First < High:
        Quicksort(ThisArray, First, High)
    if Low < Last:
        Quicksort(ThisArray, Low, Last)


def InitialiseList(array):
    print("Before:")
    print(array)

    array.append(0)  # add counter to back of list
    Quicksort(array, 0, len(array)-2)  # original list is at 0 to n-2

    print("\nAfter:")
    print(array[:-1])

    function_calls = array[-1]
    print("\nFunction calls:", function_calls)
