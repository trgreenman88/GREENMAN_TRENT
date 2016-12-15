myList = [1, 2, 3, 4, 5]
print(myList[2])
print(myList[0:2])
print(myList)
#last term is exclusive and first term starts at 0
output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1:
        output += ", "
    j+=1
print(output)




List = []
for i in range(0, 8):
    List.append(i*4)

out = ""
j = 0
for i in List:
    out += str(i)
    if j < len(List):
        out += ", "
    j += 1
    
print(List)





word = "P r o f e s s o r"
Litht = word.split(" ")

O = ""
for i in Litht:
    O += (i)
print(O)
    







