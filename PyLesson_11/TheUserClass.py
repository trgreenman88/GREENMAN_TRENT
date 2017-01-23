import random
class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)

    def setAvatar(self, newAvat):
        self.avatar = newAvat
        
    def getfirstName(self):
        return self.firstName
    def getlastName(self):
        return self.lastName
    def getavatar(self):
        return self.avatar
    def getuserID(self):
        return self.userID

def main():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    yorn = input("Would you like to use a public avatar? (y or n)")
    if yorn == "n":
        user1 = User(firstName, lastName)
    if yorn == "y":
        avatar = input("Please enter your avatar name: ")
        user1 = User(firstName, lastName, avatar)

    def __str__(self):
        return "Customer Info...\n First Name: " + self.firstName + "\n Last Name: " + self.lastName + "\n Avatar: " + self.avatar + "\n User ID#: " + str(self.userID)
main()
        
    
    
    
                
