from tkinter import * 
import random
import string
from tkinter import messagebox
import pyperclip

LENGTH=20
NUMBERS=string.digits
LETTERS=string.ascii_letters
SPECIAL_CHARACTERS="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


# Password Generator
def get_password(nums_len,letters_len,sp_chars_len):    
    nums_gen=[random.choice(NUMBERS) for __ in range(0,nums_len)]
    letters_gen=[random.choice(LETTERS) for __ in range(0,letters_len)]
    spchars_gen=[random.choice(SPECIAL_CHARACTERS) for __ in range(0,sp_chars_len)]
    pswd=nums_gen+letters_gen+spchars_gen
    random.shuffle(pswd)
    return ''.join(pswd)


def generate_password():
    nums_len=random.randint(0,LENGTH)
    letters_len=random.randint(0,LENGTH-nums_len)
    sp_chars_len=LENGTH-(nums_len+letters_len)

    pswd_generated=get_password(nums_len,letters_len,sp_chars_len)

    if pswd_entry.get():
        pswd_entry.delete(0,'end')
    
    pyperclip.copy(pswd_generated)
    pswd_entry.insert(0,f'{pswd_generated}')


# Save Password
def add_record():
    if not website_entry.get() or not pswd_entry.get():
        messagebox.showwarning(title='Warning',message='Do not leave any field empty.')
    else:
        is_confirmed=messagebox.askokcancel(title=f'{website_entry.get()}',message=f'The details entered are: \nWebsite: {website_entry.get()} \nUsername/Email: {email_entry.get()} \nPassword: {pswd_entry.get()}')

        if is_confirmed:
            with open('D29/data.txt','a') as file:
                file.write(f'{website_entry.get()} | {email_entry.get()} | {pswd_entry.get()}\n')
            website_entry.delete(0,END)
            pswd_entry.delete(0,END)


# UI Setup
window=Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas for the logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='D29/logo.png')  
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)

pswd_label = Label(text='Password')
pswd_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0,'ayushi@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

pswd_entry = Entry(width=21)
pswd_entry.grid(row=3, column=1)

# Buttons
generate_pswd = Button(text='Generate Password',command=generate_password)
generate_pswd.grid(row=3, column=2)

add_btn = Button(text='Add', width=36,command=add_record)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
