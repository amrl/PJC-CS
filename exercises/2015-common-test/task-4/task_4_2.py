def efficiency():
    with open("DATA42.txt", 'r') as infile:
        n = 0
        m = 0
        for line in infile:
            n += 1
            m = len(line) - 1

    data_bits = m * n
    add_bits = m + n + 1
    efficiency = data_bits / (data_bits + add_bits)

    print("{0:.2f}".format(efficiency))
