print("This program will help you to find the average of 3 numbers")
num1 = float(input("What is your first number?"))
num2 = float(input("What is your second number?"))
num3 = float(input("What is your third number?"))
avg = 0

def setNums():
    global num1, num2, num3
    num1 = num1
    num2 = num2
    num3 = num3
    
def findAvg():
    global avg
    avg = (num1 + num2 + num3) / 3

setNums()
findAvg()

print("The average of" , num1, "," , num2, ", and" , num3, "is" , "{:00.5f}".format(avg) , ".")

