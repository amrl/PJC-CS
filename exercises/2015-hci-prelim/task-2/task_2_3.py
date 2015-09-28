from task_2_2 import decToBin


def Add_Binary(binNum1, binNum2):
    # reverse binary strings
    binNum1, binNum2 = str(binNum1)[::-1], str(binNum2)[::-1]

    # make both binary strings the same length
    if len(binNum1) > len(binNum2):
        binNum2 = binNum2.ljust(len(binNum1), '0')
    else:
        binNum1 = binNum1.ljust(len(binNum2), '0')

    carry = False
    result = ""
    for idx in range(len(binNum1)):
        if binNum1[idx] == '1' and binNum2[idx] == '1':    # 1 + 1
            if carry:         # 1 + 1 + 1
                result += '1'
            else:             # 1 + 1
                result += '0'
            carry = True
        elif binNum1[idx] == '0' and binNum2[idx] == '0':  # 0 + 0
            if carry:         # 0 + 0 + 1
                result += '1'
            else:             # 0 + 0
                result += '0'
            carry = False
        else:                                        # 1 + 0
            if carry:         # 1 + 0 + 1
                result += '0'
            else:             # 1 + 0
                result += '1'

    if carry:
        result += '1'

    result = result[::-1]
    if result[0] == '0':  # remove leading zero
        result = result[1:]

    return result


def RP_multiply_bin(decNum1, decNum2):
    binNum1, binNum2 = str(decToBin(decNum1)), str(decToBin(decNum2))

    half_list = list()
    double_list = list()

    while int(binNum1) >= 1:
        half_list.append(binNum1)
        double_list.append(binNum2)
        binNum1 = '0' + binNum1[:-1]
        binNum2 += '0'

    summ = list()
    for index, number in enumerate(half_list):
        if number[-1] == '1':
            summ.append(double_list[index])

    while len(summ) > 1:
        summ[0] = Add_Binary(summ[0], summ[1])
        summ.pop(1)

    print(summ.pop())


# RP_multiply_bin(13, 12)
