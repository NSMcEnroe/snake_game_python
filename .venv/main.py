from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

player = Snake()
player.start()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    player.move()



screen.exitonclick()
