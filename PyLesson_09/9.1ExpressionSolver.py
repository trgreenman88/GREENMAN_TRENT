expression = input("Please enter an expression with spaces: ")
eqn = expression.split(" ")
i = 0
while i < len(eqn):
    if i < len(eqn) and eqn[i] == "*" or eqn[i] == "/":
        if eqn[i] == "*":
            eqn[i] = int(eqn[i-1]) * int(eqn[i+1])
        else:
            eqn[i] = float(eqn[i-1]) / float(eqn[i+1])
        eqn.pop(i-1)
        eqn.pop(i)
    i += 1
i = 0
while i < len(eqn):
    if i < len(eqn) and eqn[i] == "+" or eqn[i] == "-":
        if eqn[i] == "+":
            eqn[i] = int(eqn[i-1]) + int(eqn[i+1])
        else:
            eqn[i] = int(eqn[i-1]) - int(eqn[i+1])
        eqn.pop(i-1)
        eqn.pop(i)
    i += 1
print(eqn)
