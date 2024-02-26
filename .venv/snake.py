from turtle import Turtle

class Snake:
    def __init__(self, segments = []):
        self.segments = []

    def start(self):
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.setx(-20 * i)
            self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)