from task_3_1 import Node, Polynomial
from task_3_2 import createPolynomial


def addTwoPolynomials():
    print("- First polynomial -\n")
    p1 = createPolynomial()

    print("- Second polynomial -\n")
    p2 = createPolynomial()

    p1_current = p1.start
    p2_current = p2.start

    p3 = Polynomial()

    while p1_current is not None and p2_current is not None:
        if p1_current.getExpon() > p2_current.getExpon():
            p3.addVariable(Node(p1_current.getCoeff(), p1_current.getExpon()))
            p1_current = p1_current.getPtr()
        elif p1_current.getExpon() < p2_current.getExpon():
            p3.addVariable(Node(p2_current.getCoeff(), p2_current.getExpon()))
            p2_current = p2_current.getPtr()
        else:
            sum_of_coeffs = p1_current.getCoeff() + p2_current.getCoeff()
            p3.addVariable(Node(sum_of_coeffs, p1_current.getExpon()))
            p1_current = p1_current.getPtr()
            p2_current = p2_current.getPtr()

    if p1_current is not None:
        while p1_current is not None:
            p3.addVariable(Node(p1_current.getCoeff(), p1_current.getExpon()))
            p1_current = p1_current.getPtr()
    elif p2_current is not None:
        while p2_current is not None:
            p3.addVariable(Node(p2_current.getCoeff(), p2_current.getExpon()))
            p2_current = p2_current.getPtr()

    return p3


# # Task 3.5
# p3 = addTwoPolynomials()
# print(p3)
