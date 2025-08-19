import random
import turtle as t

tur = t.Turtle()
directions = [0, 90, 180, 270]
tur.pensize(10)
tur.speed("fast")
t.colormode(255)

def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for n in range(200):
    tur.forward(30)
    tur.color(colors())
    move = random.choice(directions)
    # move = random.randint(0, 360) ==> all possible directions
    tur.setheading(move)

ms = t.Screen()
ms.exitonclick()