import random

def guessNumber(num):
  random_number = random.randint(1, num)
  guess = 0
  while guess != random_number:
    print("Guess The Number Game (Computer)")
    guess = int(input(f"Guess a number between 1 and {num}: "))
    if guess < random_number:
      print("Oops! Sorry , guess again , Too low.")
    elif guess > random_number:
      print("Oops! Sorry , guess again , Too high.")

  print(f"Hurry! You have Guessed The Correct Number {random_number}")

guessNumber(10)