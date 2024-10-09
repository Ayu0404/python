from turtle import Turtle

LEFT=(-430,0)
RIGHT=(420,0)
MOVE_DISTANCE=20

class Paddle(Turtle):
    def __init__(self, is_left) -> None:
        super().__init__()

        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.points=0
        self.is_left=is_left

        if is_left:
            self.goto(LEFT)
        else:
            self.goto(RIGHT)


    def up(self):
        newY=self.ycor()+MOVE_DISTANCE
        if newY < 280:
            self.goto(self.xcor(),newY)


    def down(self):
        newY=self.ycor()-MOVE_DISTANCE
        if newY > -250:
            self.goto(self.xcor(),newY)

