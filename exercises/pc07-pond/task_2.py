def val_x(X):
    if int(X) >= 1 and int(X) <= 15:
        return True
    else:
        return False


def val_y(Y):
    if int(Y) >= 1 and int(Y) <= 8:
        return True
    else:
        return False


def throw():
    pond = [['.' for i in range(15)] for i in range(8)]
    # 2D array
    # 8 smaller lists (rows) in one main list
    # each smaller list contains 15 '.'s
    # i.e. pond = [['.', '.', ...], ['.', '.', ...], ['.', '.', ...], ...]

    while True:  # get X-coordinate to throw to
        X = input("X coordinate <1 to 15>? ")
        if val_x(X):
            break
        else:
            print("\n- Invalid X value -\n")

    while True:  # get Y-coordinate to throw to
        Y = input("Y coordinate <1 to 8>? ")
        if val_y(Y):
            break
        else:
            print("\n- Invalid Y value -\n")

    X, Y = int(X)-1, int(Y)-1  # -1 to accomodate indices starting from 0
    pond[Y][X] = 'S'           # pond[column][row]

    print()
    for row in pond:  # display pond to console
        print(''.join(row))


# throw()
