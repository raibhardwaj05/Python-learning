from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Red")
        self.penup()
        self.xmove = 20
        self.ymove = 20
        self.goto(0,0)

    def movement(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()