import random


def rolling():
    dice_roll = random.randint(1, 6)
    print(dice_roll)


rolling()
roll_again = input("Do you wish to roll the dice again? (yes or no): ")
while roll_again.lower() == "yes":
    rolling()
    roll_again = input("Do you wish to roll the dice again? (yes or no): ")
