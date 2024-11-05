from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain) -> None:
        self.quiz=quiz

        self.window=Tk()
        self.window.title('Trivia Quiz')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_title=Label(text=f'Score: {self.quiz.score}', font=('Arial',10,'bold'),padx=20,pady=20,bg=THEME_COLOR,fg='white')
        self.score_title.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg='white')
        self.ques_canvas=self.canvas.create_text(150,120,width=250,text='',font=('Arial',15,'italic'),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=30)


        wrong_img=PhotoImage(file='D34/images/false.png')
        self.wrong=Button(image=wrong_img,highlightthickness=0,command=self.incorrect_btn)
        self.wrong.grid(row=2, column=0,padx=20,pady=20)

        right_img=PhotoImage(file='D34/images/true.png')
        self.correct=Button(image=right_img,highlightthickness=0,command=self.correct_btn)
        self.correct.grid(row=2,column=1,padx=20,pady=20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_title.config(text=f'Score: {self.quiz.score}')
            question=self.quiz.next_question()
            self.canvas.itemconfig(self.ques_canvas,text=question)
        else:
            self.canvas.itemconfig(
                self.ques_canvas,
                text=f'Quiz completed. You final score is {self.quiz.score}/{len(self.quiz.question_list)}'
            )
            self.correct.config(state=DISABLED)
            self.wrong.config(state=DISABLED)


    def correct_btn(self):
        self.is_correct(self.quiz.check_answer('True'))

    def incorrect_btn(self):
        self.is_correct(self.quiz.check_answer('False'))


    def is_correct(self,val):
        if val:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)