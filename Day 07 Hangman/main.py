import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("\nWelcome to hangman<3 dedicated to smelly beb")
print(hangman_art.stages[6])

chosen_word = random.choice(hangman_words.word_list)
size_of_word = len(chosen_word)
user_guesses = size_of_word * '_'
print(user_guesses)

lives = 6
previous_guesses = []

while lives > 0:
  in_the_word = ''
  position = -1
  guess = input("Guess a letter: ")
  checked = False
  if guess.isalpha() == False:
    print("That's not a letter.")
  elif guess[0] != guess[-1]:
    print("Enter only one character.")
  else:
    for letter in previous_guesses:
      if letter == guess:
        print("You've already guessed that.")
        checked = True  
    
    if checked == False:
      previous_guesses.append(guess)
      for x in chosen_word:
        position += 1
        if guess == x:
          user_guesses = user_guesses[:position] + guess + user_guesses[position+1:]
          in_the_word = True

      if in_the_word == True:
        print("You guessed the right letter!")
        print(user_guesses)
      else:
        lives -= 1
        print("You guessed the wrong letter!")
        print(hangman_art.stages[lives])
        print(user_guesses)
        in_the_word = False
        
      if user_guesses == chosen_word:
        print("You won!")
        break       
else:
  print(f"You lost. The word was: {chosen_word}")
