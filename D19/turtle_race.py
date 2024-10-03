from turtle import Turtle, Screen
import random as r

screen=Screen()
screen.setup(width=500,height=400)

colors=['red','yellow','orange','green','blue','purple']
LeftMostY=125
turtles=[]
is_game_begin=False

user_bet=screen.textinput('Turtle Race','Make your bet.')

for idx in range(0,6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[idx])
    new_turtle.goto(-230,LeftMostY-idx*35)
    turtles.append(new_turtle)

if user_bet:
    is_game_begin=True
    while is_game_begin:
        for turtle in turtles:
            dist=r.randint(0,10)
            turtle.forward(dist)
            if turtle.xcor()>=230:
                is_game_begin=False
                if user_bet.lower()==turtle.pencolor():
                    print(f'You won. Color {turtle.pencolor()} won the race.')
                else:
                    print(f'You lose. Color {turtle.pencolor()} won the race.')



screen.exitonclick()
