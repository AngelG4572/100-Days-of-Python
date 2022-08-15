import requests
import datetime as dt

parameters = {
    "lat": 31.75872,
    "lng": -106.486931,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()

LOCAL_UTC_OFFSET = -6


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


sunrise = utc_to_local(int(data["results"]["sunrise"].split("T")[1].split(":")[0]))
sunset = utc_to_local(int(data["results"]["sunset"].split("T")[1].split(":")[0]))

print(sunrise)
print(sunset)

now = dt.datetime.now()
print(now.hour)
