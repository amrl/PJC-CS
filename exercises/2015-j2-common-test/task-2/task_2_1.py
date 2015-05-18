def get_cc_num():
    while True:
        cc_num = input("Enter credit card number: ")
        if cc_num.isdigit():
            if len(cc_num) == 16:
                if (cc_num[0] == '4'
                        or 51 <= int(cc_num[:2]) <= 55):
                    return cc_num
            elif len(cc_num) == 13:
                if cc_num[0] == '4':
                    return cc_num

        print("Error: Credit card number is not valid.\n")


def validate_cc_num():
    cc_num = get_cc_num()

    summ = 0
    x2 = False

    for i in range(1, len(cc_num) + 1):
        if x2:
            double = int(cc_num[-i]) * 2

            if double >= 10:
                summ += int(str(double)[0]) + int(str(double)[1])
            else:
                summ += double

            x2 = False

        else:
            summ += int(cc_num[-i])

            x2 = True

    return summ % 10 == 0
