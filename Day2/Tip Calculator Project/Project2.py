print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percent? "))
peoples = int(input("how many people to split the bill? "))

print(f"Total Bill = {bill + (bill * tip / 100)}")
print(f"Each person should pay: ${(bill + (bill * tip / 100)) / peoples}")
