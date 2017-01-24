import random
class Object:
    def __init__(self, ItemManufacturer, ItemName, ItemCategory = "", ItemPrice = ""):
        self.IM = ItemManufacturer
        self.IN = ItemName
        self.IC = ItemCategory
        self.UPC = random.randint(1000000000, 9999999999)
        self.IP = ItemPrice

    def setIM(self, newIM):
        self.IM = newIM
    def setIN(self, newIN):
        self.IN = newIN

    def getIM(self):
        return self.IM
    def getIN(self):
        return self.IN
    def getIC(self):
        return self.IC
    def getUPC(self):
        return self.UPC
    def getIP(self):
        return self.IP
    def __str__(self):
        return "Item Info...\n Item Manufacturer: " + self.IM + "\n Item Name: " + self.IN + "\n Item Category: " + self.IC + "\n Item Price: " + self.IP + "\n UPC#: " + str(self.UPC)

def main():
    IM = input("Please enter your item manufacturer: ")
    IN = input("Please enter your item name: ")
    yorn = input("Will you be entering category and price information? (y or n) ")
    if yorn == "n":
        item1 = Object(IN, IM)
    if yorn == "y":
        IC = input("Please enter your item category: ")
        IP = input("Please enter your item price: ")
        item1 = Object(IN, IM, IC, IP)
    print(item1.__str__())
main()
                            
        
    
    
    
