from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.setworldcoordinates(0, 0, 800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


player_left = Paddle(50)
player_right = Paddle(750)
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


screen.exitonclick()
