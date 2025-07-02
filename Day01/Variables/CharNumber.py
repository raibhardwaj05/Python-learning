# count the number of characters entered by the user

name = input("Your Name ? ")
print(name)

# You must convert it to a string using str() to concatenate it with another string.
print("number of characters = "+ str(len(name)) )

# OR len(name) returns an int.
print("number of characters = ", (len(name)) )

# OR
length = (len(name))
print("Length = ", length)

# OR use formatted strings (f-strings):
print(f"Number of characters = {len(name)}")
