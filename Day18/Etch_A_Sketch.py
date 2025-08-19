from turtle import Turtle, Screen

tim = Turtle()
Sc = Screen()

def turn_right():
    h = tim.heading()
    tim.setheading(h - 10)

def turn_left():
    head = tim.heading()
    tim.setheading(head + 10)

def move():
    tim.forward(10)

def back():
    tim.backward(50)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

Sc.listen()
Sc.onkey(key = "Right", fun= turn_right)
Sc.onkey(key = "Left", fun= turn_left)
Sc.onkey(key = "Up", fun= move)
Sc.onkey(key = "Down", fun= clear)

Sc.exitonclick()