from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score=0
        self.r_score=0
        self.update_score()


    def left_score(self):
        self.l_score+=1
        self.update_score()


    def right_score(self):
        self.r_score+=1
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.goto(-100,260)
        self.write(self.l_score,align='center',font=('Courier',20,'normal'))
        self.goto(100,260)
        self.write(self.r_score,align='center',font=('Courier',20,'normal'))

