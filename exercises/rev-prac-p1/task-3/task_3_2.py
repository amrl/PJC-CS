def HashKey(Country):
    ascii_sum = 0
    for c in Country:
        ascii_sum += ord(c)
    key = ascii_sum % 53 + 1

    return key
