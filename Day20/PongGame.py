from turtle import Screen
from Paddle import CreatePaddle
from Ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("PING_PONG")
screen.bgcolor("black")
screen.tracer(0)

rPaddle = CreatePaddle(350, 0)
lPaddle = CreatePaddle(-350, 0)

screen.listen()
screen.onkey(key="Up", fun = rPaddle.go_up)
screen.onkey(key="Down", fun = rPaddle.go_down)

screen.onkey(key="w", fun = lPaddle.go_up)
screen.onkey(key="s", fun = lPaddle.go_down)

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.movement()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detest miss
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()

    # contact with left or right paddle
    if ball.distance(lPaddle) < 50 and ball.xcor() < -320 or ball.distance(rPaddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

screen.exitonclick()