nums = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]
number = 0
def gFactor(number):
    for i in range(2, number):
        if number % i == 0:
            return 1
        else:
            return 0
def removeComposites():
    for number in nums:
        if gFactor(number) == 0:
            nums.remove(number)
removeComposites()
print(nums)
    
    
