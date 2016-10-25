word = input("Please print a word: ")

def printWord():
    for i in range(0, len(word)):
        print(word[0:len(word)])

printWord()
