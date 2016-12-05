expression = input("Please enter an expression without spaces: ")
eqn = expression.split("")
while i < len(eqn):
    if i < len(eqn) and eqn[i] == "*" or "/":
        if eqn[i] == "*":
            eqn[i] = int(eqn[i-1]) * int(eqn[i+1])
        else:
            equation[i] = int(eqn[i-1]) / int(eqn[i+1])
        eqn.pop(i-1)
        eqn.pop(i)
    i += 1
i = 0
while i < len(eqn)
