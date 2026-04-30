import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

CBR_API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"
WEATHER_LOG_PATH = "data/weather_logs.csv"

# ADMIN_IDS = [...]