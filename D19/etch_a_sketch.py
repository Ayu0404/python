from turtle import Turtle, Screen

timmy=Turtle()
screen=Screen()

def moveForward():
    timmy.forward(10)

def moveBackward():
    timmy.backward(10)

def moveCounterClockwise():
    timmy.left(10)

def moveClockwise():
    timmy.right(10)

def clearScreen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key='w',fun=moveForward)
screen.onkey(key='s',fun=moveBackward)
screen.onkey(key='a',fun=moveCounterClockwise)
screen.onkey(key='d',fun=moveClockwise)
screen.onkey(key='c',fun=clearScreen)
screen.exitonclick()