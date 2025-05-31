# if condition:
#   do A
# elif condition:
#   do B
# else:
#   do this

age = int(input("Age: "))

if age < 18:
    print("Teenager")
elif age >= 18 and age <= 60:  # Or ==>> 18 <= age <= 60
    print("Adult")
else:
    print("Senior citizen")

# in python && = and (keyword)