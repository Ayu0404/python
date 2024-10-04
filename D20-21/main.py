from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen=Screen()
screen.title('Snake Game')
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 4. Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        # 5. Create a Scoreboard
        snake.extend()
        scoreboard.refresh_score()

    # 6. Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on=False
        scoreboard.game_over()

    # 7. Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            scoreboard.game_over()


screen.exitonclick()
