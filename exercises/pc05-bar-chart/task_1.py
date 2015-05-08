def barchart():
    max_input = 6
    x_list = []
    freq_list = []

    while max_input > 0:
        x_value = input("Next X value ... <ZZZ to END> ")

        if x_value == "ZZZ":
            break
        else:
            freq = int(input("Frequency ... "))

            x_list.append(x_value)
            freq_list.append(freq)

        max_input -= 1

    # header
    print()
    print('+'*80)
    print("Frequency distribution")
    print('+'*80)

    # bar charts
    for x_value, freq in zip(x_list, freq_list):
        print("{0:^20}{1}".format(x_value, '@'*freq))
