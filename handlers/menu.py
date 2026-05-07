from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from handlers.weather import ask_city
from handlers.currency import show_currency
from handlers.crypto import (
    crypto_menu_handler,
    show_top_3,
    show_top_10
)

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

    # Крипта
    elif action == "crypto":
        await crypto_menu_handler(update, context)
        return ConversationHandler.END

    elif action == "crypto_top_3":
        await show_top_3(update, context)
        return ConversationHandler.END

    elif action == "crypto_top_10":
        await show_top_10(update, context)
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