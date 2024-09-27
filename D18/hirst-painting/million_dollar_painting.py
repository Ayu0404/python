import turtle as t
import random as r

INITIAL_POS_X=-200
INITIAL_POS_Y=-200

t.colormode(255)

random_colors=[(223, 153, 90), (223, 62, 96), (35, 107, 134), (113, 176, 157), (198, 140, 158), (109, 179, 204), (244, 209, 73), (50, 99, 63), (130, 81, 56), (43, 157, 199), (177, 151, 64), (236, 83, 66), (241, 162, 202), (180, 181, 216), (110, 72, 88), (50, 57, 91), (39, 173, 116), (157, 215, 150), (234, 210, 16), (156, 203, 210), (238, 173, 153), (74, 81, 43), (41, 83, 42), (109, 125, 153), (43, 52, 80), (19, 88, 104)]

timmy=t.Turtle()
timmy.shape('turtle')
screen=t.Screen()

timmy.penup()
timmy.goto(INITIAL_POS_X, INITIAL_POS_Y)
timmy.pendown()

y=INITIAL_POS_Y
for i in range(10):
    for __ in range(10):
        timmy.dot(20,r.choice(random_colors))
        timmy.penup()
        timmy.forward(30)
        timmy.pendown()

    timmy.penup()
    y+=30
    timmy.goto(INITIAL_POS_X, y)
    timmy.pendown()


screen.exitonclick()