print("This program will help you to find the perimeter of your rectangle.")
l = float(input("What is the length of your rectangle?"))
w = float(input("What is the width of your rectangle?"))
def setNums(l,w):
    global length, width
    length = l
    width = w

def findPerim(length,width):
    return length * 2 + width * 2

print("Your rectangle is" , "{:00.5f}".format(findPerim(l,w)) , "feet around.")


