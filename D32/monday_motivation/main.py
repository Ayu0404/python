import smtplib
import datetime as dt
import pandas
import random

my_email='arai8548@gmail.com'
pswd='yffe ufns pdjz kffa'
to='ayushiraiar@gmail.com'
now=dt.datetime.now()

if now.weekday()==0:
    subject='You Midweek Motivational Quote'
    df=pandas.read_csv('./D32/monday_motivation/quotes.txt')
    quotes=df.values.tolist()
    quote=random.choice(quotes)[0]

    with smtplib.SMTP('smtp.gmail.com',587) as conn:    
        conn.starttls()
        conn.login(user=my_email,password=pswd)
        conn.sendmail(from_addr=my_email,to_addrs=to,msg=f'Subject:{subject}\n\nRemember:\n\n{quote}')
        print('Sent')

