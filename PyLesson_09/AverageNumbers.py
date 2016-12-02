import random
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, 10):
    numbers.append(random.randint(1, 100))
print(numbers[10:len(numbers)])


def average(numbers):
    avg = 0
    for i in numbers:
        avg += (i)
    return (avg / 10)
print("The average of the above numbers is... " , average(numbers))



