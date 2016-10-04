print("This program will help you to find the average of 3 numbers")
num1 = float(input("What is your first number?"))
num2 = float(input("What is your second number?"))
num3 = float(input("What is your third number?"))

def setNums(num1,num2,num3):
    global number1, number2, number3
    number1 = num1
    number2 = num2
    number3 = num3

def findAvg(number1, number2, number3):
    return (number1 + number2 + number3) / 3

print("The average of" , num1, "," , num2, ", and" , num3, "is" , "{:00.5f}".format(findAvg(num1,num2,num3)) , ".")

