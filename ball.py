from turtle import Turtle
from time import sleep


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle(visible=False)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(400, 300)
        self.ball.showturtle()
        self.ball.setheading(40)

    def move(self):
        self.ball.forward(5)
        sleep(0.01)

    def collision(self):
        if self.ball.ycor() > 595 or self.ball.ycor() < 5:
            self.ball.setheading(360 - self.ball.heading())