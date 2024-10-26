from tkinter import * 
import random
import string
from tkinter import messagebox
import pyperclip
import json

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


def save(website,email,password):
    new_obj={
        website:{
            'username':email,
            'password':password
        }
    }
    try:
        with open('D29/data.json') as datafile:
            # Reading the old data
            data=json.load(datafile)
    except (FileNotFoundError):
        data={}
        data.update(new_obj)
        with open('D29/data.json','w') as datafile:
            # Dump newly created data
            json.dump(data,datafile,indent=2)
    else:
        # Updating old data with ne
        data.update(new_obj)
        with open('D29/data.json','w') as datafile:
            # Dump newly created data
            json.dump(data,datafile,indent=2)
    finally:
        website_entry.delete(0,END)
        pswd_entry.delete(0,END)


# Save Password
def add_record():
    website_name=website_entry.get()
    entered_pswd=pswd_entry.get()

    if not website_name or not entered_pswd:
        messagebox.showwarning(title='Warning',message='Do not leave any field empty.')
    else:
        save(website_name,email_entry.get(),entered_pswd)
        

def search():
    website=website_entry.get()
    if not website:
        messagebox.showwarning(title='Warning',message='Enter the website name.')
    else:
        try:
            with open('D29/data.json') as datafile:
                data=json.load(datafile)
        except FileNotFoundError:
            messagebox.showwarning(title='No Data Found',message=f'Username and Password for {website} does not exist.')
        else:
            if website in data:
                username=data[website]['username']
                password=data[website]['password']
                messagebox.showinfo(title=website.title(),message=f'Username: {username}\nPassword: {password}')
            else:
                messagebox.showwarning(title='No Data Found',message=f'Username and Password for {website} does not exist.')
        finally:
            website_entry.delete(0,END)



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
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

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

search_btn=Button(text='Search',width=10,command=search)
search_btn.grid(row=1, column=2)

window.mainloop()
