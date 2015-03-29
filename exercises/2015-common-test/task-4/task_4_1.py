# Note: This program only deals with 1 set of data, as opposed to 2 sets
# indicated by the question. Add your own code to complete it.


def find_error():
    # input each row into a list
    with open("DATA41.txt", 'r') as infile:
        rows = []
        for line in infile:
            rows.append(line[:-1])

    # find the row with the error, if it exists
    error_row = None
    for row_number, line in enumerate(rows):
        ones_count = 0
        for bit in line:
            if bit == '1':
                ones_count += 1
        if ones_count % 2 != 0:
            error_row = row_number
            break

    if error_row is None:
        print("No error detected.")
    else:
        # input each column into a list
        columns = []
        for index in range(len(rows)):
            columns.append(''.join(row[index] for row in rows))

        # find the column with the error
        for column_number, line in enumerate(columns):
            ones_count = 0
            for bit in line:
                if bit == '1':
                    ones_count += 1
            if ones_count % 2 != 0:
                error_column = column_number

        # replace the row in the list (rows) with the corrected row
        new_row = ""
        for column, bit in enumerate(rows[error_row]):
            if column == error_column:
                if bit == '1':
                    new_row += '0'
                else:
                    new_row += '1'
            else:
                new_row += bit
        rows[error_row] = new_row

        # remove the last row and column (parity bits) before final printing
        for count, row in enumerate(rows):
            rows[count] = row[:-1]
        rows.pop()

        print("Error at ({0},{1})".format(error_row, error_column))
        print("Correct data: {0}".format(' '.join(rows)))
