import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv

URL = "https://pixe.la/v1/users"

load_dotenv("../keys.env")
USERNAME = os.environ['PIXELA_USERNAME']
TOKEN = os.environ['PIXELA_TOKEN']
GRAPH_ID = "graph1"
HEADER = {
    "X-USER-TOKEN": TOKEN
}

graph_url = f"{URL}/{USERNAME}/graphs"
creation_url = f"{graph_url}/{GRAPH_ID}"


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=URL, json=user_params)
    print(f"Pixela response: {response.text}")


def create_graph():
    graph_params = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "sora",

    }
    response = requests.post(url=graph_url, json=graph_params, headers=HEADER)
    print(f"Pixela response: {response.text}")


def create_pixel():
    print("Creating a data point for today.")
    quantity = input("How many km did you cycle?\n")
    pixel_data = {
        "date": dt.today().strftime("%Y%m%d"),
        "quantity": quantity,
    }

    response = requests.post(url=creation_url, json=pixel_data, headers=HEADER)
    print(f"Pixela response: {response.text}")


def update_pixel():
    user_date = input("What date would you like to change? Please follow the format: yyyymmdd\n")
    quantity = input("Enter the new quantity:\n")

    updated_data = {
        "quantity": quantity
    }
    update_url = f"{creation_url}/{user_date}"

    response = requests.put(url=update_url, json=updated_data, headers=HEADER)
    print(f"Pixela response: {response.text}")


def delete_pixel():
    user_date = input("What date would you like to delete? Please follow the format: yyyymmdd\n")

    delete_url = f"{creation_url}/{user_date}"
    response = requests.delete(url=delete_url, headers=HEADER)
    print(f"Pixela response: {response.text}")


running = True
print("Pixela Cycling Graph Editor")

while running:
    action = input("Please specify an action: (create, update, delete, exit)\n")

    if action == "create":
        create_pixel()
    elif action == "update":
        update_pixel()
    elif action == "delete":
        delete_pixel()
    elif action == "exit":
        running = False
    else:
        print("That's not a valid input.")
