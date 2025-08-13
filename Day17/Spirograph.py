import random
import turtle as t

tr = t.Turtle()
tr.speed("fastest")
t.colormode(255)

def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for _ in range(int(360 / 10)):
    tr.color(colors())
    tr.circle(100)  # radius = 100
    cur_head = tr.heading()
    tr.setheading(cur_head + 10)


s = t.Screen()
s.exitonclick()
