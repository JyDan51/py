from os import getenv
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather():
    city = input ("Enter city name: ").strip()

    if not city:
        print ("City name cannot be empty.")
        return

    key = getenv("API_KEY")

    if not key:
        print ("Check API key in .env file.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    try:
        resp = requests.get(url)
        data = resp.json()

        if resp.status_code == 200:
            description = data['weather'][0]['description']
            temp = data['main']['temp'] - 273.15
            name = data['name']

            print (f"\nWeather in {name}:")
            print (f"Condition: {description.capitalize()}")
            print (f"Temperature: {temp:.1f} °C")

        elif resp.status_code == 404:
            print (f"City '{city}' not found.")
        elif resp.status_code == 401:
            print ("Invalid or missing API key.")
        else:
            print (f"Request error (Status: {resp.status_code})")

    except requests.exceptions.RequestException as e:
        print (f"Connection error: {e}")

if __name__ == "__main__":
    get_weather()