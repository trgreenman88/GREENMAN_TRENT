def amount(info):
    return(p * (1 + (r / n))**(n * t))

r = int(input("Give your interest rate in decimal form:"))
p = int(input("Give your principle cost of the loan:"))
n = int(input("Give the number of times the loan is compounded per year:"))
t = int(input("Give the life of the loan in years:"))
print("The total cost of your loan is" , amount(info), "dollars")
