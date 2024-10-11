import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Move the turtle with key press
timmy=Player()
screen.onkeypress(timmy.up,'Up')

car_manager=CarManager()
score_board=Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move the cars
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(timmy) < 15:
            game_is_on=False
            score_board.game_over()

    

    # Detect when turtle reaches the other side
    if timmy.ycor() == 280:
        timmy.goto_start()
        car_manager.level_up()
        # Scoreboard
        score_board.increment_level()
    

screen.exitonclick()
