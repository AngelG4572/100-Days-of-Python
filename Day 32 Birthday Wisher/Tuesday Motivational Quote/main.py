import smtplib
import datetime as dt
import random

MY_EMAIL = "a.solis.python@gmail.com"
MY_PASSWORD = ""
OTHER_EMAIL = "a.solis1010@yahoo.com"

now = dt.datetime.now()
day_of_week = now.weekday()

with open(file="quotes.txt") as quotes:
    quote_list = quotes.readlines()
    quote = random.choice(quote_list).strip("\n")

if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=OTHER_EMAIL,
                            msg=f"Subject:Tuesday Motivational Quote\n\n{quote}")
