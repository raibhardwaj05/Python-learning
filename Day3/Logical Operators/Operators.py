height = int(input("Height in cm: "))
bill = 0

if height >= 120:
    age = int(input("Your Age: "))
    if age <= 12:
        print("pay $5 for the ticket")
        bill = 5
    elif age >= 45 and age <= 55:
        print("pay $0 for ticket")
        bill = 0
    elif age >= 18:
        print("pay $12 for the ticket")
        bill = 12
    elif age > 12 and age < 18:
        print("pay $7 for the ticket")
        bill = 7
    elif age >= 45 and age <= 55:
        print("pay $0 for ticket")
        bill = 0

    photos = input("Want photos? y(yes) n(no): ")
    if photos == "yes":
        print(f"total bill = ${bill + 3}")
    else:
        print(f"Total bill = ${bill}")
else:
    print("Not eligible for the ride")
