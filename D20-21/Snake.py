from turtle import Turtle

START_POS=[(x,0) for x in range(0,-60,-20)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    # 1. Create a Snake
    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    # 2. Move the Snake
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            newX=self.segments[i-1].xcor()
            newY=self.segments[i-1].ycor()
            self.segments[i].goto(newX,newY)
        self.head.forward(MOVE_DISTANCE)


    def add_segment(self,pos):
        block=Turtle('square')
        block.color('white')
        block.penup()
        block.goto(pos)
        self.segments.append(block)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # 3. Control the Snake
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

