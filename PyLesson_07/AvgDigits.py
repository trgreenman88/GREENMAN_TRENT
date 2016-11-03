number = int(input("Please enter a number: "))
digits = 0
add = 0
avg = 0
num = number
while num > 0:
    digits += 1
    add += (num % 10)
    avg = add / digits
    num = int(num / 10)
print("The average of the digits in " , number, " is" , avg)
    
