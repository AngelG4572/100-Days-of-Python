# Extra Hard Starting Project
import pandas
from random import randint
import smtplib
import datetime as dt

MY_EMAIL = "a.solis.python@gmail.com"
MY_PASSWORD = ""

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

data_dict = data.to_dict(orient="records")

for person in data_dict:
    if person["month"] == current_month:
        if person["day"] == current_day:
            template_content = open(f"letter_templates/letter_{randint(1,3)}.txt").read()
            email_content = template_content.replace("[NAME]", person["name"])
            email_content = email_content.replace("Angela", "Angelina")

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"],
                                    msg=f"Subject:Happy Birthday!\n\n{email_content}")

# I love u beby<3
