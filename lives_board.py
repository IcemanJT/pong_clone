#
#   Jeremi Torój 13.08.2023
#

from turtle import Turtle


class LivesBoard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.goto(x, 620)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 24, "normal"))

    def update_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 24, "normal"))
