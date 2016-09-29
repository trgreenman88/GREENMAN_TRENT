print("This program will help you to find the average of 3 numbers")
num1 = float(input("What is your first number?"))
num2 = float(input("What is your second number?"))
num3 = float(input("What is your third number?"))
def calcAvg():
    return (num1 + num2 + num3) / 3

print("The average of" , num1, "," , num2, ", and" , num3, "is" , "{:00.5f}".format(calcAvg()) , ".")
