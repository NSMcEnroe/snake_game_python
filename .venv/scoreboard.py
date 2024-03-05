from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.speed("fastest")
        self.color("white")
        self.write(f"Score = {self.points}", align = "center", font = ("Arial", 16, "normal"))

    def gain_points(self):
        self.clear()
        self.points += 1
        self.write(f"Score = {self.points}", align = "center", font = ("Arial", 16, "normal"))