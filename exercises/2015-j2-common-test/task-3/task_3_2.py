from task_3_1 import Node, Polynomial


def createPolynomial():
    poly = Polynomial()

    while True:
        coeff = input("Enter the coefficient (0 to exit): ")
        if coeff == '0':
            print()
            break
        expon = input("Enter the exponent: ")
        poly.addVariable(Node(coeff, expon))
        print()

    return poly


# # Task 3.3
# p1 = createPolynomial()
# print(p1)
