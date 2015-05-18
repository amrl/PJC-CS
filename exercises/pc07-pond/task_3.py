from random import randint


fish_coords = set()          # a set can only contain unique values
while len(fish_coords) < 3:  # stop only when obtained 3 different coordinates
    X = randint(0, 14)
    Y = randint(0, 7)

    fish_coords.add((X, Y))  # only adds to set when (X, Y) is not in the set

pond = [['.' for i in range(15)] for i in range(8)]

# coord => (X, Y)
for coord in fish_coords:
    pond[coord[1]][coord[0]] = 'F'  # pond[column][row]
    # coord[1] => Y
    # coord[0] => X

for row in pond:
    print(''.join(row))
