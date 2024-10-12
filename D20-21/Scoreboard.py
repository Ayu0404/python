from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score=0

        with open('D20-21\data.txt') as data:
            self.high_score=int(data.read())

        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.color('white')
        self.print_score()

    
    def print_score(self):
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}',align='center',font=('Arial',10,'normal'))


    def update_score(self):
        self.score += 1
        if self.score>self.high_score:
            self.high_score=self.score

            with open('D20-21\data.txt','w') as file:
                file.write(str(self.high_score))
        
        self.print_score()


    def reset_score(self):
        self.score=0
        self.print_score()


    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over. ',align='center',font=('Arial',15,'normal'))
