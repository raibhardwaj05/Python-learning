# Calculator based on user demanded operation

def Calculate(a, b, operator):
    """performs basic mathematical operation"""
    match operator:
        case "+":
            return a+b

        case "-":
            return a-b

        case "*":
            return a*b

        case "/":
            return a/b

        case _:
            return "Invalid Operator"

while True: # always true ==>> infinite loop

    a = float(input("What's the first number?: "))
    operator = input("+\n-\n*\n/\nPick an operation: ")
    b = float(input("What's the next number?: "))

    solve = Calculate(a, b, operator)

    print(f"{a} {operator} {b} = {solve}")

    while True:
        loop = input(f"Type 'y' to continue calculating with {solve}, or 'n' to start new calculation or 'q' to quit: ")

        if loop == "y":
            operator = input("+\n-\n*\n/\nPick an operation: ")
            b = float(input("What's the next number?: "))
            old_solve = solve

            solve = Calculate(old_solve, b, operator)

            print(f"{old_solve} {operator} {b} = {solve}")

        elif loop == "n":
            break

        elif loop == "q":
            print("Exiting the calculator!")
            exit()

        else:
            print("Invalid Input")
