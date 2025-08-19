from turtle import Screen
import time
from Snake import SnakeCreate
from Food import Food
from ScoreBoard import ScoreBoard

# set the screen environment for the game
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # this turns off the animation until its updated (update())

game_is_on = True

snake = SnakeCreate()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    # once the snake is created and changes its position on screen ===>> it updates on the screen
    screen.update()

    # this slows down the movement of the snake
    time.sleep(0.1)

    # calls move function fron SnakeCreate class in Snake file
    snake.move()

    # detect collision of food
    if snake.head.distance(food) < 20:
        food.refresh()
        score.update_score()
        snake.extend()

    # detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        score.game_end()
        game_is_on = False

    # detect collision with tail
    for segment in snake.snake[1:]:
        # snake[start: (whatever be the length)]
        if snake.head.distance(segment) < 10:
            score.game_end()
            game_is_on = False


screen.exitonclick()