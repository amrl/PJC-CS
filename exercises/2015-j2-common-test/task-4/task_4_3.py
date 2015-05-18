def addParity(rows):
    # add parity to each row
    for index, eachrow in enumerate(rows):
        ones_count = 0
        for bit in eachrow:
            if bit == '1':
                ones_count += 1
        if ones_count % 2 == 0:
            rows[index] = eachrow + '0'
        else:
            rows[index] = eachrow + '1'

    # transpose the matrix
    columns = []
    for index in range(len(rows[0])):
        columns.append(''.join(eachrow[index] for eachrow in rows))

    # add parity to each column
    for index, eachcolumn in enumerate(columns):
        ones_count = 0
        for bit in eachcolumn:
            if bit == '1':
                ones_count += 1
        if ones_count % 2 == 0:
            columns[index] = eachcolumn + '0'
        else:
            columns[index] = eachcolumn + '1'

    # revert transposition
    rows = []
    for index in range(len(columns[0])):
        rows.append(''.join(eachcolumn[index] for eachcolumn in columns))

    return rows


with open("DATA43.txt", 'r') as infile:
    no_of_sets = int(infile.readline())

    while no_of_sets > 0:
        rows = []

        for line in infile:
            if line[:-1] != '*':
                rows.append(line[:-1])
            else:
                newrows = addParity(rows)

                for eachrow in newrows:
                    print(eachrow)

                print()
                break

        no_of_sets -= 1

    # 2nd method - without using the no_of_sets variable
    # Drawback - have to read the whole file into memory
    #
    # sets = infile.read().split('*\n')[:-1]
    # for rows in sets:
    #     rows = rows.split('\n')[:-1]
    #     newrows = addParity(rows)
    #     for eachrow in newrows:
    #         print(eachrow)
    #     print()
