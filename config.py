import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

CRYPTO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"

CBR_API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

WEATHER_LOG_PATH = "data/weather_logs.csv"

def parse_admins(raw: str):
    if not raw:
        return []
    return [int(x.strip()) for x in raw.split(",") if x.strip().isdigit()]

ADMIN_IDS = parse_admins(os.getenv("ADMIN_IDS"))