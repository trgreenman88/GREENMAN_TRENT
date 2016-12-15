import random
XandO = []
for i in range(0, 4):
    XandO.append([])
    for j in range(0, 4):
        switch = random.randint(1, 100)
        if switch == 1:
            XandO.append("X")
        else:
            XandO.append("O")
for k in XandO:
    output = ""
    for l in k:
        output += l
    print(output)
