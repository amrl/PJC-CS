from task_4 import HashKey


def HandleCollision(record, outfile):
    username = record[:15].rstrip()

    # start at next address
    address = HashKey(username) + 1

    # find free address
    outfile.seek((address-1) * 57)
    while outfile.read(1).isalpha():
        address += 1  # move on to the next address
        outfile.seek((address-1) * 57)

    # write to outfile at correct position
    outfile.seek((address-1) * 57)
    outfile.write(record)
