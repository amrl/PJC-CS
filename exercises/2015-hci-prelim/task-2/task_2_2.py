def decToBin(decNumber):
    binStack = list()

    while decNumber != 0:
        if decNumber % 2 == 0:
            binStack.append('0')
        else:
            binStack.append('1')
        decNumber //= 2

    binNumber = ""
    while len(binStack) > 0:
        binNumber += binStack.pop()

    return binNumber
