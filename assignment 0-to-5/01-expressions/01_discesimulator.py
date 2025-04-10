# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.


import random

# Numbers if sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and print their result
    """
    die1 : int = random.randint(1,NUM_SIDES)
    print("1st die roll: ",die1)
    die2 : int = random.randint(1,NUM_SIDES)
    print("2nd die roll",die2)
    total : int = die1 + die2
    print(f"Total of Two Dice : {total}")
    print("\n")


def main():
    die1 : int = 10
    print("die1 in main() starts as: ", str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: ", str(die1))

    


if __name__ == '__main__':
    main()    