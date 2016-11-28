print("First letters...")
words = ["Fries", "Burger", "Shake", "Onion Rings", "Soda"]

def first():
    output = ""
    global words
    for word in words:
        output += word[0] + " "
    print(output)
first()








