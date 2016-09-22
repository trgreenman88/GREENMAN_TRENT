def amount(hlw):
    return(0.000578704 * l * w * h)

l = float(input("What is the length of your box in inches?"))
w = float(input("What is the width of your box in inches?"))
h = float(input("What is the height of your box in inches?"))
print("The total volume of your subwoofer box is" , amount(l), "cubic feet")
