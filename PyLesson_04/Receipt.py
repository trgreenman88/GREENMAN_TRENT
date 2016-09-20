print("menu:\n$6.00-Cheeseburger   \t$4.00-Hot Dog\t$12.00-Steak\n$12.00-Babyback Ribs   \t$2.00-Fries    \t$1.00-Coleslaw\n$2.00-Milkshakes     \t$1.00-Soda     \t$2.00-Ice Cream")


def format(item, price):
      print("{:-<40} \t {:<40}". format(item,price))

#input item1

item1 = input("What would you like to order first?")
print("Yummmmm..." + item1 + " is my favorite")
price1 = float(input("Please enter the price of your first item"))

#input item2

item2 = input("What would you like to go with your first choice?")
price2 = float(input("Please enter the price of your second item"))

#input item3

item3 = input("What would you like to finish your order with?")
print("Wow, that all sounds very delicious")
price3 = float(input("Please enter the price of your final item."))

#calculate subtotal
subtotal = (price1 + price2 + price3)
tax = (subtotal * 0.08)
total = (tax + subtotal)
print("======================RECEIPT======================")

format(item1, price1)
format(item2, price2)
format(item3, price3)
#same thing for tax and toatal
print("Subtotal--------------------------------\t" , subtotal)
print("Tax-------------------------------------\t" , tax)
print("Total-----------------------------------\t" , total)
print("______________________________________________________")
print("Thank you for choosing Greenman's Diner :-)")
