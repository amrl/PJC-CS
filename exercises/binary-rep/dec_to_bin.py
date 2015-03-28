from stack import Stack


def dec_to_bin(decNumber):
    binary_stack = Stack()

    while decNumber >= 1:
        if decNumber % 2 == 0:
            binary_stack.push(0)
        else:
            binary_stack.push(1)

        decNumber //= 2

    binary_number = ""
    while not binary_stack.isEmpty():
        binary_number += str(binary_stack.pop())

    return binary_number


print(dec_to_bin(3))
print(dec_to_bin(6))
print(dec_to_bin(9))
print(dec_to_bin(12))
print(dec_to_bin(77))
print(dec_to_bin(129))
