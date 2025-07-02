height = int(input("Height in cm: "))

if height >= 120:
    age = int(input("Your Age: "))
    if age <= 18:
        print("pay $7 for the ticket")
    else:
        print("pay $12 for the ticket")
else:
    print("Not eligible for the ride")
