import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("----Weather Report----")
        print(f"City: {city}")
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

    else:
        print("City not found or API error")


while True:
    print("---Weather CLI App---")
    print("1. Search Weather")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        city = input("Enter city name: ")
        get_weather(city)

    elif choice == '2':
        print("EXiting...")
        break

    else:
        print("Invalid choice")