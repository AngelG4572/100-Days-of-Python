import requests
import datetime as dt
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("../keys.env")
STOCK_API_KEY = os.environ['ALPHA_VANTAGE_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['twilio_number']
recipient = os.environ['my_number']
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title,description",
    "pageSize": 3,
    "sortBy": "popularity",
    "language": "en",
    "from": str(dt.date.today() - dt.timedelta(7)),
}


def adjust_date(date):
    weekday = dt.date.weekday(date)
    while weekday > 4:
        date -= dt.timedelta(1)
        weekday = dt.date.weekday(date)
    return date


def get_api_data(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


yesterday = dt.date.today() - dt.timedelta(1)
yesterday = adjust_date(yesterday)
day_before = yesterday - dt.timedelta(1)
day_before = adjust_date(day_before)

data = get_api_data(STOCK_URL, stock_params)["Time Series (Daily)"]
yesterdays_data = data[str(yesterday)]
day_before_data = data[str(day_before)]
yesterday_price = float(yesterdays_data["4. close"])
day_before_price = float(day_before_data["4. close"])

difference = round(((yesterday_price - day_before_price) / day_before_price) * 100)
if difference < 0:
    symbol = "🔻"
else:
    symbol = "🔺"

if abs(difference) >= 5:

    data = get_api_data(NEWS_URL, news_params)["articles"]
    client = Client(account_sid, auth_token)

    for article in data:
        headline = article["title"]
        brief = article["description"]

        body = f"{STOCK}: {symbol}{difference}% \nHeadline: {headline} \nBrief: {brief}"

        message = client.messages.create(
            body=body,
            from_=twilio_number,
            to=recipient
        )

        print(message.sid)
else:
    print(f"not enough change: {difference}%")
