# Declare dictionary (assigning values)

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# finding value (retrieve data from the dictionary)
print(programming_dictionary["Bug"]) # key value is case sensitive !!

# to add data
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# to edit the existing data
programming_dictionary["Bug"] = "Programming Error."
print(programming_dictionary["Bug"])

# loops in dictionary
for key in programming_dictionary:
    print(key) # prints the key
    print(programming_dictionary[key]) # prints the value

# wipe an existing dictionary
empty_dictionary = {} # declare an empty dictionary
programming_dictionary = {} # the dictionary is now clear and wiped off
print(programming_dictionary)