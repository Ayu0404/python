import pandas
import random
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv('.gitignore/.env')
my_email=email=os.getenv('EMAIL')
pswd=os.getenv('PSWD')
to=os.getenv('TO')
now=dt.datetime.now()

LETTERS=[
    'D32/birthday_wisher/letter_templates/letter_1.txt',
    'D32/birthday_wisher/letter_templates/letter_2.txt',
    'D32/birthday_wisher/letter_templates/letter_3.txt'
]

# 1. Read the csv file
df=pandas.read_csv('D32/birthday_wisher/birthdays.csv')
records=df.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
send_to=[record for record in records if record['month'] == now.month and record['day'] == now.day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(send_to):
    letter=random.choice(LETTERS)
    with open(letter) as l:
        msg=l.readlines()

    for person in send_to:
        name=person['name']
        to=person['email']
        subject=f'Happy Birthday {name}'
        personalized_msg=[m.replace('[NAME]',name) for m in msg]
        bday_msg=' '.join(personalized_msg)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com',587) as conn:    
            conn.starttls()
            conn.login(user=my_email,password=pswd)
            conn.sendmail(from_addr=my_email,to_addrs=to,msg=f'Subject:{subject}\n\n{bday_msg}')
            print('Sent')
