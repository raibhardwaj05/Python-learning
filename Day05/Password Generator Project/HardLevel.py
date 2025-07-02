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

# Hard level password ==>> letters, symbols, numbers together
password = []

# for letters
for i in range(1, no_letters+1):
    # random.choice() to pick a random element from a list in Python.
    password.append(random.choice(letters))


# for symbols
for i in range(1, no_symbols + 1):
    # random.choice() to pick a random element from a list in Python.
    password.append(random.choice(symbols))


# for symbols
for i in range(1, no_numbers + 1):
    # random.choice() to pick a random element from a list in Python.
    password.append(random.choice(numbers))


# Final password

# shuffle the list
random.shuffle(password)

# concat it into a string
my_password = ''.join(password)

print("Your Password: ", my_password)