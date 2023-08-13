#
#   Jeremi Torój 13.08.2023
#

from turtle import Turtle
from time import sleep
from random import choice
directions = [-2, 2]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(400, 300)
        self.x_move = choice(directions)
        self.y_move = choice(directions)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        sleep(0.01)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move > 0:
            self.x_move += 0.2
            self.y_move += 0.2
        else:
            self.x_move -= 0.2
            self.y_move -= 0.2

    def collision_ceiling_floor(self):
        if self.ycor() > 595 or self.ycor() < 5:
            self.bounce_y()

    def collision_paddle(self, paddle):
        if self.xcor() > 740 and self.distance(paddle) < 50\
                or self.xcor() < 60 and self.distance(paddle) < 50:
            self.bounce_x()

    def reset_position(self):
        self.goto(400, 300)
        self.bounce_x()
        if self.x_move > 0:
            self.x_move = 3
            self.y_move = 3
        else:
            self.x_move = -3
            self.y_move = -3
