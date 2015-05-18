def efficiency(filename):
    with open(filename, 'r') as infile:
        m = len(infile.readline()[:-1])

        infile.seek(0)

        n = 0
        for line in infile:
            n += 1

    data_bits = n * m
    additional_bits = n + m + 1

    return round(data_bits / (data_bits + additional_bits), 2)
