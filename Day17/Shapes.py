import math
from turtle import Turtle, Screen

t = Turtle()
colors = ["red", "green", "blue", "black", "purple", "peru", "maroon", "DarkCyan"]
i = 0

for n in range(3, 11):
    angle = 360 / n
    t.color(colors[i])

    for i in range(n):

        t.forward(85)
        t.right(angle)

    i += 1

s = Screen()
s.exitonclick()
