def barchart3():
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

    maximum = -1
    for freq in freq_list:
        if freq > maximum:
            maximum = freq

    if maximum > 60:
        downscale = True
        factor = maximum / 60  # factor to downscale frequencies
    else:
        downscale = False

    # header
    print()
    print('+'*80)
    print("Frequency distribution")
    print('+'*80)

    # bar charts
    if downscale is True:
        for x_value, freq in zip(x_list, freq_list):
            print("{0:20}{1}".format(' ', '\u2588'*int((freq/factor))))
            print("{0:^20}{1}".format(x_value, '\u2588'*int((freq/factor))))
            print("{0:20}{1}".format(' ', '\u2588'*int((freq/factor))))
            print()

        # horizontal axis
        print("{0:20}{1}".format(' ', '-'*60))
        step = maximum / 6
        print("{0:20}{1:<10}{2:<10.1f}{3:<10.1f}{4:<10.1f}{5:<10.1f}{6:<10.1f}"
              "{7:.1f}"
              .format(' ', 0.0, step, 2*step, 3*step, 4*step, 5*step, 6*step))
    else:
        for x_value, freq in zip(x_list, freq_list):
            print("{0:20}{1}".format(' ', '\u2588'*freq))
            print("{0:^20}{1}".format(x_value, '\u2588'*freq))
            print("{0:20}{1}".format(' ', '\u2588'*freq))
            print()

        # horizontal axis
        print("{0:20}{1}".format(' ', '-'*60))
        print("{0:20}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}{6:<10}{7}"
              .format(' ', 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0))
