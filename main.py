#
#   Jeremi Torój 13.08.2023
#

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from lives_board import LivesBoard

screen = Screen()
screen.setup(width=800, height=700)
screen.setworldcoordinates(0, 0, 800, 700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# grid of a pong game
grid = Turtle(visible=False)
grid.pensize(3)
grid.speed("fastest")
grid.color("white")
grid.goto(0, 600)
grid.goto(800, 600)
grid.goto(800, 0)
grid.goto(0, 0)


# player handlers and ball object
player_left = Paddle(50)
player_right = Paddle(750)
right_lives = LivesBoard(700)
left_lives = LivesBoard(100)
ball_obj = Ball()
screen.onkey(player_left.move_up, "w")
screen.onkey(player_left.move_down, "s")
screen.onkey(player_right.move_up, "Up")
screen.onkey(player_right.move_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    ball_obj.move()
    ball_obj.collision_ceiling_floor()
    ball_obj.collision_paddle(player_left)
    ball_obj.collision_paddle(player_right)
    if ball_obj.xcor() > 800:
        ball_obj.reset_position()
        right_lives.lives -= 1
        right_lives.update_lives()
    elif ball_obj.xcor() < 0:
        ball_obj.reset_position()
        left_lives.lives -= 1
        left_lives.update_lives()
    if right_lives.lives == 0:
        game_is_on = False
        grid.goto(400, 300)
        grid.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        grid.goto(400, 250)
        grid.write("Left player wins!", align="center", font=("Courier", 24, "normal"))
    elif left_lives.lives == 0:
        game_is_on = False
        grid.goto(400, 300)
        grid.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        grid.goto(400, 250)
        grid.write("Right player wins!", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
