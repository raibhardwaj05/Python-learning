# returning multiple values

def nameSurname():
    name = input("name: ")
    surname = input("Surname: ")

    return name, surname

name, surname = nameSurname()
print(f"{name} {surname}")