# Hangman Game
import random

words = ["apple", "grape", "mango", "peach", "lemon"]

word = random.choice(words) # Correct word

chance = 6 # Chances to save the hangman

Guess = "_____" # guess 5 letters
word_list = list(Guess)

guess_list = [] # stores all the guess (correct, incorrect both)

print("Word: ", Guess)

# loops until number of chance is not 0 and there is no '_' in the guess variable
while chance > 0 and "_" in word_list:
    letter = input("Guess The Letters in the name of the fruit: ").lower()

    # checks whether the guessed letter is already guessed and repeated or not
    if letter in guess_list:
        print("You have already guessed that letter!")
        continue

    # adds every guess to the guess_list
    guess_list.append(letter)

    # if the letter entered is present in the word
    if letter in word:
        # Find all occurrences (all positions) ==>> enumerate():
        for index, char in enumerate(word):
            # if any char of the word matches the letter
            # then word_list is updated to that position
            if char == letter:
                word_list[index] = letter
        print("Correct Guess!")
        # converts the word_list into a word
        Guess = ''.join(word_list)
        print(Guess)

    else:
        chance -= 1
        print("Wrong Guess! Chance:", chance)


if '_' not in Guess:
    print("Congrats You Won!")
else:
    print("Oops! You Lose")
