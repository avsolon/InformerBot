import csv
from datetime import datetime
from config import WEATHER_LOG_PATH

def log_weather(user_id, username, city, status):
    with open(WEATHER_LOG_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_id,
            username,
            city,
            status
        ])