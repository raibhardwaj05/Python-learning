# Casting into different datatypes

x = int("12")
y = int("12")

print(x + y)

# Integer
print(int("24") + int("24"))

# String
print(str(1234))

# Floating
print(float("12345.25"))

# boolean
print(bool("True"))

# Solve print("Number of letter in your name: " + len(input("Enter your name ")))
print("Number of letter in your name: " + str(len(input("Enter your name ")))) # here str() is used to cast
print("Number of letter in your name: ", len(input("Enter your name ")))