import random
numsList = []
for i in range(0, 4):
    numsList.append([random.randint(1, 100)])
    numsList.append([random.randint(1, 100)])
    numsList.append([random.randint(1, 100)])
    numsList.append([random.randint(1, 100)])
    output = ""
    for j in range(0, len(numsList)):
        output += str(numsList[i][j]) + " "
    print(output)
        
    
