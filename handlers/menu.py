from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from handlers.weather import ask_city
from handlers.currency import show_currency

from utils.keyboards import main_menu_inline


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