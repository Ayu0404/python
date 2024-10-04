from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
    

    def refresh(self):
        randX=r.randint(-260,260)
        randY=r.randint(-260,260)
        self.goto(randX,randY)
        