import random
from itertools import count

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable
chosen_word = random.choice(word_list)

print(chosen_word)

# Create an empty String called placeholder
placeholder_list = []
place = len(chosen_word)
placeholder = ""

for holders in range(0, place):
    placeholder_list.append("_")
    placeholder = ''.join(placeholder_list)

print(placeholder)

# OR
placeholders = "_" * place
print(placeholders)

# Guess letter if correct display at the correct position

# Ask the user to guess a letter and assign their answer to a variable called guess
guess = []

game_over = False

while not game_over:
    letter = input("guess a letter: ").lower()

    if letter in guess:
        print("You have already guessed the letter")
    else:
        guess.append(letter)

    # Check if the letter the user guessed(guess) is one of the letter in the chosen_word
    for index, char in enumerate(chosen_word):
        if char == letter:
            placeholder_list[index] = letter

    placeholders = ''.join(placeholder_list)
    print(placeholders)

    if "_" not in placeholders:
        game_over = True
        print("You Won!")