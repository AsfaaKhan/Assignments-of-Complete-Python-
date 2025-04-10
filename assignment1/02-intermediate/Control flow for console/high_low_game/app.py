# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# Solution

import random

# number of rounds to play
NUM_ROUNDS = 3



def main():
    print(50*"-")
    print("Welcome  to the High-Low Game!")
    print(50*"-")

    # Initilize score
    # Milstone 5 -> track of the score
    score = 0


    # Milstone 4 -> play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)

        # Milstone 1 -> Generate random number, & print them out
        computer_num : int = random.randint(1,100)
        your_num : int = random.randint(1,100)
        print("Your Number is ", your_num)

        # Milstone 2: Get user input for their choice 
        choice : str = input("Do you think your number is higher or lower than the computer's? ")

        # Milstone 3 -> Map out all the ways to win the round
        heigher_and_correct : bool = choice == "higher" and your_num > computer_num
        lower_and_correct : bool = choice == "lower" and your_num < computer_num

        if heigher_and_correct or lower_and_correct:
            print("Your were right! The computer number was", computer_num)
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was ", computer_num)

        # Milstone 5 -> Keep track of the score
        print("Your score is now ", score)
        print()
    print("Thanks for playing! ")

if __name__ == "__main__":
    main()


