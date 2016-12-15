values = []
values.append([1, 2, 3, 4])   #gets added @values[0]
values.append([5, 6, 7, 8])  #gets added @values[1]
values.append([9, 10, 11, 12]) #gets added @values[2]
values.append([13, 14, 15, 16]) #gets added @values[3]
print("\nHere is what a list of lists looks like...")
print(values, "\n")
print(values[0][2])
print("")







print("Using range...")
for i in range(0, len(values)): #outer loop: loops through list (columns)
    output = ""   
    for j in range(0, len(values[i])): #inner loop: loops through position i (rows)
        output += str(values[i][j]) + "\t"
    print(output)
    
    







print("Using enhanced loop...")
for value in values:
   output = ""
   for num in value:
       output += str(num) + "\t"
   print(output + "\n")








print("Search the list...")
count = 0
for value in values:
   for number in value:
       if number % 5 == 0:
           count += 1
print("There are ", count, " multiples of 5 in the array.\n\n")







lettersList = []
lettersList.append(["a", "b", "c", "d"])
lettersList.append(["e", "f", "g", "h"])
lettersList.append(["i", "j", "k", "l"])
lettersList.append(["m", "n", "o", "p"])

print("Here is a list with letters...")

for letters in lettersList:
   output = ""
   for letter in letters:
       output += str(letter) + "\t"
   print(output)









print("\nHere is a list of words using split()...\n")
wordsList = []
go = "father mother eagle house car office coffee make create laugh cry photo"
spList = go.split(" ")
spot = 0
for i in range(0, 3):
   output = ""
   wordsList.append([])
   for j in range(0, 4):
       wordsList[i].append(spList[spot])
       output += wordsList[i][j] + "\t"
       spot += 1
   print(output)












