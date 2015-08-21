# get equation from file
infile = open("equation3.txt", 'r')
equation = infile.read()[:-1]
LHS, RHS = equation.split('=')
infile.close()

# identify the char used as the variable ('x', 'a', etc.)
for c in equation:
    if c.isalpha():
        variable = c
        break

# get all the terms in the LHS
left_terms = []
term = LHS[0]
for c in LHS[1:]:
    if c in ('+', '-'):
        left_terms.append(term)
        term = c
    else:
        term += c
left_terms.append(term)

# get all the terms in the RHS
right_terms = []
term = RHS[0]
for c in RHS[1:]:
    if c in ('+', '-'):
        right_terms.append(term)
        term = c
    else:
        term += c
right_terms.append(term)

# get the sum of the coefficients of the variable (as if all vars are on LHS)
var_sum = 0
for term in left_terms:
    if variable in term:  # if term contains a variable
        coeff = term[:-1]
        if term == variable or coeff == '+':  # 'x', '+x'
            var_sum += 1
        elif coeff == '-':                    # '-x'
            var_sum -= 1
        else:
            var_sum += float(coeff)
for term in right_terms:
    if variable in term:  # if term contains a variable
        coeff = term[:-1]
        if term == variable or coeff == '+':  # 'x', '-x'
            var_sum -= 1
        elif coeff == '-':                    # '-x'
            var_sum += 1
        else:
            var_sum -= float(coeff)

# get the sum of the constants (as if all constsants are on RHS)
const_sum = 0
for term in left_terms:
    if variable not in term:
        const_sum -= float(term)
for term in right_terms:
    if variable not in term:
        const_sum += float(term)

# calculate and display result
result = const_sum / var_sum
print("{0} = {1:.3f}".format(variable, result))
