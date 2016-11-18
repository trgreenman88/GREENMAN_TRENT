words = ["happy", "sad", "excited", "angry", "surprised"]


print("In order...")
output = ""
for i in words:
    output += i + " "
print(output)



print("")
print("Reversed...")
output = ""
for i in range(len(words)-1, -1, -1):
    output += words[i] + " "
print(output)
        
    


