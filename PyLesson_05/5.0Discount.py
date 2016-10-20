print("Items and Prices:")
print("Macbook Pro \t $500.00 \t iDrone           \t $1000.00 \t iProjector       \t $250.00")
print("iMouse      \t $50.00  \t Headset          \t $150.00  \t Monitor          \t $400.00")
print("iPhone      \t $750.00 \t Wireless Earbuds \t $1500.00 \t iCell Tower Mini \t $5000.00") 
print("")
print("Please exclude all dollar signs when entering your prices")
print("")

item1 = input("What is your first item?")
p1 = float(input("What is the price of that item"))
item2 = input("What is your second item?")
p2 = float(input("What is the price of your second item?"))
item3 = input("What is your third item?")
p3 = float(input("What is the price of your third item?"))
item4 = input("What is your fourth item?")
p4 = float(input("What is the price of your fourth item?"))

subtotal = (p1 + p2 + p3 + p4)
discount = subtotal * 0.15

print("<<<<<<<<<<<<<<<<<<Receipt>>>>>>>>>>>>>>>>>>")

def format(item, price):
    print("{:=<30} \t {:<30}". format(item,price))
format(item1, p1)
format(item2, p2)
format(item3, p3)
format(item4, p4)
print("Subtotal======================\t" , subtotal)

if subtotal >= 2000:
    print("Discount======================\t" , discount)
    print("Total=========================\t" , subtotal - discount)

if not subtotal >= 2000:
    print("Discount======================\t 0.0")
    print("Total=========================\t" , subtotal)
    
    
