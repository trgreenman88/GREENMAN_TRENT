word = input("Please print a word: ")
def printTri():
    for i in range(len(word), 0, -1):
        print(word[0:i])
printTri()
    
