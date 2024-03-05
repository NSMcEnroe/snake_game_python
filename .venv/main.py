from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

player = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    player.move()

#Detect collision with food.
    if player.head.distance(food) < 15:
        food.refresh()
        player.extend()
        scoreboard.gain_points()
# Detect collision with wall
    if player.head.xcor() > 280 or player.head.xcor() < -280 or player.head.ycor() > 280 or player.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
# Detect collision with tail
    for segment in player.segments:
        if segment == player.head:
            pass
        elif player.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
