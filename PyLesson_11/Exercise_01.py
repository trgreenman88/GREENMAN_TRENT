class MilesPerHour:
    def __init__(self, distance, hours, minutes):
        self.dist = distance
        self.hrs = hours
        self.mins = minutes
    mph = 0
    def setDist(self, newdist):
        self.dist = newdist
    def setHrs(self, newhrs):
        self.hrs = newhrs
    def setMins(self, newmins):
        self.mins = newmins

    def getdistance(self):
        return self.dist
    def gethours(self):
        return self.hrs
    def getminutes(self):
        return self.mins
    def getMPH(self):
        mph = self.dist/(self.hrs + (self.mins / 60))
        return mph
def main():
    dist = float(input("Please enter a distance in miles: "))
    hrs = int(input("Please enter a time in hours: "))
    mins = int(input("Plese enter a time in minutes: "))

    mph1 = MilesPerHour(dist, hrs, mins)

    print("Distance: ", mph1.getdistance())
    print("Time: ", mph1.gethours(), "hours and ", mph1.getminutes()," minutes")
    print("Speed: ", mph1.getMPH())

    mph1.setDist(10)
    mph1.setHrs(2)
    mph1.setMins(0)

    print("Distance: ", mph1.getdistance())
    print("Time: ", mph1.gethours(), "hours and ", mph1.getminutes()," minutes")
    print("Speed: ", mph1.getMPH())
main()
    
    
    
                 
