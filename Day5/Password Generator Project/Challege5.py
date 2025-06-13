# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(']

print("Welcome to the PyPassword Generator!")

no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like in your password?\n"))

# easy level password ==>> letters, symbols, numbers together
password = ""

# for letters
for i in range(1, no_letters+1):
    # random.choice() to pick a random element from a list in Python.
    letter = random.choice(letters)
    print(letter)

    # storing data to the variable
    password += letter

# for symbols
for i in range(1, no_symbols + 1):
    # random.choice() to pick a random element from a list in Python.
    symbol = random.choice(symbols)
    print(symbol)

    # storing data to the variable
    password += symbol


# for symbols
for i in range(1, no_numbers + 1):
    # random.choice() to pick a random element from a list in Python.
    number = random.choice(numbers)
    print(number)

    # storing data to the variable
    password += number

print("Your Password: ", password)

