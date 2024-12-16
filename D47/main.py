from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
my_email = email = os.getenv('EMAIL')
pswd = os.getenv('PSWD')
to = os.getenv('TO')


url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
price = float(soup.find(class_="a-offscreen").get_text().split('$')[1])
print(price)


if price < 100:
    with smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=pswd)
        conn.sendmail(from_addr=my_email, to_addrs=to,
                      msg=f'Subject:Price Drop Alert {price}\n\nPrice dropped to {price} for {url}')
        print('Sent')
