def passCheck():
    u = input("What is your username?")
    p = input("What is your password?")
    
    if u == "greenmant" and p == "password":
        print("You are granted access!")
    else:
        if u == "greenmant" or p == "password":
            if not p == "password":
                print("Your password is incorrect")
                passCheck()
            if not u == "greenmant":
                print("Your username is incorrect")
                passCheck()
            else:
                print("Your username and password are both incorrect")
                passCheck()
passCheck()

        
    
    
    
