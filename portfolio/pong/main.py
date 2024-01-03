from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# set up of screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Erica's Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() <-320:
        ball.paddle_bounce()

    # detect miss by right paddle
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_point()

    # detect miss by left paddle
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()