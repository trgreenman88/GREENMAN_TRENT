import random
numbers = []
for i in range(0, 10):
    numbers.append(random.randint(0, 100))
print(numbers)

output = ""
for i in numbers:
    output += str(i) + " "
print(output)
print("")
def average(numbers):
    avg = 0
    for i in numbers:
        avg += output
        return avg / 10
print("The average or the above numbers is... " + average(numbers))



