class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.income = 0

    # check for available resources
    def report(self):
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nIncome: ${self.income:.2f}")

    # money conversion
    def totalmoney(self, penny, nickel, dime, quarter):
        total = (penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25)
        return total

    # type of coffee you want
    def wish(self, need):
        self.need = need
        w = m = c = cost = 0
        match self.need:
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
                print("Sorry, wrong input!")
                return None

        return w, m, c, cost

    # check and process the order
    def condition(self, amount, cost, w, m, c, need):
        if self.water < w or self.milk < m or self.coffee < c:
            print("Sorry, not enough resources!")

        if amount < cost:
            print(f"Insufficient money inserted\nRefunding: ${amount:.2f}")

        else:
            change = amount - cost
            print(f"Enjoy your {need}!\nYour change: ${change:.2f}")
            # update resources
            self.water -= w
            self.milk -= m
            self.coffee -= c
            self.income += cost

