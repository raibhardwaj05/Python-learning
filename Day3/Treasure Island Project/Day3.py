# https://ascii.co.uk/art
# use print('''_''') for multiple line print statement

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? left or right: ")

if direction == "left":
    print("You reached a lake. There is an island in the middle of the lake.")

    decide = input("Type 'wait' to wait for the boat. Type 'swin' to swim across: ")

    if decide == "wait":
        print("You Reached a hall with three doors.")

        door = input("Which door you want to enter 'red', 'yellow' or 'blue': ")

        if door == "yellow":
            print("You Won!")
        elif door == "red":
            print("Burned by fire.\nGame Over!")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over!")
else:
    print("You fell into a hole.\nGame Over!")