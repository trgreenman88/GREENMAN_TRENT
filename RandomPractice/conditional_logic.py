num = int(input("Print the number 5:"))

if num == 5:
    print("num equals 5!")

if not num == 5:
    print("num doesnt equal 5!")

word1 = input("Please enter your favorite color (all lower case letters):")
word2 = "green"

same = word1 == word2
if same:
    print("I love that color")

if not same:
    print("That color sucks")

import random

integer = random.randint(1, 2)
print(integer)

if integer == 2:
    print("Thats my favorite number")

if not integer == 2:
    print("That number is for scrubs")

one = int(input("Please enter a number:"))

even = one % 2 == 0

if even:
    print(one, "is even")

if not even:
    print(one, "is odd")
