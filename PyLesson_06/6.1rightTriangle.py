word = input("Please enter a word: ")
def printTri():
    for i in range(len(word), 0, -1):
        print(word[i:len(word)])
printTri()
    
