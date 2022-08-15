import smtplib
import requests
from datetime import datetime
from time import sleep

MY_LAT = 31.75872
MY_LONG = -106.486931
MY_EMAIL = "a.solis.python@gmail.com"
MY_PASSWORD = ""
LOCAL_UTC_OFFSET = -6


# -------------------- ISS POSITION API -------------------- #
def iss_position():
    """Returns True if the ISS is overhead."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5):
        return True


# -------------------- SUNRISE/SUNSET API -------------------- #
def utc_to_local(utc_hour):
    """Converts int in UTC to local time."""
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24

    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24

    return utc_hour


def night():
    """Returns True if it is currently nighttime (between sunset and sunrise)."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()

    utc_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    utc_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = utc_to_local(utc_sunrise)
    sunset = utc_to_local(utc_sunset)

    time_now = datetime.now()
    if sunrise >= time_now.hour or time_now.hour >= sunset:
        return True


# -------------------- ISS OVERHEAD EMAIL -------------------- #
while True:
    if iss_position() and night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"Subject:Look Up!\n\nThe ISS is overhead!")
            print("Email sent!")
    sleep(60)
