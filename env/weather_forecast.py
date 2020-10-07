import requests
import os
from datetime import datetime
from pprint import pprint

key = os.environ.get("WEATHER_KEY")

city = input("Please enter a city name: ")
country = input("Please enter the two-letter country code for that city: ")
location = f"{city}, {country}"

url = "http://api.openweathermap.org/data/2.5/forecast"
query = {"q" : location, "units" : "imperial", "appid" : key}
data = requests.get(url , params=query).json()

forecasts_list = data["list"]

for forecast in forecasts_list:
    timestamp = ["dt"]
    date = datetime.fromtimestamp(timestamp)
    temp = forecast["main"]["temp"]
    description = forecast["weather"]["descpription"]
    wind_speed = forecast["wind"]["speed"]

    print(f"The forecast for {date} is: {temp} degrees F, {description} with winds at {wind_speed} MPH. Dress to survive, not to arrive.")
