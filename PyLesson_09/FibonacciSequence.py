start = int(input("Please enter your starting number: "))
size = int(input("Please enter the length of your sequence: "))

seq = []
for i in range(0, size):
    if i == 0 or i == 1:
        seq = start
    else:
        seq = (i-1) + (i-2)
print(seq[i] + " ")
        
    
    
