import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


grad = input("Unesi ime grada: ")
url = f"https://wttr.in/{grad}?format=j1"

response=requests.get(url)
data = response.json()

temp = data["current_condition"][0]["temp_C"]
opis = data["current_condition"][0]["weatherDesc"][0]["value"]

print(f"Grad: {grad}")
print(f"Temperatura: {temp}°C")
print(f"Opis: {opis}")