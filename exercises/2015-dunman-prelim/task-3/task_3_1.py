def ISBN_Check_Digit(isbn):
    # check if isbn is ISBN10 or ISBN 13 by length
    chunks = isbn.split('-')
    length = len(''.join(chunks))

    if length == 9:  # ISBN-10
        summ = 0
        weight = 1
        for digit in isbn:
            if digit.isdigit():
                summ += int(digit) * weight
                weight += 1
        remainder = summ % 11
        if remainder == 10:
            check_digit = 'X'
        else:
            check_digit = str(remainder)

    elif length == 12:  # ISBN-13
        summ = 0
        multiplier = 1
        for digit in isbn:
            if digit.isdigit():
                summ += multiplier * int(digit)
                if multiplier == 1:
                    multiplier = 3
                else:
                    multiplier = 1
        remainder = summ % 10
        if remainder != 0:
            check_digit = str(10 - remainder)
        else:
            check_digit = '0'

    return check_digit


# Tests
# print(ISBN_Check_Digit("0-07-063546"))
# print(ISBN_Check_Digit("978-0-07-063546"))
