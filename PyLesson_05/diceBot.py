import random
play = random.randint(1,6)
comp = random.randint(1,6)

print("You rolled a" , play)
print("Dice Bot rolled a" , comp)

if play > comp:
    print("You win!")
    

if play < comp:
    print("You lose :-(")

if play == comp:
    print("Its a draw")

