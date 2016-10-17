h = float(input("What is your height in inches?"))
w = float(input("What is your weight in pounds?"))

BMI = float((703 * w) / (h * h))

print("Your BMI is" , BMI)
if BMI <= 18.5:
    print("Condition is Underweight")
elif BMI <= 24.9:
    print("Condition is Normal")
elif BMI <= 29.9:
    print("Condition is Overweight")
elif BMI <= 34.9:
    print("Condition is Obese")
elif BMI <= 39.9:
    print("Condition is Very Obese")
else:
    print("Condition is Morbidly Obese")
    
