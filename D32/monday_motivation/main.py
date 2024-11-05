import smtplib
import datetime as dt
import pandas
import random
from dotenv import load_dotenv
import os

load_dotenv()
my_email=email=os.getenv('EMAIL')
pswd=os.getenv('PSWD')
to=os.getenv('TO')
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

