def format(first, last):
    print(" * {:<30} \t {:>20} * ". format(first, last)) 
school = input("What is the name of your school?")
name1 = input("Enter your first name:")
name2 = input("Enter your last name:")
title = input("Enter your title:")
year = input("Enter the school year:")
subject = input("What is your subject?")

print("---------------------------------------------------------------")
format(name1, name2)
format(school, year)
format(title, subject)
print("---------------------------------------------------------------")
