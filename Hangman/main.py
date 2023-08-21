import random

import hangman_stages as hg_s
import hangman_words as hg

wordlist = hg.word_list
stages = hg_s.stages
logo = hg_s.logo

print(logo)

display = []  # list of alphabet to be displayed
guessed = []  # list for alphabet that already guessed
lives = 6  # number of player lives

# STEP 1 // Generate random words from wordlist
random_words = random.choice(wordlist)

# STEP 2 // Go through each letter in the random words. For every letter in random words, print "_"
for _ in random_words:
    display.append("_")
print(display)
print(random_words)  # For debugging purpose show the random word answer

while True:  # while loop to keep the game going until win or lose all lives

    user_guess = input("\nGuess a letter: ").lower()    # take user input (1 character only)

    if user_guess in display:
        print(f"You already guess {user_guess}")    # if user already guess the right alphabet, remind the user

    for position in range(len(random_words)):   # go through each letter position in random words
        letter = random_words[position]         # take the letter from that particular position
        if user_guess == letter:                # if the letter in that position is same to user guess
            display[position] = user_guess      # replace the list with that letter

    print(display)

    if "_" not in display:      # if there are no more underline in the list (all alphabet filled)
        print("You win")        # player win the game, finish
        break

    elif user_guess not in random_words:       # if the user guess it wrong
        if user_guess not in display:          # print the letter not in the word
            print("This letter is not in the word")
        lives -= 1                   # minus one live
        print(stages[lives])         # draw the hangman stage
        if lives == 0:               # if lives is 0, player lose
            print("You lose")
            break

