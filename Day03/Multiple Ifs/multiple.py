height = int(input("Height in cm: "))
bill = 0

if height >= 120:
    age = int(input("Your Age: "))
    if age <= 12:
        print("pay $5 for the ticket")
        bill = 5
    elif age >= 18:
        print("pay $12 for the ticket")
        bill = 12
    elif 12 < age < 18:
        print("pay $7 for the ticket")
        bill = 7

    photos = input("Want photos? y(yes) n(no): ")
    if photos == "yes":
        print(f"total bill = ${bill + 3}")
    else:
        print(f"Total bill = ${bill}")
else:
    print("Not eligible for the ride")
