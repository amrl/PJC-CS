# Merged all the Tasks together


class Stack:

    def __init__(self, lim):
        self.Limit = lim
        self.Data = []  # max size => self.Limit

    def IsEmpty(self):
        return len(self.Data) == 0

    def IsFull(self):
        return len(self.Data) == self.Limit

    def Push(self, data):
        self.Data.append(data)

    def Pop(self):
        return self.Data.pop()

    def Peek(self):
        return self.Data[-1]

    def Size(self):
        return len(self.Data)

    def Display(self):
        for data in self.Data:
            print(data)
        print("TOP OF STACK")


def infixToPostfix(infixexpression):
    opStack = Stack(len(infixexpression))
    output = []

    ###########################################################################
    # Use this when parenthesis are not separated from numbers by spaces
    # e.g. (6 + 2)
    ###########################################################################
    # raw_tokens = infixexpression.split()
    # tokens = []
    # for token in raw_tokens:
    #     if token.startswith('('):
    #         tokens.append('(')
    #         tokens.append(token[1:])
    #     elif token.endswith(')'):
    #         tokens.append(token[:-1])
    #         tokens.append(')')
    #     else:
    #         tokens.append(token)
    ###########################################################################

    tokens = infixexpression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            opStack.Push(token)
        elif token in ('*', '/', '+', '-'):
            if token in ('*', '/'):
                while not opStack.IsEmpty() and opStack.Peek() in ('*', '/'):
                    output.append(opStack.Pop())
            else:
                while (not opStack.IsEmpty()
                       and opStack.Peek() in ('*', '/', '+', '-')):
                    output.append(opStack.Pop())
            opStack.Push(token)
        elif token == ')':
            while opStack.Peek() != '(':
                output.append(opStack.Pop())
            opStack.Pop()

    while not opStack.IsEmpty():
        output.append(opStack.Pop())

    return ' '.join(output)


def postfixEval(postfixexpression):
    operandStack = Stack(len(postfixexpression))

    tokens = postfixexpression.split()

    for token in tokens:
        if token.isdigit():
            operandStack.Push(int(token))
        elif token in ('*', '/', '+', '-'):
            second_op = operandStack.Pop()
            first_op = operandStack.Pop()
            if token == '*':
                result = first_op * second_op
            elif token == '/':
                result = first_op / second_op
            elif token == '+':
                result = first_op + second_op
            elif token == '-':
                result = first_op - second_op
            operandStack.Push(result)

    answer = float(operandStack.Pop())
    return answer


# Task 4.4
infile = open("Infix.txt", "r")
for line in infile:
    postfix = infixToPostfix(line[:-1])
    answer = postfixEval(postfix)
    print(answer)
infile.close()
