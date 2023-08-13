from turtle import Turtle
from time import sleep


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(400, 300)
        self.x_move = 2
        self.y_move = 2
        self.setheading(40)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        if new_x > 795 or new_x < 5:
            return
        self.goto(new_x, new_y)
        sleep(0.01)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def collision_ceiling_floor(self):
        if self.ycor() > 595 or self.ycor() < 5:
            self.bounce_y()

    def collision_paddle(self, paddle):
        if self.xcor() > 740 and self.distance(paddle) < 50\
                or self.xcor() < 60 and self.distance(paddle) < 50:
            self.bounce_x()
