import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from data import DATA,NEWS_DATA
from newsapi import NewsApiClient

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
URL_STOCK='https://www.alphavantage.co/query'
URL_NEWS='https://newsapi.org/v2/everything'

params_stock={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'outputsize':'compact',
    'apikey':os.getenv('ALPHA_VANTAGE')
}

params_news={
    'q':COMPANY_NAME,
    'apiKey':os.getenv('NEWS_API')
}

# response=requests.get(url_stock=URL_STOCK,params_stock=params_stock)
# response.raise_for_status()
# data=response.json()
# stock_time_series_data=data['Time Series (Daily)']
stock_time_series_data=DATA
# print(object.e(stock_time_series_data))

curr_date=datetime.now().date()
prev_date=curr_date-timedelta(days=1)
two_days_ago=curr_date-timedelta(days=2)

prev_Date_str=prev_date.strftime("%Y-%m-%d")
two_days_ago_str=two_days_ago.strftime("%Y-%m-%d")


def get_news():
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    params_news={
        'q':COMPANY_NAME,
        'from':two_days_ago_str,
        'to':prev_Date_str,
        'sortBy':'27popularity',
        'apiKey':os.getenv('NEWS_API')
    }
    # res=requests.get(url=URL_NEWS,params=params_news)
    # news_data=res.json()
    # news=news_data['articles'][0]
    # return news
    return NEWS_DATA['articles'][:3]

if prev_Date_str and two_days_ago_str in stock_time_series_data:
    prev_open=float(stock_time_series_data[prev_Date_str]['1. open'])
    two_days_ago_close=float(stock_time_series_data[two_days_ago_str]['4. close'])
    price_percent_change=round(((two_days_ago_close-prev_open)/two_days_ago_close)*100,2)

    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    if (price_percent_change > 0 and price_percent_change > 5) or (price_percent_change < 0 and price_percent_change < -5):
        news=get_news()
        formatted_message=[f'{COMPANY_NAME}: {price_percent_change}% \n{article['title']} \n{article['description']}' for article in news]              
        print(formatted_message)      
        

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# Somehow, not able to receive messages, even though they are queued.