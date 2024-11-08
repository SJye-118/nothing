testing = ("hello world")

print(testing)

import random

def roll_dice():
    return [random.randrange(1,7)for _ in range(3)]

def get_total(rolls):
    return sum (rolls)

def print (rools,owner):
    print (f"{owner}'s number : ", rools )
    print (f"{owner}'s total : ", get_total(rools))

print ("hello user from earth")
age= input ("whats your age")
if int (age)> 18 :
    print("you are an adult")
else:
    print("you are dumb")

while True:
    # Roll for user
    user_rolls = roll_dice()
    print(user_rolls, "Your")
    
    # Roll for computer
    computer_rolls = roll_dice()
    print(computer_rolls, "My")

    # Determine winner
    if get_total(user_rolls) > get_total(computer_rolls):
        print("You win!")
    elif get_total(user_rolls) < get_total(computer_rolls):
        print("I win!")
    else:
        print("It's a tie!")

    # Ask if the user wants to play again
    play_again = input("Enter 'g' to roll again or any other key to exit: ")
    if play_again.lower() != 'g':
        break

print("Thanks for playing!")