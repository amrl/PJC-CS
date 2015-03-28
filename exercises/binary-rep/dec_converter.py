from stack import Stack


def dec_converter(decNumber, base):
    answer_stack = Stack()

    if base == 16:
        hexa = 'ABCDEF'
        while decNumber >= 1:
            if decNumber % base == 0:
                answer_stack.push(0)
            else:
                remainder = decNumber % base
                if remainder >= 10:
                    answer_stack.push(hexa[remainder - 10])
                else:
                    answer_stack.push(remainder)

            decNumber //= base
    else:
        while decNumber >= 1:
            if decNumber % base == 0:
                answer_stack.push(0)
            else:
                answer_stack.push(decNumber % base)

            decNumber //= base

    answer = ""
    while not answer_stack.isEmpty():
        answer += str(answer_stack.pop())

    return answer


print(dec_converter(3, 8))
print(dec_converter(7, 8))
print(dec_converter(8, 8))
print(dec_converter(15, 8))
print(dec_converter(55, 8))
print(dec_converter(129, 8))

print(dec_converter(3, 16))
print(dec_converter(7, 16))
print(dec_converter(8, 16))
print(dec_converter(15, 16))
print(dec_converter(55, 16))
print(dec_converter(129, 16))
