from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score=0
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.color('white')
        self.update_score()

    
    def update_score(self):
        self.write(f'Score: {self.score}',align='center',font=('Arial',10,'normal'))


    def refresh_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over. ',align='center',font=('Arial',15,'normal'))
