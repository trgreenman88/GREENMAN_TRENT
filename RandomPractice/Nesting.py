num = int(input("Please enter a number"))

if num > 4:
    print("It meeets the first condition")
    if num <= 10:
        print("It meets both conditions!")

else:
    print("It meets none of the conditions!")

mathORwords = int(input("Would you like to..." +
                        "\n 1. Do a Math problem" +
                        "\n 2. Answer a question"))
if mathORwords == 1:
    mathAnswer = int(input("Wat is 2 * 2?"))
    if mathAnswer == 4:
                     print("Correct!")
    else: print("No!")
else:
    wordAnswer = input("Who said the phrase \"Whatever you are, be a good one.\"")
    if wordAnswer == "Abraham Lincoln":
        print("Correct!")
    else:
        print("No!")

print("Logical Operators")

#a = True
#b = False
#print( a and b )
#print( a or b )
#print( not (a and b) )
guess = int(input("Pick a number between 1 and 10"))

if (guess >= 1 and guess <= 10):
    print("yep")
else:
    print("nope")



