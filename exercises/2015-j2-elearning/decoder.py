def decoder():
    with open("textstream.txt", 'r') as infile:
        textstream = infile.read()
        integers = [int(i) for i in textstream.split(',')]
        # make a list containing each integer from the text stream

    punctuations = ['', '!', '?', ',', '.', ' ', ';', '"', "'"]

    decoded = ""    # final output
    mode = "upper"  # starting mode - uppercase

    for number in integers:  # time to decode each integer in the list

        if mode == "upper":
            if number % 27 == 0:
                mode = "lower"  # switch to lowercase mode
            else:
                decoded += chr(number % 27 + 64)

        elif mode == "lower":
            if number % 27 == 0:
                mode = "punct"  # switch to punctuation mode
            else:
                decoded += chr(number % 27 + 96)

        else:
            if number % 9 == 0:
                mode = "upper"  # switch to uppercase mode
            else:
                decoded += punctuations[number % 9]

    print(decoded)
