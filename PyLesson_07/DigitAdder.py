print("This will help you to find the sum of each of the digits in a number")
number = int(input("Please enter a number: "))
add = 0
num = number
def sumDigits():
    while num > 0:
        add += 1
        num = int(num / 10)
sumDigits()
print("The sum of the digits in " , number, " is" , add)

