# Rock Paper scissors
import random

choice = ["rock", "paper", "scissors"]

computers_choice = random.randint(0,2)

your_choice = int(input("choose:\n0.Rock\n1.Paper\n2.scissors:\n"))

if your_choice == computers_choice :
    print("Draw!")

elif ((your_choice == 0 and computers_choice == 2) or
      (your_choice == 1 and computers_choice == 0) or
      (your_choice == 2 and computers_choice == 1)):
    print("You:", choice[your_choice], "and Bot:", choice[computers_choice])
    print("You Won!")

elif ((your_choice == 2 and computers_choice == 0) or
      (your_choice == 0 and computers_choice == 1) or
      (your_choice == 1 and computers_choice == 2)):
    print("You:", choice[your_choice], "and Bot:", choice[computers_choice])
    print("You Loose")

else :
    print("Invalid Input!")