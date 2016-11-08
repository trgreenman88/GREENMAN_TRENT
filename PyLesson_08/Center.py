word1 = input("Please enter your first word: ")
word2 = input("Please enter your second word: ")
word3 = input("Please enter your third word: ")
def makeCenter(word1):
    if int(len(word1)) >= 20:
        return (word1)
    else:
        return (makeCenter(" " + word1 + " "))
print(makeCenter(" " + word1 + " "))    
def makeCenter(word2):
    if int(len(word2)) >= 20:
        return (word2)
    else:
        return (makeCenter(" " + word2 + " "))
print(makeCenter(" " + word2 + " "))    
def makeCenter(word3):
    if int(len(word3)) >= 20:
        return (word3)
    else:
        return (makeCenter(" " + word3 + " "))
print(makeCenter(" " + word3 + " "))
   
    
