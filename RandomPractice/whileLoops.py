number = int(input("Please enter a number: "))
while number > 0:
    print(number % 10)
    number = int(number / 10)



num = int(input("Please enter a number: "))
digits = 0
nun = num
while nun > 0:
    digits += 1
    nun = int(nun / 10)
print("There are", digits, "digits in", num)



sentence = input("Please enter a string: ")
top = 0
while top < sentence.count(" ") > 0:
    sentence = sentence[0 : sentence.index(" ")] + sentence[sentence.index(" ")+1 : len(sentence)]
print("without spaces..." + sentence)


