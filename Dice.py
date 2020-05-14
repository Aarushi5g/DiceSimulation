import random
dice_dictionary = {
    1: '''
          _   _   _
        |           |
        |    O    |
        |_   _  _|
         ''',
    2: '''
          _   _   _
        |  O      |
        |      O  |
        |_   _  _|
         ''',
    3: '''
          _   _   _
        |O        |
        |   O     |
        |_   _O_|
         ''',
    4: '''
          _   _   _
        |O      O|
        |            |
        |O_  _O|
         ''',
    5: '''
           _   _   _
        |O      O|
        |    O     |
        |O_  _O|
         ''',
    6: '''
          _    _    _
        |O O  O |
        |O O  O |
        |O_O_O|
         '''
}


def rolling():
    dice_roll = random.randint(1, 6)
    print(dice_roll)
    print(dice_dictionary[dice_roll])


rolling()
roll_again = input("Do you wish to roll the dice again? (yes or no): ")
while roll_again.lower() == "yes":
    rolling()
    roll_again = input("Do you wish to roll the dice again? (yes or no): ")
