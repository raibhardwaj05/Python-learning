from turtle import Screen
from Paddle import CreatePaddle
from Ball import Ball
import time
from Score_board import Score

# Screen Setup
screen = Screen()
screen.setup(height=600, width=800)
screen.title("PING_PONG")
screen.bgcolor("black")
screen.tracer(0)

# create paddle
rPaddle = CreatePaddle(350, 0)
lPaddle = CreatePaddle(-350, 0)

# create ball & score board
ball = Ball()
Score = Score()

# To end the game
def game_over():
    global game_is_on
    game_is_on = False
    Score.show_winner()

# give functions
screen.listen()
screen.onkey(key="Up", fun = rPaddle.go_up)
screen.onkey(key="Down", fun = rPaddle.go_down)
screen.onkey(key="w", fun = lPaddle.go_up)
screen.onkey(key="s", fun = lPaddle.go_down)

# to end the game
screen.onkey(key="q", fun= game_over)

# Game Logic
game_is_on = True
while game_is_on:
    time.sleep(0.17) # speed of the ball
    screen.update()
    ball.movement()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # contact with left or right paddle
    if ball.distance(lPaddle) < 50 and ball.xcor() < -320 or ball.distance(rPaddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detect miss on right player
    if ball.xcor() > 380:
        Score.left_increment()
        ball.reset_position()

    # detect miss on left player
    if ball.xcor() < -380:
        Score.right_increment()
        ball.reset_position()

screen.exitonclick()