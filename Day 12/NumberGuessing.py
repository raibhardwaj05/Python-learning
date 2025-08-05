import random

NoOfGuess = 0
game = True

while game:
    n = random.randint(1, 10)
    g = int(input("guess the number: "))

    if g == n:
        print(f"right guess\nnumber of guess: {NoOfGuess}")
        game = False
    elif g > n:
        print("wrong guess try lower")
    elif n > g:
        print("try higher ")

    NoOfGuess = NoOfGuess + 1


