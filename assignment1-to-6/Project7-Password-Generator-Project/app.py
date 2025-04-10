# Password Generator
import string
import random
import re


def generate_password(length,use_digits,use_special_char):
  characters = string.ascii_letters.lower()

  if use_digits:
    characters += string.digits

  if use_special_char:
    characters += string.punctuation

  return ''.join(random.choice(characters) for _ in range(length))


while True:
  try:
    password_num : int = int(input("Numbers of password suggestion? "))
    break
  except ValueError:
    print("❌ Only use numbers!")


while True:
  try:
    password_len : int = int(input("Password length? "))
    break
  except ValueError:
    print("❌ Only use numbers!")


while True:
    use_digits = str(input("Include digits? (y/n): ").lower())
    if use_digits in ['y','n']:
      break
    else:
      print("invalid input. Please enter 'y' or 'n' ")


while True:

    use_special_char = str(input("Include special charcters? (y/n): ").lower())
    if use_special_char  in ['y', 'n']:
      break
    else:
      print("❌ Invalid input. Please enter 'y' or 'n' ")


use_digits = use_digits == 'y'
use_special_char = use_special_char == 'y'

print("\n✅Password Generate! ")
print(20*"=")

for _ in range(password_num):
  password = generate_password(password_len,use_digits, use_special_char)
  print(password)