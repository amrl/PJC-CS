def checkError(rows):
    # search for the row with the error, if any
    error_row = None
    for index, eachrow in enumerate(rows):
        ones_count = 0
        for bit in eachrow:
            if bit == '1':
                ones_count += 1
        if ones_count % 2 != 0:
            error_row = index
            break

    if error_row is None:
        print("No error detected.\n")
    else:
        # transpose the matrix
        columns = []
        for index in range(len(rows[0])):
            columns.append(''.join(eachrow[index] for eachrow in rows))

        # search for the column with the error
        for index, eachcolumn in enumerate(columns):
            ones_count = 0
            for bit in eachcolumn:
                if bit == '1':
                    ones_count += 1
            if ones_count % 2 != 0:
                error_column = index
                break

        # revert transposition
        rows = []
        for index in range(len(columns[0])):
            rows.append(''.join(eachcolumn[index] for eachcolumn in columns))

        # correct the error
        rows[error_row] = bitFlip(rows[error_row], error_column)

        # display corrected bits, without parity bits
        print("Error at ({0},{1})".format(error_row, error_column))
        print("Correct data: ", end="")
        for eachrow in rows:
            print(eachrow[:-1], end=" ")
        print()


def bitFlip(bitstring, index):
    """Flip the bit at the specified index of the bit string"""
    if bitstring[index] == '1':
        return bitstring[:index] + '0' + bitstring[index+1:]
    else:
        return bitstring[:index] + '1' + bitstring[index+1:]


with open("DATA41.txt", 'r') as infile:
    # read in all the rows
    allrows = []
    for line in infile:
        allrows.append(line[:-1])

    # separate the 2 datasets
    for index, eachrow in enumerate(allrows):
        if len(eachrow) != len(allrows[0]):
            start_index_2nd_set = index
            break

    set_1 = allrows[:start_index_2nd_set]
    set_2 = allrows[start_index_2nd_set:]
    sets = [set_1, set_2]

    # check for errors
    for eachset in sets:
        checkError(eachset)
