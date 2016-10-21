print("You will be given 3 choices to go on your adventure and you will need to find the rigt order to succeed.")
print("choice1 is Go through the woods")
print("choice2 is Go to Grandma's house")
print("choice3 is go over the river")
def Adventure():
    choice = input("What would you like to do first?")
    if choice == "choice3" or "choice2" or "choice1":
        if choice == "choice3":
            print("Nicely done!")
        else:
            print("Not quite. Try another path")
            Adventure()
Adventure()


def SecondStep():
    choice = input("What would you like to do next?")
    if choice == "choice3" or "choice2" or "choice1":
        if choice == "choice1":
            print("Geat job!")
        else:
            print("Not quite. Try another path")
            SecondStep()
SecondStep()

def LastStep():
    choice = input("What would you like to do to finish your journey?")
    if choice == "choice3" or "choice2" or "choice1":
        if choice == "choice2":
            print("YAAAAAAAAAY!!! YOU SUCCESSCULLY COMPLETED YOUR JOURNEY!!! YOU WIN!!!")
        else:
            print("Not quite. Try another path")
            LastStep()
LastStep()

        
    
            
            
            
