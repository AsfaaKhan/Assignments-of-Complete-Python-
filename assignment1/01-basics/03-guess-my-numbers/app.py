# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random 


def main():
    secret_number : int = random.randint(1,20)
    print("I am Thinking of a number between 1 and 20...")

    # Get user's guess
    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess < secret_number :
            print("Your guess is too low")
        else: 
            print("Your guess is too high")
        print()
        guess : int = int(input("Enter a new guess: ")) 
    print(f"Congratulations! You guess the correct number '{str(secret_number)}'")       

if __name__ == "__main__":
    main()