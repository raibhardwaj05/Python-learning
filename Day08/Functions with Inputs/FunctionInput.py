# how to pass values in a function

name = input("Enter your name: ")
num1 = int(input("num1: "))
num2 = int(input("num2: "))


def my_function(name, num1, num2) :
    print(f"Name: {name}")
    print(f"Sum: {num1 + num2}")

my_function(name, num1, num2)

# parameter ==>> variable actual name
# argument ==>> actual value of the variable being passed

# name = "Bhardwaj" ==>> name is parameter, "Bhardwaj" is Argument