# Randon Heads OR Tails
import random

choices = ["heads", "tails"]
random_choice = random.choice(choices)

choice = input("Heads or Tails: ").lower()

if choice == random.choice:
    print("You won the TOSS!")
else:
    print(random_choice + " You lose")