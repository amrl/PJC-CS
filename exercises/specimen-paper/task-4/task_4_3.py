from task_4_1 import roman_form


def denary_form(numeral):
    numeral = numeral.replace("XL", "XXXX")
    numeral = numeral.replace("IX", "VIIII")
    numeral = numeral.replace("IV", "IIII")

    roman_to_den = {"L": 50, "X": 10, "V": 5, "I": 1}
    denary = 0
    for c in numeral:
        denary += roman_to_den[c]

    return denary


def main():
    numeral1 = input("Enter a numeral between 1 and 20: ")
    numeral2 = input("Enter a numeral between 1 and 20: ")

    result = roman_form(denary_form(numeral1) + denary_form(numeral2))

    print(result)


# main()
