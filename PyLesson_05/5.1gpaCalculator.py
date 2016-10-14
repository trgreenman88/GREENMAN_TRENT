print("When entering your grades please use lowercase letters.")
print("")
c1 = input("What was your letter grade for Government?")
c2 = input("What was your letter grade for Physics C?")
c3 = input("What was your letter grade for Computer Programming?")
c4 = input("What was your letter grade for Calculus CD?")
c5 = input("What was your letter grade for PE?")
c6 = input("What was your letter grade for English 12?")
c7 = input("What was your letter grade for Engineering?")

def calcPoints(grade):
    if grade == "a":
        return 4.00
    if grade == "b":
        return 3.00
    if grade == "c":
        return 2.00
    if grade == "d":
        return 1.00
    else:
        return 0.00

gPoints = float((calcPoints(c1) + calcPoints(c2) + calcPoints(c3) + calcPoints(c4) + calcPoints(c5) + calcPoints(c6) + calcPoints(c7)) / 7)
print("")
print("Your overall GPA is" , (gPoints))
    
    
    
