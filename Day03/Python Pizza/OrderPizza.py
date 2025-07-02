# size of pizza
# addition of personal choice
# total bill
amt = 0

size = input("Small (S)\nMedium (M)\nLarge (L)\nSize of pizza: ")
pepper = input("Do you want pepper? Yes(y) or No(n): ")
cheese = input("Do you want cheese? Yes(y) or No(n): ")

if size == "S":
    amt = 15
elif size == "M":
    amt = 20
elif size == "L":
    amt = 25
else:
    print("Wrong item")

if pepper == "y":
    amt +=3
if cheese == "y":
    amt += 1

print(f"Total bill: ${amt}")

