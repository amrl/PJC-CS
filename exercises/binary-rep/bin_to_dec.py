from stack import Stack


def bin_to_dec(binNumber):
    binary_stack = Stack()

    for digit in str(binNumber):
        binary_stack.push(digit)

    power = 0
    decNumber = 0
    while not binary_stack.isEmpty():
        decNumber += int(binary_stack.pop()) * 2**power
        power += 1

    return decNumber


BINARY = [1011, 10001011, 1100000010110101, 100010010010011010101011,
          11111010010110101010101110101100]

for number in BINARY:
    print(bin_to_dec(number))
