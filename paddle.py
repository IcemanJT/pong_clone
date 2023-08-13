#
#   Jeremi Torój 13.08.2023
#

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.y_pos = 300
        self.lives = 3
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, self.y_pos)
        self.showturtle()

    def move_up(self):
        self.y_pos += 20
        if self.y_pos > 550:
            self.y_pos = 550
        self.goto(self.xcor(), self.y_pos)

    def move_down(self):
        self.y_pos -= 20
        if self.y_pos < 50:
            self.y_pos = 50
        self.goto(self.xcor(), self.y_pos)
