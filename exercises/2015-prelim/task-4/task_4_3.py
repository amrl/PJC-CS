from task_4_1 import Stack


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
