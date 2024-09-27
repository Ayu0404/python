import turtle as t
import random as r

directions=[0,90,180,270]
timmy=t.Turtle()
timmy.shape('turtle')
t.colormode(255)

def get_random_color():
    red=r.randint(0,255)
    green=r.randint(0,255)
    blue=r.randint(0,255)
    r_color=(red,green,blue)
    return r_color


def draw_dotted_line():
    for __ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def draw(angle):
    timmy.forward(100)
    timmy.right(angle)
    timmy.forward(100)


def draw_shapes():
    for lines in range(3,11):
        timmy.color(get_random_color())
        angle=round(360/lines,2)
        for i in range(lines):
            draw(angle)


def random_walk():
    timmy.width(5)
    timmy.speed('fastest')
    for __ in range(300):
        timmy.color(get_random_color())
        timmy.setheading(r.choice(directions))
        timmy.forward(30)    


def draw_spirograph(gap_size):
    timmy.speed('fastest')

    for __ in range(int(360/gap_size)):
        timmy.color(get_random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap_size) 


# Turtle functionalities
# draw_dotted_line()
# draw_shapes()
# random_walk()
draw_spirograph(10)


screen=t.Screen()
screen.exitonclick() 
