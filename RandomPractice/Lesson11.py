class UserNames:
    #Constructor
    def __init__(self, fname, lname, uname):
        self.firstName = fname
        self.lastName = lname
        self.userName = uname

    #Modifier
    def setUserName(self, newUser):
        self.userName = newUser

    #Accessor
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getUserName(self):
        return self.userName

def main():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    userName = input("Please enter your desired user name: ")

    #instantiate an object
    user1 = UserNames(firstName, lastName, userName)

    print("<<<<<<<<<<<<<<< USER INFO >>>>>>>>>>>>>>>")
    print("Name: ", user1.getFirstName(), " ", user1.getLastName())
    print("User Name: ", user1.getUserName(),"\n\n")

    user1.setUserName("Mr. Bigglesworth")

    print("<<<<<<<<<<<<<<< USER INFO >>>>>>>>>>>>>>>")
    print("Name: ", user1.getFirstName(), " ", user1.getLastName())
    print("User Name: ", user1.getUserName(),"\n\n")

main()
    
    
        
