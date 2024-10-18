from tkinter import *
CONSTANT=1.609344

window=Tk()
window.title('Miles to Kms')
window.minsize(height=100,width=400)

labelmiles=Label(text='Enter distance in miles', font=('Roboto',10))
labelmiles.grid(row=0,column=0)

input=Entry(width=20)
input.grid(row=0,column=2)


def convert():
    answer=Label(text=f'{round(CONSTANT*float(input.get()),2)}', font=('Roboto',10,'bold'))
    answer.grid(row=2,column=2)


button=Button(text='Convert', command=convert)
button.grid(row=1,column=1)


labelkms=Label(text='Distance in kms is', font=('Roboto',10))
labelkms.grid(row=2,column=0)

window.mainloop()
