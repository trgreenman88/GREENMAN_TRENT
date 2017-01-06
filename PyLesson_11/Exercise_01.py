class MilesPerHour:
    def __init__(self, distance, hours, minutes):
        self.dist = distance
        self.hrs = hours
        self.mins = minutes
    mph = 0
    def modify(self, newdist, newhrs, newmins):
        self.dist = newdist
        self.hrs = newhrs
        self.mins = newmins
    def getdistance():
        return self.dist
    def gethours():
        return self.hrs
    def getminutes():
        return self.mins
    mph = dist/(hrs + (mins / 60))
def main():
    dist = float(input("Please enter a distance in miles: "))
    hrs = int(input("Please enter a time in hours: "))
    mins = int(input("Plese enter a time in minutes: "))
    mph1 = milesperhour(dist, hrs, mins)

    print("Distance: ", mph1.getdistance())
    print("Time: ", mph1.gethours(), "hours and ", mph1.getminutes()," minutes")
    print("Speed: ", mph)

    mph1.modify(newdist, newhrs, newmins)
    newdist = 10
    newhrs = 2
    newmins = 0

    print("Distance: ", mph1.getdistance())
    print("Time: ", mph1.gethours(), "hours and ", mph1.getminutes()," minutes")
    print("Speed: ", mph)
main()
    
    
    
                 
