# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

# Solution:
import random

NUMBERS_SIDES = 6

def main():

    # Roll die
    die1 : int = random.randint(1,NUMBERS_SIDES)
    die2 : int = random.randint(1, NUMBERS_SIDES)

    # Get Their Total:
    total : int = die1 + die2

    # Print out the result 
    print(f"Dice have {NUMBERS_SIDES} sides each.")
    print(f"First Die: {die1} ")
    print(f"Second Die: {die2} ")
    print(f"Total of two dice : {total}")

if __name__ == '__main__':
    main()