import requests
import datetime
import smtplib
from dotenv import load_dotenv
import os

load_dotenv('.gitignore/.env')
my_email=email=os.getenv('EMAIL')
pswd=os.getenv('PSWD')
to=os.getenv('TO')

URL_SUNRISE='https://api.sunrise-sunset.org/json'
URL_ISS='http://api.open-notify.org/iss-now.json'

subject='ISS within your range'
msg='International Space Station is orbiting right above you. Look up.'

My_LAT=28.704060
My_LNG=77.102493
params={
    'lat':My_LAT,
    'lng':My_LNG,
    'formatted':0,
}

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url=URL_ISS)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if My_LAT-5 <= iss_latitude <= My_LAT+5 and My_LNG-5 <= iss_longitude <= My_LNG+5:
        return True
    return False


def is_night():
    response=requests.get(url=URL_SUNRISE,params=params)
    data=response.json()
    sunrise=int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset=int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now=datetime.datetime.now().hour

    if time_now >= sunrise and time_now <= sunset:
        return True
    return False


if is_iss_overhead() and is_night():
    with smtplib.SMTP('smtp.gmail.com',587) as conn:    
        conn.starttls()
        conn.login(user=my_email,password=pswd)
        conn.sendmail(from_addr=my_email,to_addrs=to,msg=f'Subject:{subject}\n\nRemember:\n\n{msg}')
        print('Sent')
else:
    print('It is not time yet')
