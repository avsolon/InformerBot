from telegram import Update
from telegram.ext import ContextTypes
from services.weather_service import get_weather
from utils.analytics.repository import log_weather
from utils.keyboards import back_button

async def ask_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("Введите город:")
    return 1

async def show_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    data = await get_weather(city)

    user = update.effective_user

    if not data:
        log_weather(user.id, user.username, city, "error")
        await update.message.reply_text("Город не найден")
        return 1

    log_weather(user.id, user.username, city, "success")

    text = (
        f"🌤️ {city}\n"
        f"{data['weather'][0]['description']}\n"
        f"🌡 {data['main']['temp']}°C\n"
        f"💧 {data['main']['humidity']}%\n"
        f"🌬 {data['wind']['speed']} м/с"
    )

    await update.message.reply_text(text, reply_markup=back_button())
    return -1