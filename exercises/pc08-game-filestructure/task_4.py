def HashKey(username):
    ascii_sum = 0
    for c in username:
        ascii_sum += ord(c)

    address = ascii_sum % 31 + 1

    return address
