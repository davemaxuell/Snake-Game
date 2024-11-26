from turtle import Turtle, Screen
from snake_logic import Snake
from food import Food
from scoreboard import Scoreboard
from outline import Outline
from game_over import Gameover

import random
import time
screen = Screen()
outline = Outline()

screen.setup(650, 650)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def blink():
    screen = Screen()
    for segments in snake.snake_part:
        if segments.isvisible():
            segments.hideturtle()
        else:
            segments.showturtle()
    screen.ontimer(blink, 200)

screen.listen()
screen.onkey(snake.upwards, "Up")
screen.onkey(snake.downwards, "Down")
screen.onkey(snake.rightwards, "Right")
screen.onkey(snake.leftwards, "Left")

game_go = True
while game_go:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.go == False:
        game_go = False
        gameover = Gameover()
        blink()

    if snake.head.distance(food) < 15:
        food.eaten()
        scoreboard.update()
        snake.make_new()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_go = False
        gameover = Gameover()
        blink()
        
screen.exitonclick()