from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.y_pos = 300
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, self.y_pos)
        self.showturtle()

    def move_up(self):
        self.y_pos += 20
        self.goto(self.xcor(), self.y_pos)

    def move_down(self):
        self.y_pos -= 20
        self.goto(self.xcor(), self.y_pos)
