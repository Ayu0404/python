from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen=Screen()
screen.title('Pong Game')
screen.setup(width=900,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

left_paddle=Paddle(True)
right_paddle=Paddle(False)
ball=Ball()
scoreboard=Scoreboard()


screen.onkeypress(left_paddle.up,'w')
screen.onkeypress(left_paddle.down,'s')
screen.onkeypress(right_paddle.up,'Up')
screen.onkeypress(right_paddle.down,'Down')

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Correct Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 400:
        ball.bounce_x()
        scoreboard.right_score()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -400:
        ball.bounce_x()
        scoreboard.left_score()

    # Ball misses the right paddle
    if ball.xcor() > 420:
        ball.reset()
        scoreboard.left_score()

    # Ball misses the left paddle
    if ball.xcor() < -420:
        ball.reset()
        scoreboard.right_score()






screen.exitonclick()
