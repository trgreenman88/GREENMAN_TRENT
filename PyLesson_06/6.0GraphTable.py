integer = int(input("Please enter a whole number"))
size = int(input("Please enter a whole number to determine the size of your table"))

for i in range(1, size):
    print("{:=^10}".format(i * integer))
    
