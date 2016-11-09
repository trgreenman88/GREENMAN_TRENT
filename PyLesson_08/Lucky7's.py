num = int(input("Please enter a number: "))
def luck(num):
    if num > 0:
        if int((num % 10)) == 7:
            return int(1 + luck(num/10))
        else:
            return (int(0 + luck(num/10)))
    else:
        return (0)
print(luck(num))
              
              
          
          
    
          
    
