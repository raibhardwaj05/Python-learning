# convert 1st letter to uppercase ==>> bhardwaj = Bhardwaj

# with in built function ==>> .capitalize() or .title()

def formatData(F_name, L_name):
    first = F_name.lower()
    last = L_name.lower()

    first = first.capitalize()
    last = last.capitalize()

    name = first + " " + last
    return name

name = formatData("BharDwaj", "RaI")
print(name)

# manually without in built function!

def formatName(f_name, l_name):
    first_letter = f_name[0].upper()  # B
    rest = f_name[1:].lower() # hardwaj
    f_name = first_letter + rest # Bhardwaj

    # Last name
    fir_letter = l_name[0].upper() # R
    remaining = l_name[1:].lower() # ai
    l_name = fir_letter + remaining # Rai

    name = f_name + " " + l_name
    return name

name = formatName("BhaRDwaj", "RAI")
print(name)

