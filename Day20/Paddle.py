from turtle import Turtle

class CreatePaddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1) # default wid = 20 & len = 20
        self.speed(0)
        self.penup()
        self.goto(xpos, ypos)

    def go_up(self):
        if self.ycor() < 250:
            new_pos = self.ycor() + 40
            self.goto(self.xcor(), new_pos)

    def go_down(self):
        if self.ycor() > -250:
            new_pos = self.ycor() - 40
            self.goto(self.xcor(), new_pos)