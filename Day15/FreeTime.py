from CoffeeMachine import *

employee = CoffeeMachine()
freetime = True

while freetime:

    # what would customer like to have
    need = input("\nWhat would you like to have? (espresso/latte/cappuccino): ").lower()

    if need == "report":
        employee.report()
        continue

    # coffee
    wat, mil, cof, cos = employee.wish(need)

    if cos == 0:
        print("Invalid coffee")
        continue

    # to payment
    print("Amount to be paid in penny, dime, nickel or quarter")
    penny = int(input("Penny?: "))
    dime = int(input("dime?: "))
    nickel = int(input("nickel?: "))
    quarter = int(input("quarter?: "))

    # money conversion
    money = employee.totalmoney(penny, nickel, dime, quarter)

    # get coffee
    employee.condition(money, cos, wat, mil, cof, need)

    breaktime = input("Your Breaktime is over? Y / N: ").lower()

    if breaktime == "y":
        freetime = False
        print("Machine turned off. Have a good day!")

