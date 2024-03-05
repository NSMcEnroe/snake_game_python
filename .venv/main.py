from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

player = Snake()
food = Food()

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


screen.exitonclick()
