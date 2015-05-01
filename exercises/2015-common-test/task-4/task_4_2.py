def efficiency(filename):
    with open(filename, 'r') as infile:
        rows = []
        for line in infile:
            rows.append(line[:-1])

    n = len(rows)
    m = len(rows[0])

    data_bits = n * m
    additional_bits = n + m + 1

    return round(data_bits / (data_bits + additional_bits), 2)
