def Hash_Key(isbn):
    isbn = ''.join(isbn.split('-'))
    # Parse ISBN into string of numbers only.

    ascii_sum = 0
    for c in isbn:
        ascii_sum += ord(c)
    # Obtain a value likely unique to each ISBN.

    address = ascii_sum % 251
    # Generate an address to insert each ISBN into.

    bucket = 7 - ascii_sum % 7
    # Used when collision at address encountered.
    # Jump through addresses by multiples of the bucket until an empty
    # address is found.

    return address, bucket
