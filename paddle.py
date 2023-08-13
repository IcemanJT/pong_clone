from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.y_pos = 300
        self.paddle = Turtle(visible=False)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, self.y_pos)
        self.paddle.showturtle()

    def move_up(self):
        self.y_pos += 20
        self.paddle.goto(self.paddle.xcor(), self.y_pos)

    def move_down(self):
        self.y_pos -= 20
        self.paddle.goto(self.paddle.xcor(), self.y_pos)
