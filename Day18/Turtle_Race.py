import random
from turtle import Turtle, Screen

Sc = Screen()

# creating an instance that will display the final message
writer = Turtle()
writer.hideturtle()

Sc.setup(width = 500, height = 500) # setup screen size

# taking input on the GUI screen
bet = Sc.textinput(title="Make your bet", prompt="On which turtle you want to bet?")

turtles = []
tur_color = ["red", "green", "orange", "blue", "purple"]
y_cord = [-200, -100, 0, 100, 200]

# creating multiple turtles (instances) and appending into turtles[]
for i in range(5):
    t = Turtle(shape = "turtle")
    t.color(tur_color[i])
    t.penup()
    t.goto(-230, y_cord[i])
    turtles.append(t)

is_race_on = False
if bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        # checks if the turtle has reached the right end or not
        if turtle.xcor() > 230:
            # turtle is 40X40 object ==>> 230 = 250 - 40/2

            is_race_on = False
            # pencolor() is the color of the turtle
            if bet == turtle.pencolor():
                message = f"You won\nThe {turtle.pencolor()} Wins"
            else:
                message = f"You Lose\nThe {turtle.pencolor()} Wins"

            # displays the winner message on the screen itself
            writer.write(message, align = "center", font = ("Arial", 16, "bold"))

        turtle.forward(random.randint(1, 15))

Sc.exitonclick()

# instances is the objects created from the same class with different names and attributes