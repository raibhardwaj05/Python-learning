# Multiple Random Numbers
import random

random_list = [random.randint(1, 10) for _ in range(5)]
print(random_list)

# This runs range(n) times and collects n different numbers
# list elements may or may not be unique
# [
#     random.randint(1, 100),
#     random.randint(1, 100),
#     random.randint(1, 100),
#     random.randint(1, 100),
#     random.randint(1, 100)
# ]



# If you want only unique random numbers, you can use:
random_unique = random.sample(range(1, 10), 5)
print(random_unique)

# sample() ==>> function in python's random module
# random.sample(population, k) ====>>>> Syntax
# population: A sequence (like a list or range) to sample from.
# k: Number of unique random elements to pick.

