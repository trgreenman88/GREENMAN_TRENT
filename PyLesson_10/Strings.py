go = input("Please enter 16 words with spaces: ")
spList = go.split(" ")
wordsList = []
spot = 0
for i in range(0, 4):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(spList[spot])
        output += wordsList[i][j] + "\t"
        spot += 1
    print(output)
        
