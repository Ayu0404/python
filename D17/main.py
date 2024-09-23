from data import question_data

class Question:
    def __init__(self,text,answer) -> None:
        self.text=text
        self.answer=answer


question_bank=[]
for ques in question_data:
    question_bank.append(Question(ques['text'],ques['answer']))


class QuizBrain:
    def __init__(self,question_bank) -> None:
        self.question_no=0
        self.question_list=question_bank
        self.score=0

    def still_has_questions(self):
        return self.question_no<len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            current_ques=self.question_list[self.question_no]
            self.question_no+=1
            answer=input(f'Q.{self.question_no}. {current_ques.text} (True/ False) ').lower()
            self.check_answer(answer,current_ques.answer)


    def check_answer(self,user_ans,correct_ans):
        if user_ans==correct_ans.lower():
            self.score+=1
            print('You are right.')
        else:
            print('You are wrong.')
        print(f'The answer was {correct_ans}. Your score is {self.score}/{self.question_no}')
        print('\n')



quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print('Well done. Quiz completed.')
print(f'Your score is {quiz.score}/{len(quiz.question_list)}')