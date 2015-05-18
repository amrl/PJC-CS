from task_2 import val_x, val_y
from random import randint


def feed():
    fish_coord = set()

    while len(fish_coord) < 3:
        X = randint(0, 14)
        Y = randint(0, 7)

        fish_coord.add((X, Y))

    pond = [['.' for i in range(15)] for i in range(8)]

    for coord in fish_coord:
        pond[coord[1]][coord[0]] = 'F'

    while True:
        X = input("X coordinate <1 to 15>? ")
        if val_x(X):
            break
        else:
            print("\n- Invalid X value -\n")

    while True:
        Y = input("Y coordinate <1 to 8>? ")
        if val_y(Y):
            break
        else:
            print("\n- Invalid Y value -\n")

    X, Y = int(X)-1, int(Y)-1

    if pond[Y][X] == 'F':  # coordinates chosen has a fish in it
        pond[Y][X] = 'H'   # HAPPY FISH !!!
    else:
        pond[Y][X] = 'P'   # pellet just floats there...

    print()
    for row in pond:
        print(''.join(row))

feed()
