class Car:
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setPaint(self, newP):
        self.paint = newP
    def setInterior(self, newI):
        self.interior = newI
    def setEngine(self, newE):
        self.engine = newE
    def setTires(self, newT):
        self.tires = newT

    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires

def main():
    paint = input("Please enter the color of your car: ")
    interior = input("Please enter the interior type of your car: ")
    engine = input("Please enter the engine type of your car: ")
    tires = input("Please enter the tire type of your car: ")
    
    car1 = Car(paint, interior, engine, tires)

    print("Your vehicle is ready...")
    print("Paint: " , car1.getPaint())
    print("Interior: " , car1.getInterior())
    print("Engine: " , car1.getEngine())
    print("Tires: " , car1.getTires())
main()


class Human:
    def __init__(self, hair, eyes, skin):
        self.h = hair
        self.e = eyes
        self.s = skin
    def setHair(self, h):
        self.h = newHair
    def setEyes(self, e):
        self.e = newEyes
    def setSkin(self, s):
        self.s = newSkin
    def getHair(self):
        return self.h
    def getEyes(self):
        return self.e
    def getSkin(self):
        return self.s
class HumanDriver:
    h = input("Please enter hair color: ")
    e = input("Please enter eye color: ")
    s = input("Please enter skin color: ")

    human1 = Human(h, e, s)
    print("Hair color: " , human1.getHair())
    print("Eye color: " , human1.getEyes())
    print("Skin color: " , human1.getSkin())

    human1.setHair("Brown")
    human1.setEyes("Brown")
    human1.setSkin("White")
    print("Hair color: " , human1.getHair())
    print("Eye color: " , human1.getEyes())
    print("Skin color: " , human1.getSkin())
    



