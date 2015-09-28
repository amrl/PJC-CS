def RP_multiply(num1, num2):
    half_list = list()
    double_list = list()

    while num1 >= 1:
        half_list.append(num1)
        double_list.append(num2)
        num1 //= 2
        num2 *= 2

    summ = 0
    for index, number in enumerate(half_list):
        if number % 2 != 0:
            summ += double_list[index]

    return summ


# print(RP_multiply(57, 85))
