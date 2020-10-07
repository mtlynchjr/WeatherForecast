import requests
import logging
import os
import time
from datetime import datetime
from pprint import pprint

# Using Unix time due to the standarization and ubiquity of Unix and the international aspect of the program.
# Converting Unix time to local time at output.

# Logging code obtained from https://gist.github.com/claraj/e07207b7b8a9f37219fb0b3972fc5073.js example
# Create debug log
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

key = os.environ.get("WEATHER_KEY") # Get permanent environment key WEATHER_KEY from .bash_profile

city = input("Please enter a city name: ") # Obtain city name from user
country = input("Please enter the two-letter country code for that city: ") # Obtain contry code from user
location = f"{city}, {country}" # Create location variable for use in the below query

query = {"q" : location, "units" : "imperial", "appid" : key} # Create parametered query as Python dictionary

url = "http://api.openweathermap.org/data/2.5/forecast" # Get API

data = requests.get(url , params=query).json() # Get API data using the above query's search parameters

forecasts_list = data["list"] # Obtain all objects contained within lists in API

for forecast in forecasts_list:
    timestamp = forecast["dt"] # Unix timestamp because any city in any country can be entered, not necessarily CST
    date = (datetime.fromtimestamp(1500000000)) # Convert to local time and display output legibly to user
    temp = forecast["list"]["main"]["temp"] # Obtain temp from main in list
    description = forecast["list"]["weather"]["descpription"] # Obtain description from weather in list
    wind_speed = forecast["list"]["wind"]["speed"] # Obtain speed from wind in list

    # Legibly display forcast results to user
    print(f"The forecast for {date} is: {temp} degrees F. The conditions will be {description} with winds at {wind_speed} MPH. Dress to survive, not to arrive.")

# def main():
# if __name__ == "__main__":
    # main()