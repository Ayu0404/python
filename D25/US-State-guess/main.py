from turtle import Screen, Turtle
import pandas
IMG_URL='D25/US-State-guess/blank_states_img.gif'

screen=Screen()
screen.title('50 US States')
screen.addshape(IMG_URL)

canvas=Turtle()
canvas.shape(IMG_URL)

data=pandas.read_csv('D25/US-State-guess/50_states.csv')
states=data.state.tolist()
guessed_states=[]

while len(guessed_states)<50:
    answer=screen.textinput(title=f'{len(guessed_states)}/50 states guessed.', prompt='Enter the name of the state. ').title()
    
    if answer=='Exit':
        missing_states=[state for state in states if state not in guessed_states]
        other_states=pandas.DataFrame(missing_states)
        other_states.to_csv('D25/US-State-guess/states-left.csv')
        break

    if answer not in guessed_states:
        if answer in states:
            guessed_states.append(answer)
            text=Turtle()
            text.penup()
            text.hideturtle()
            state=data[data.state==answer]
            text.goto(int(state.x),int(state.y))
            text.write(state.state.item(),align='center',font=('Courier',10,'normal'))
