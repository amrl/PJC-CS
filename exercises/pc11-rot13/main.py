infile = open("INPUT.txt", 'r')
message = infile.read()[:-1]
infile.close()

unscrambled = ""
for c in message:
    ordinal = ord(c)

    if 65 <= ordinal <= 90:
        unscrambled_ord = ordinal + 13
        if unscrambled_ord > 90:
            unscrambled_ord = unscrambled_ord - 90 + 64

    elif 97 <= ordinal <= 122:
        unscrambled_ord = ordinal + 13
        if unscrambled_ord > 122:
            unscrambled_ord = unscrambled_ord - 122 + 96

    else:
        unscrambled_ord = ordinal  # no change

    unscrambled_c = chr(unscrambled_ord)
    unscrambled += unscrambled_c

print(unscrambled)
