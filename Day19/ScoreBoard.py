from turtle import Turtle

Align="center"
Font=("Arial", 10, "bold")
Font1=("Arial", 15, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 268)
        self.score = 0
        self.write(f"#Score: {self.score}", align= Align, font= Font)


    def update_score(self):
        self.score += 1
        self.clear() # clears previous score from screen before writing new score
        self.write(f"#Score: {self.score}", align="center", font=("Arial", 10, "bold"))

    def game_end(self):
        self.goto(0,0)
        self.write(f"Game over\nYour Score: {self.score}", align= Align, font= Font1)
