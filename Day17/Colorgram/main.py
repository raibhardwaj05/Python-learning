import random
import turtle as t

colors = [
    (198, 13, 32),    # dark red
    (40, 76, 188),    # blue
    (39, 216, 69),    # bright green
    (227, 159, 49),   # orange-brown
    (29, 40, 154),    # dark blue
    (212, 76, 15),    # dark orange
    (17, 153, 17),    # green
    (241, 36, 161),   # pink-magenta
    (195, 16, 12),    # deep red
    (223, 21, 120),   # magenta
    (68, 10, 31),     # maroon
    (61, 15, 8),      # very dark brown
    (11, 97, 62),     # dark teal
    (219, 159, 11),   # gold
    (54, 209, 229),   # cyan
    (19, 21, 49),     # dark navy
    (79, 74, 212),    # violet
    (10, 228, 238),   # aqua
    (73, 212, 168),   # turquoise
    (217, 88, 51)     # brick red
]

tr = t.Turtle()
tr.pensize(15)
tr.speed("fastest")
t.colormode(255)
tr.hideturtle()

tr.penup()
# tr.goto(-280,-250)
# (0,0) ==>> center
# (-x, -y) ==>> (left, down)
# (x, y) ==>> (right, up)

for n in range(168):
    tr.goto(-280, (-240 + (28 * n)))

    for _ in range(18):
        tr.dot(20, random.choice(colors))
        tr.forward(28)

        # tr.color(random.choice(colors))
        # tr.pendown()
        # tr.forward(2)
        # tr.penup()
        # tr.forward(25)


screen = t.Screen()
screen.exitonclick()