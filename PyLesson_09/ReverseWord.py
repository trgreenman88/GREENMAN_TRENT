words = ["happy", "sad", "excited", "angry", "surprised"]
print(words)



for i in words:
    print(words[1])



print("")
print("Reversed...")
word = input("Please enter a word: ")
myList = word.split("")
output = ""
for i in myList:
    output += str((-1) * (i))
print(output)
        
    


