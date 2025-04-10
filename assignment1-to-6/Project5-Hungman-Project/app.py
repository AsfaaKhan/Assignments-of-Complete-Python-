
#Hangman Game
import random
import string

#  Words list from https://www.randomlists.com/data/words.json
word_list = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act","action","activity","actor","actually","ad hoc","adamant","adaptable","add","addicted","addition","adhesive","adjoining","adjustment","admire","admit","adorable","adventurous","advertisement","advice","advise","afford","afraid","aftermath","afternoon","afterthought","aggressive","agonizing","agree","agreeable","agreement","ahead","air","airplane","airport","ajar","alarm","alcoholic","alert","alike","alive","alleged","allow","alluring","aloof","amazing","ambiguous","ambitious","amount","amuck","amuse"]

def get_val_word(words):
  word = random.choice(word_list)  #randomly chooses something from the list of words
  while '-' in word:
    word = random.choice(words)
  return word

def hungman():
  word = get_val_word(word_list).upper()
  word_letters = set(word) # letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() # what the user has guessed

  lives = 15

  #getting user input
  while len(word_letters) > 0 and lives > 0:
    # Letters used
    # ' '.join (['a','b', 'cd']) --> 'a b cd'
    print(f"You have {lives} lives left and you have used these letters already: ", " ".join(used_letters))

    # what current word is (ie W - R D )
    display_word = [letter if letter in used_letters else '-' for letter in word]
    print("Current Word : ", ' '.join(display_word))

    user_letter = input ("Guess a letter:").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print("✅ Good guess!")
      else:
        lives = lives - 1 # takes away a life if wrong
        print("❌ Wrong guess.")

    elif  user_letter in used_letters:
      print("⚠️You have already used that letter. Please try again.")
    else:
      print("❌Invalid character. Please try again! ")

  if lives == 0:
    print(f"You die! ⚠️sorry. The Word was {word}")

  # Get here when len(word_letter) == 0
  print(f"\n🎉 Congratulations! You guessed the word: {word}")

hungman()