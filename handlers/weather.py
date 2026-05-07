from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from services.weather_service import get_weather
from utils.logger.weather_logger import log_weather
from utils.keyboards import back_button
from states import WAIT_CITY


async def ask_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    await query.message.reply_text(
        "🌍 Введите название города:"
    )

    return WAIT_CITY


async def show_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("SHOW_WEATHER CALLED")
    city = update.message.text.strip()

    user = update.effective_user

    print(f"WEATHER REQUEST: {city}")

    data = await get_weather(city)

    if not data:
        log_weather(user.id, user.username, city, "error")

        await update.message.reply_text(
            "❌ Город не найден. Попробуйте ещё раз:"
        )

        return WAIT_CITY

    log_weather(user.id, user.username, city, "success")

    text = (
        f"🌤️ Погода в городе: {city}\n\n"
        f"📝 Состояние: {data['weather'][0]['description']}\n"
        f"🌡️ Температура: {data['main']['temp']}°C\n"
        f"💧 Влажность: {data['main']['humidity']}%\n"
        f"🌬️ Ветер: {data['wind']['speed']} м/с"
    )

    await update.message.reply_text(
        text,
        reply_markup=back_button()
    )

    return ConversationHandler.END