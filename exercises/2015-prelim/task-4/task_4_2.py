from task_4_1 import Stack


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
