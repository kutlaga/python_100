import random
import hangman_word_list
import hangman_art

# initial setup
word_list = hangman_word_list.word_list
word_list_len = len(word_list)
lives = 6
stages = hangman_art.stages
print(hangman_art.logo)

# choose a random word
rand_index = random.randint(0, word_list_len - 1)
chosen_word = word_list[rand_index]
chosen_word_progress = ['_'] * len(chosen_word)

# game loop
while(lives > 0):
  # prompt user for a guess and check if correct
  guess = input("Please guess a leter: ").lower()
  guessed_flag = False
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
      chosen_word_progress[i] = guess
      guessed_flag = True
    else:
      if i == (len(chosen_word) - 1) and guessed_flag == False:
        lives -= 1
        if lives == 0:
          print("You lose.")
          print(f"The word was {chosen_word}.")

  print(chosen_word_progress)

  # win detection
  if '_' not in chosen_word_progress:
    print("You win.")
    break

  print(stages[lives])