test_array = [435, 646, 344, 54, 23, 98, 789, 212, 847, 201, 733]


def Quicksort(ThisArray, First, Last):
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

    Quicksort(array, 0, len(array)-1)

    print("\nAfter:")
    print(array)
