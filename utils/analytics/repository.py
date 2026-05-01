import pandas as pd
from config import WEATHER_LOG_PATH
import os

def load_weather_logs():
    if not os.path.exists(WEATHER_LOG_PATH):
        return pd.DataFrame()

    try:
        df = pd.read_csv(WEATHER_LOG_PATH)
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return df

    required_columns = {'timestamp', 'user_id', 'username', 'city', 'status'}
    if not required_columns.issubset(df.columns):
        return pd.DataFrame()

    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['user_id'] = pd.to_numeric(df['user_id'], errors='coerce')

    return df.dropna(subset=['timestamp'])