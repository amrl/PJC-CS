from random import randint


def random_encoder():
    punctuations = ['', '!', '?', ',', '.', ' ', ';', '"', "'"]

    while True:  # obtain valid input from user
        sentence = input("Enter a sentence to encode: ")

        valid = True  # input check
        for c in sentence:
            if not c.isalpha() and c not in punctuations:
                valid = False

        if valid:
            break  # exit loop if sentence is valid
        print("Invalid input. Try again.")  # oops

    encoded = []    # list to contain integers representing the chars
    mode = "upper"  # starting mode - uppercase (since 1st letter capitalised)

    for c in sentence:

        if c.isupper():       # current char is uppercase letter
            if mode == "lower":
                encoded.extend(('0', '0'))  # switch modes twice
            elif mode == "punct":
                encoded.append('0')         # switch modes once
            mode = "upper"    # ensure current mode corresponds to current char
            encoded.append(str((ord(c) - 64) + 27*randint(0, 100)))

        elif c.islower():     # current char is lowercase letter
            if mode == "punct":
                encoded.extend(('0', '0'))  # switch modes twice
            elif mode == "upper":
                encoded.append('0')         # switch modes once
            mode = "lower"    # ensure current mode corresponds to current char
            encoded.append(str((ord(c) - 96) + 27*randint(0, 100)))

        else:                 # current char is a punctuation
            if mode == "upper":
                encoded.extend(('0', '0'))  # switch modes twice
            elif mode == "lower":
                encoded.append('0')         # switch modes once
            mode = "punct"    # ensure current mode corresponds to current char
            encoded.append(str((punctuations.index(c)) + 9*randint(0, 100)))

    return ','.join(encoded)  # integers joined as a string, comma delimited
