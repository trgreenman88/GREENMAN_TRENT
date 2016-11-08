num = int(input("Please enter a number: "))
def luck(num):
    if num > 0:
        if int((num % 10)) == 7:
            return int((luck(num/10) + 1 + luck(num)))
        else:
            return (int(0 + luck(num/10)))
    else:
          print("0")
luck(num)
              
              
          
          
    
          
    
