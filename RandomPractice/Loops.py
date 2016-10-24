output = ""
for i in range(10, 0, -1):
    output = output + str(i) + " "
print(output)



word = "COMPPROG"
print(len(word))

print(word.index("R"))

print(word[1:4])




need = int(input("Please enter the number of cookies that you need:"))
bs = 25
batch = 1

for cookies in range(need, -1, -bs):
    print("Cookies Needed: ", cookies)
    print("Batch #: ", batch)
    batch = batch + 1

print("Order UP!")




vord = input("Please enter a word: ")

for l in range(0, len(vord)):
    print(vord[l])



wword = input("Please enter a word: ")
def printTri():
    for u in range(0, len(wword) + 1):
        print(wword[0:u])
printTri()


