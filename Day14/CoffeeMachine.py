
water = 300
milk = 200
coffee = 100
income = 0
freetime = True

# check for available resources
def report(w, m, c, inc):
    print(f"Water: {w}ml\nMilk: {m}ml\nCoffee: {c}g\nIncome: ${inc}")

# money conversion
def totalmoney(pen, nick, dim, quart):
    return (pen * 0.01) + (nick * 0.05) + (dim * 0.10) + (quart * 0.25)

# type of coffee you want
def wish(n):
    w = m = c = cost = 0
    match n:
        case "espresso":
            w = 50
            c = 18
            cost = 1.5
        case "latte":
            w = 200
            c = 24
            m = 150
            cost = 2.5
        case "cappuccino":
            w = 250
            c = 24
            m = 100
            cost = 3
        case _:
            print("Sorry wrong input!")
            cost = 0

    return w, m, c, cost # returns a tuple

# process order
def condition(amt, coff, cost):
    if amt < cost:
        print(f"Insufficient money inserted\nRefunding:{amt}")
        return False
    else:
        change = amt - cost
        print(f"Enjoy your {coff}\nYour change: {change}")
        return True


while freetime:

    # what would customer like to have
    need = input("\nWhat would you like to have? (espresso/latte/cappuccino): ").lower()

    if need == "report":
        report(water, milk, coffee, income)
        continue

    # coffee
    wat, mil, cof, cos = wish(need)

    if water < wat or milk < mil or coffee < cof:
        print("Insufficient resource\nWe are sorry!")
        continue

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
    money = totalmoney(penny, nickel, dime, quarter)

    # get coffee
    success = condition(money, need, cos)

    if success:
        water -= wat
        milk -= mil
        coffee -= cof
        income += cos

    breaktime = input("Your Breaktime is over? Y / N: ").lower()

    if breaktime == "y":
        freetime = False
        print("Machine turned off. Have a good day!")


