# NOTE: this code can also handle variables with no explicit coefficients
# e.g. 'x', '-x', '+x'


def get_terms(string):
    """Return a list of terms found in a string.
    e.g. "-3x+7+x" => ['-3x', '+7', '+x']
    """
    terms = []

    term = string[0]
    for c in string[1:]:
        if c in ('+', '-'):
            terms.append(term)
            term = c
        else:
            term += c
    terms.append(term)

    return terms


# get equation from file
infile = open("equation.txt", 'r')
equation = infile.read()[:-1]
LHS, RHS = equation.split('=')
infile.close()

# get all the terms
LHS_terms = get_terms(LHS)
RHS_terms = get_terms(RHS)

# identify the char used as the variable ('x', 'a', etc.)
for c in equation:
    if c.isalpha():
        variable = c
        break

var_sum = 0  # sum of coefficients of all variables (as if all at LHS)
const_sum = 0  # sum of all constants (as if all at RHS)

for term in LHS_terms:
    if variable in term:  # term contains a variable
        coeff = term[:-1]

        if term == variable or coeff == '+':  # 'x', '+x'
            var_sum += 1
        elif coeff == '-':                    # '-x'
            var_sum -= 1
        else:
            var_sum += float(coeff)

    else:  # term is a constant
        const_sum -= float(term)

for term in RHS_terms:
    if variable in term:  # term contains a variable
        coeff = term[:-1]

        if term == variable or coeff == '+':  # 'x', '+x'
            var_sum -= 1
        elif coeff == '-':                    # '-x'
            var_sum += 1
        else:
            var_sum -= float(coeff)

    else:  # term is a constant
        const_sum += float(term)

# calculate and display result
result = const_sum / var_sum
print("{0} = {1:.3f}".format(variable, result))
