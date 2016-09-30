print("This program will help you to find the surface area of a cube")
side = float(input("What is the length of any given side of your cube in feet"))
def setNums(side):
    global SIDE
    SIDE = side

def findSA(SIDE):
    return SIDE * SIDE * 6

print("The surface area of a cube with sides that are" , side, "feet long is" , "{:00.5f}".format(findSA(side)) , "square feet")
