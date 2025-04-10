import random

def computerGuessNumber(num):
  low = 1
  high = num
  feedback = ""
  print("Let computer guess the number! ")
  while feedback != "c":
    guess = random.randint(low, high)
    feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)? ").lower()
    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1
  print(f"Hurry! The Computer gussed your number  {guess} , correctly!")

computerGuessNumber(10)