from turtle import Turtle

cords = [(0, 0), (-20, 0), (-40, 0)]
movement = 20

class SnakeCreate:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in cords:
            self.add_seg(position)

    def add_seg(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake.append(t)

    def extend(self):
        self.add_seg(self.snake[-1].position()) # .position() ==>> method from turtle class

    def up(self):
        # prevent reversing
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        # prevent reversing
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # prevent reversing
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # prevent reversing
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        # range(start, stop, step)
        for i in range(len(self.snake) - 1, 0, -1):
            # last block will move to the coordinates of the preceding one 3 -> 2 -> 1
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)

        self.head.forward(movement)
