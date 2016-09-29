print("This program will help you to find the perimeter of your rectangle.")
l = float(input("What is the length of your rectangle?"))
w = float(input("What is the width of your rectangle?"))
def calcPerim():
    return l * 2 + w * 2
    

print("Your rectangle is" , "{:00.5f}".format(calcPerim()) , "ft around")
