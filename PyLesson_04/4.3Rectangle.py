print("This program will help you to find the perimeter of your rectangle.")
l = float(input("What is the length of your rectangle?"))
w = float(input("What is the width of your rectangle?"))
perim = 0
def setNums():
    global l, w
    l = l
    w = w

def findPerim():
    global perim
    perim = l * 2 + w * 2
setNums()
findPerim()

print("Your rectangle is" , "{:00.5f}".format(perim) , "feet around.")


