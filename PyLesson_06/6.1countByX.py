num = int(input("What number would you like to count up to?"))
interval = int(input("What interval would you like to count by?"))
output = ""

for i in range(0, num + 1, interval):
    output = output + str(i) + " "

print(output)
