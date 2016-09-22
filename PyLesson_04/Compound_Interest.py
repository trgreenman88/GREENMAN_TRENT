def amount(rpnt):
    return(p * (1 + (r / n))**(n * t))
r = float(input("Give your interest rate in decimal form:"))
p = float(input("Give your principle cost of the loan:"))
n = float(input("Give the number of times the loan is compounded per year:"))
t = float(input("Give the life of the loan in years:"))
print("The total cost of your loan is ${:<10.2f}".format (amount(r)), "")
