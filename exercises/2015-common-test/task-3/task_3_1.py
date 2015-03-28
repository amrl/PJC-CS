class Node:

    def __init__(self, new_coeff, new_expon):
        self.coeff = float(new_coeff)
        self.expon = int(new_expon)
        self.ptr = None

    def setCoeff(self, new_coeff):
        self.coeff = float(new_coeff)

    def getCoeff(self):
        return self.coeff

    def setExpon(self, new_expon):
        self.expon = int(new_expon)

    def getExpon(self):
        return self.expon

    def setPtr(self, new_ptr):
        self.ptr = new_ptr

    def getPtr(self):
        return self.ptr

    def __str__(self):
        return "{0}x{1}".format(self.coeff, self.expon)


class Polynomial:

    def __init__(self):
        self.start = None

    def addVariable(self, new_node):
        current = self.start

        if current is None:
            self.start = new_node
        else:
            while current.getPtr() is not None:
                current = current.getPtr()

            current.setPtr(new_node)

    def __str__(self):
        current = self.start
        if current is None:
            return ""

        full_polynomial = []

        while current is not None:
            full_polynomial.append(str(current.getCoeff()) + 'x' +
                                   str(current.getExpon()))
            current = current.getPtr()

        return ' + '.join(full_polynomial)
