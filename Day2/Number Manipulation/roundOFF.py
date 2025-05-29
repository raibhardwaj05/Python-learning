b = 84 / (1.65 ** 2) # == 30.85399449035813

print(b)

# Casting removes deciamls ==>> 3.9 ko 3 kar dega even though it's close to 4
print(int(b)) # == 30

# round() ==>> Round Off 3.9 to 4
print(round(b)) # == 31

# decimal place < 0.5 ==>> same number (3.4 == 3)
print(round(3.4))
# decimal place >= 0.5 ==>> same number (3.7 == 4)
print(round(3.5))

# Round OFF to specific decimal places ==>> round(number, n decimal places)
print(round(b, 3)) # == 30.854
