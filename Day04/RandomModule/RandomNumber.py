import random
import my_module # Calling the module

# generate random integer ==>> a<= num <=b
random_integer = random.randint(1, 10)
print(random_integer)

# floating point random number ===>>> a<= num <b
random_float = round((random.random() * 10), 2)
print(random_float)

# to generate a floating number between any range
random_range = round(random.uniform(3.0, 3.6), 2)
print(random_range)

if my_module.my_Fav_No == random_range :
    print("Number Matched!!!!!!")


print(my_module.my_Fav_No)