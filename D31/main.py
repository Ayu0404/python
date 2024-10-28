from tkinter import * 
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
words=[]
word={}

try:
    data=pandas.read_csv('D31/updated_data.csv')
except FileNotFoundError:
    all_data=pandas.read_csv('D31/data.csv')
    words=all_data.to_dict(orient='records')
else:
    words=data.to_dict(orient='records')


def set_new_list():
    print(len(words))
    if len(words)>0:
        words.remove(word)
        data=pandas.DataFrame(words)
        data.to_csv('D31/updated_data.csv',index=False)
        get_next_card()
    else:
        canvas.itemconfig(language,text='CONGRATULATIONS',fill='green')
        canvas.itemconfig(display_text,text='You have learnt the most common 500 words used in Norwegian!!',fill='green', font=('Ariel',15,'bold'))    
        wrong_btn.config(state=DISABLED)
        right_btn.config(state=DISABLED)


def get_next_card():
    global word,delay
    window.after_cancel(delay)
    word=random.choice(words)
    canvas.itemconfig(flash_card,image=front_img)
    canvas.itemconfig(language,text='Norwegian',fill='black')
    canvas.itemconfig(display_text,text=word['Norwegian'],fill='black')
    delay=window.after(3000,english_word)


def english_word():
    canvas.itemconfig(language,text='English',fill='white')
    canvas.itemconfig(display_text,text=word['English'],fill='white')
    canvas.itemconfig(flash_card,image=back_img)


# UI Setup
window=Tk()
window.title('Language - Flash Cards')
window.minsize(height=400,width=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
delay=window.after(3000,func=english_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
front_img = PhotoImage(file='D31/images/card_front.png')  
flash_card=canvas.create_image(400, 263, image=front_img)
language=canvas.create_text(400,120,text='',font=('Ariel',30,'bold'))
display_text=canvas.create_text(400,263,text='',font=('Ariel',40,'bold'))
canvas.grid(row=0, column=0,columnspan=3)

wrong_img=PhotoImage(file='D31/images/wrong.png')
wrong_btn=Button(image=wrong_img,highlightthickness=0,command=set_new_list)
wrong_btn.grid(row=1, column=0)

right_img=PhotoImage(file='D31/images/right.png')
back_img=PhotoImage(file='D31/images/card_back.png')

right_btn=Button(image=right_img,highlightthickness=0,command=get_next_card)
right_btn.grid(row=1, column=2)

get_next_card()

window.mainloop()
