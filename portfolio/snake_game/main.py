from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# set up of screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Erica's Snake Game")
screen.tracer(0)  # to resolve choppy movement of snake

# create the snake
snake = Snake()
# create the food
food = Food()
# create the scoreboard
scoreboard = Scoreboard()
# control movement with keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # shows smooth movement of snake
    time.sleep(0.1)  # adds delay before screen updates
    snake.move()  # move the snake forward

    # detect collision with food using distance method from turtle class
    if snake.head.distance(food) < 15:  # this took some doing to figure out good distance
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    #detect collision with tail
    for segment in snake.segments[1:]: # skip the first segment in list because that's the head
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
