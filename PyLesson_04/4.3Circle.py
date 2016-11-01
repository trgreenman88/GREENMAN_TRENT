print("This program will help you to find the area of a circle")
r = float(input("What is the radius of your circle in feet?"))
area = 0
def setNums():
    global r
    r = r

def findArea():
    global area
    area = 2 * 3.14159265358979323 * r
setNums()
findArea()

print("The area of a circle with a radius of" , r, "meters is" , "{:00.5f}".format(area) , "square meters")

