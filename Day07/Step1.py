import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable
chosen_word = random.choice(word_list)

print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess
guess = []

letter = input("guess a letter: ").lower()

guess.append(letter)
print(guess)

# Check if the letter the user guessed(guess) is one of the letter in the chosen_word
if letter in chosen_word:
    print("right")
else:
    print("wrong")