import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

print(f"Kljuc ucitan: {API_KEY is not None}")
print(f"Duzina: {len(API_KEY)}")
