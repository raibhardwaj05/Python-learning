from turtle import Turtle

Align = "center"
Font = ("Arial", 30, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.gameborder()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(f"PL1: {self.left_score}", align=Align, font=Font)

        self.goto(100, 200)
        self.write(f"PL2: {self.right_score}", align=Align, font=Font)

    def gameborder(self):
        t = Turtle("square")
        t.shapesize(stretch_wid=5, stretch_len= 1)
        t.hideturtle()
        t.color("white")
        t.penup()
        t.goto(0,-380)
        t.setheading(90)
        while t.ycor() < 380:
            t.pendown()
            t.forward(20)
            t.penup()
            t.forward(20)

    def left_increment(self):
        self.left_score += 1
        self.clear()
        self.update_score()

    def right_increment(self):
        self.right_score += 1
        self.clear()
        self.update_score()

    def show_winner(self):
        self.goto(0,0)
        self.color("yellow")

        if self.right_score > self.left_score:
            self.write(f"Player2 Won!", align= Align, font= Font)
        elif self.right_score < self.left_score :
            self.write(f"Player1 Won!", align=Align, font=Font)
        else:
            self.write(f"Game Over!", align=Align, font=Font)
