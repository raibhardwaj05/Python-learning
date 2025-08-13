from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.fillcolor("green")

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



my_screen = Screen()
my_screen.exitonclick()
