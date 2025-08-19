from turtle import Turtle, Screen

tim = Turtle()
Sc = Screen()

def moveforward():
    tim.forward(10)

def movebackward():
    tim.backward(10)

Sc.listen()
Sc.onkey(key = "Right", fun=moveforward)
Sc.onkey(key = "Left", fun=movebackward)

Sc.exitonclick()