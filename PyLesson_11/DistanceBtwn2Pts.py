import math
class Distance:
    def __init__(self, x1, x2, y1, y2):
        self.xOne = x1
        self.xTwo = x2
        self.yOne = y1
        self.yTwo = y2
    distance = 0

    def setX1(self, newx1):
        self.xOne = newx1
    def setX2(self, newx2):
        self.xTwo = newx2
    def setY1(self, newy1):
        self.yOne = newy1
    def setY2(self, newy2):
        self.yTwo = newy2

    def getX1(self):
        return self.xOne
    def getX2(self):
        return self.xTwo
    def getY1(self):
        return self.yOne
    def getY2(self):
        return self.yTwo
    def getDist(self):
        distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return distance

def main():
    x1 = float(input("Please enter a number for your first x coordinate: "))
    y1 = float(input("Please enter a number for your first y coordinate: "))
    x2 = float(input("Please enter a number for your second x coordinate: "))
    y2 = float(input("Please enter a number for your second y coordinate: "))

    distance1 = Distance(x1, x2, y1, y2)

    print("The distance between the points (" , distance1.getX1(), "," , distance1.getY1() , ") and (" , distance1.getX2() , "," , distance1.getY2() , ") is" , distance1.getDist())
main()
        
