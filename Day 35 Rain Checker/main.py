import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("../keys.env")
API_KEY = os.environ['WEATHER_MAP_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['twilio_number']
recipient = os.environ['my_number']
LAT = 31.761877
LONG = -106.485023

params = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()
twelve_hour_list = data["hourly"][:12]
conditions_list = [n["weather"][0]["id"] for n in twelve_hour_list]

rain = False
for x in range(0, 12):
    if data["hourly"][x]["weather"][0]["id"] < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring an umbrella.",
        from_=twilio_number,
        to=recipient
    )

    print(message.sid)
else:
    print("Message not sent: it won't rain.")
