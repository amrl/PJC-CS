# Task 3

from random import randint


fish_coord = set()
while len(fish_coord) < 3:
    X = randint(0, 15)
    Y = randint(0, 8)

    fish_coord.add((X, Y))

pond = [['.' for i in range(15)] for i in range(8)]
for coord in fish_coord:
    pond[coord[1]][coord[0]] = 'F'

for row in pond:
    print(''.join(row))
