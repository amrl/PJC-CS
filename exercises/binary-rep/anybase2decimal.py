from stack import Stack


def anybase2decimal(number, base):
    answer_stack = Stack()

    for digit in str(number):
        answer_stack.push(digit)

    power = 0
    decNumber = 0

    if base == 16:
        hexa = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        while not answer_stack.isEmpty():
            digit = answer_stack.pop()
            if digit.isalpha():
                decNumber += hexa[digit] * base**power
            else:
                decNumber += int(digit) * base**power
            power += 1
    else:
        while not answer_stack.isEmpty():
            decNumber += int(answer_stack.pop()) * base**power
            power += 1

    return decNumber


print(anybase2decimal(10, 8))
print(anybase2decimal(546, 8))
print(anybase2decimal(3562, 8))

print(anybase2decimal("1F", 16))
print(anybase2decimal("CAD", 16))
print(anybase2decimal("EBCA", 16))
