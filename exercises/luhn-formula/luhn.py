def verify_luhn(id_number):
    id_number = str(id_number)

    if not id_number.isdigit():
        # raise TypeError('Invalid input type. Only numbers allowed.')
        return -1
    if len(id_number) == 1:
        # raise ValueError('Invalid input format. Number has to be > 1 digit.')
        return -1

    id_digits = []
    for c in id_number:
        id_digits.append(int(c))

    check_digit = id_digits.pop()

    rev_id_digits = [id_digits[-i] for i in range(1, len(id_digits) + 1)]

    times_2 = True
    sum_of_digits = 0

    for digit in rev_id_digits:
        if times_2:
            digit_x2 = digit * 2

            if digit_x2 > 9:
                sum_of_digits += int(str(digit_x2)[0]) + int(str(digit_x2)[1])
            else:
                sum_of_digits += digit_x2

            times_2 = False

        else:
            sum_of_digits += digit

            times_2 = True

    return (sum_of_digits + check_digit) % 10 == 0


def gen_luhn(id_number):
    id_number = str(id_number)

    if not id_number.isdigit():
        # raise TypeError('Invalid input type. Only enter numbers.')
        return -1
    if len(id_number) == 1:
        # raise ValueError('Invalid input format. Number has to be > 1 digit.')
        return -1

    id_digits = []
    for c in id_number:
        id_digits.append(int(c))

    rev_id_digits = [id_digits[-i] for i in range(1, len(id_digits) + 1)]

    times_2 = True
    sum_of_digits = 0

    for digit in rev_id_digits:
        if times_2:
            digit_x2 = digit * 2

            if digit_x2 > 9:
                sum_of_digits += int(str(digit_x2)[0]) + int(str(digit_x2)[1])
            else:
                sum_of_digits += digit_x2

            times_2 = False

        else:
            sum_of_digits += digit

            times_2 = True

    for check_digit in range(10):
        if (sum_of_digits + check_digit) % 10 == 0:
            id_number = int(id_number + str(check_digit))
            break

    return id_number


# TEST
print(verify_luhn('asparagus'))
print(verify_luhn(737))
print(verify_luhn(1762483))
print(verify_luhn(9781471134896))
print()
print(gen_luhn(234))
print(gen_luhn(5813674))
