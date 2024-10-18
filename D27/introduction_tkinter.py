from tkinter import *

window=Tk()
window.title('Hello World')
window.minsize(height=400,width=600)
counter=0


label=Label(background='grey',text=f'Button clicks {counter}', font=('Roboto',24,'bold'))
label.grid(row=0,column=0)


input=Entry(width=20)
input.insert(string='heading', index=0)
input.grid(row=0,column=3)


def btn_clicked():
    global counter
    counter+=1
    input_txt=input.get()
    if input_txt:
        label.config(text=f'{input_txt}')
    else:
        label.config(text=f'Button clicks {counter}')

button=Button(text='Click Me', command=btn_clicked)
button.grid(row=1,column=2)


text_box=Text(height=5,width=30)
text_box.focus()
text_box.insert(END,'Enter your introduction....')
text_box.grid(row=3,column=0)


def get_spinbox_val():
    val=spin_box.get()
    spinbox_label=Label(text=f'{val}', font=('Roboto',10,'bold'))
    spinbox_label.grid(row=5,column=0)


spin_box=Spinbox(from_=1,to=10,width=10,command=get_spinbox_val)
spin_box.grid(row=4,column=0)


def is_checkbox_checked():
    print(is_checked.get())

is_checked=IntVar()
checkbox=Checkbutton(text='Is checked?', variable=is_checked,command=is_checkbox_checked)
checkbox.grid(row=4,column=3)


window.mainloop()
