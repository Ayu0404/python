from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
count_down_event=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # reset timer
    window.after_cancel(count_down_event)
    # reset check marks
    reps_display.config(text='')
    # change title to timer
    title.config(text='Timer')
    canvas.itemconfig(timer_text,text='00:00')
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global tick
    reps+=1

    work_secs=WORK_MIN*60
    short_break_secs=SHORT_BREAK_MIN*60
    long_break_secs=LONG_BREAK_MIN*60
    window.attributes("-topmost", False)

    if reps%8==0:
        title.config(text=f'Break',fg=RED)
        count_down(long_break_secs)
    elif reps%2==0:
        title.config(text=f'Break',fg=PINK)
        window.attributes("-topmost", True)
        count_down(short_break_secs)
    else:
        title.config(text=f'Work',fg=GREEN)
        count_down(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global count_down_event
    mins_left=math.floor(count/60)
    secs_left=count%60
    if mins_left<10:
        mins_left=f'0{mins_left}'
    if secs_left<10:
        secs_left=f'0{secs_left}'

    canvas.itemconfig(timer_text,text=f'{mins_left}:{secs_left}')
    if count>0:
        count_down_event=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=''
        count=math.floor(reps/2)
        for _ in range(count):
            marks+='✔'
        reps_display.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100,bg=YELLOW)


title=Label(text='Timer', font=(FONT_NAME,40,'bold'), fg=GREEN,bg=YELLOW,highlightthickness=0)
title.grid(row=0,column=1)

canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='D28/tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text='00:00',font=(FONT_NAME,35,'bold'),fill='white')
canvas.grid(row=1,column=1)

button=Button(text='Start',highlightthickness=0, command=start_timer)
button.grid(row=2,column=0)

button=Button(text='Reset', highlightthickness=0,command=reset_timer)
button.grid(row=2,column=2)

reps_display=Label(font=(FONT_NAME,20,'bold'), fg=GREEN,bg=YELLOW,highlightthickness=0)
reps_display.grid(row=3,column=1)

window.mainloop()
