import os
import random
from data import data

score = 0
play = True

def formatprint(account1, account2):
    print(f"\nCompare A: {account1['name']}, a {account1['description']}")
    print("VS")
    print(f"Compare B: {account2['name']}, a {account2['description']}")

def check(account1, account2):
    return 'a' if account1['follower_count'] > account2['follower_count'] else 'b'

acc1 = random.choice(data)

while play:

    acc2 = random.choice(data)

    while acc1 == acc2:
        acc2 = random.choice(data)

    os.system('cls' if os.name == 'nt' else 'clear')

    formatprint(acc1, acc2)

    guess = input("\nGuess who will have the highest followers count 'A' or 'B': ").lower()

    answer = check(acc1, acc2)

    if answer == guess:
        score = score + 1
        print(f"You are right!\nYour Score: {score}")
    else:
        print(f"You are wrong!\nYour Score: {score}")
        play = False

    acc1 = acc2

