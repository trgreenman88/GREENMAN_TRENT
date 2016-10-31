print("This program will help you to find the perimeter of your rectangle.")
l = float(input("What is the length of your rectangle in feet?"))
w = float(input("What is the width of your rectangle in feet?"))
def calcPerim():
    global perim
    perim = l * 2 + w * 2
calcPerim()
    

print("Your rectangle is" , "{:00.5f}".format(perim) , "ft around")
