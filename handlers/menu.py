from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from utils.keyboards import main_menu_inline
from handlers.weather import ask_city, show_weather
from handlers.currency import show_currency
from states import WAIT_CITY


async def menu_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    action = query.data

    # 🌤️ Погода
    if action == "weather":
        return await ask_city(update, context)

    # 💱 Валюта
    elif action == "currency":
        await show_currency(update, context)
        return ConversationHandler.END

    # ℹ️ Информация
    elif action == "info":
        await query.edit_message_text(
            text=(
                "ℹ️ Информация о боте\n\n"
                "• Данные о погоде: OpenWeather\n"
                "• Курсы валют: ЦБ РФ\n\n"
                "Бот находится в разработке 🚀"
            ),
            reply_markup=main_menu_inline()
        )
        return ConversationHandler.END

    # 🔙 Назад
    elif action == "back":
        await query.edit_message_text(
            text="📌 Главное меню:",
            reply_markup=main_menu_inline()
        )
        return ConversationHandler.END

    # ❌ Закрыть
    elif action == "close":
        await query.message.delete()
        return ConversationHandler.END

    return ConversationHandler.END