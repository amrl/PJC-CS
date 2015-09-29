# NOTE: The task only requires conversion of denary to roman form for numbers
# between 1 and 20 inclusive. This code expands that range since implementation
# is trivial.


def val_denary(denary):
    return denary.isdigit() and 1 <= int(denary) <= 20


def roman_form(denary):
    """Return the roman numeral form of a denary number.
    (only for 1 to 89 inclusive)
    """
    # split into digits and reverse
    digits = list(str(denary))[::-1]
    special_roman = {4: "IV", 5: "V", 9: "IX"}

    power = 0
    full_numeral = list()
    for digit in digits:
        numeral = ""

        number = int(digit) * 10**power
        if number >= 10:
            tens = number // 10
            if 10 <= number <= 39:
                numeral += "X"*tens
            elif 40 <= number <= 49:
                numeral += "XL"
            else:
                remaining_tens = (number-50) // 10
                numeral += "L"
                numeral += "X"*remaining_tens
            ones = number - 10*tens
        else:
            ones = number

        for curr_digit in range(1, ones+1):
            if curr_digit in special_roman:
                numeral = special_roman[curr_digit]
            else:
                numeral += 'I'

        full_numeral.append(numeral)
        power += 1

    full_numeral = ''.join(full_numeral[::-1])

    return full_numeral


def main():
    while True:
        denary = input("Enter a number between 1 and 20 inclusive: ")
        if val_denary(denary):
            break
        else:
            print("\n* Error: Invalid denary number. Try again. *\n")

    print("{0}: {1}".format(denary, roman_form(denary)))


# main()
