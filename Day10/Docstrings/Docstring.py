# tells the job of the function ===>>> """___"""

def nameSurname():
    """inputs strings and returns multiple values"""
    # docstring is immediately next line to the fuction declaration!

    name = input("name: ")
    surname = input("Surname: ")

    return name, surname # tuple[name, surname]

naam, lastname = nameSurname()
print(f"{naam} {lastname}")

