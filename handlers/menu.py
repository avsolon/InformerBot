from telegram import Update
from telegram.ext import ContextTypes
from utils.keyboards import main_menu_inline
from utils.ui.router import UIRouter


async def show_home(update, context):
    router: UIRouter = context.user_data.setdefault(
        "router",
        UIRouter()
    )

    router.reset()

    text = "🏠 Главное меню"

    if update.message:
        await update.message.reply_text(
            text,
            reply_markup=main_menu_inline()
        )
    else:
        await update.callback_query.edit_message_text(
            text,
            reply_markup=main_menu_inline()
        )

    async def go_back(update, context):
        router = context.user_data["router"]
        router.pop()

        await show_home(update, context)

    async def menu_click(update, context):
        query = update.callback_query
        await query.answer()

        action = query.data

        router = context.user_data.setdefault("router", UIRouter())
        router.push(action)

        # 🌤 Weather
        if action == "weather":
            from handlers.weather import ask_city
            return await ask_city(update, context)

        # 🪙 Crypto
        elif action == "crypto":
            from handlers.crypto import crypto_menu_handler
            return await crypto_menu_handler(update, context)

        # 💱 Currency
        elif action == "currency":
            from handlers.currency import show_currency
            await show_currency(update, context)

        # 🔙 Back
        elif action == "back":
            return await go_back(update, context)

        # ❌ Close = НЕ ломаем UI
        elif action == "close":
            await query.message.edit_text("🔒 Окно закрыто. Нажми /start")
            router.reset()

        return None

# from telegram import Update
# from telegram.ext import ContextTypes, ConversationHandler
#
# from handlers.weather import ask_city
# from handlers.currency import show_currency
# from handlers.crypto import (
#     crypto_menu_handler,
#     show_top_3,
#     show_top_10
# )
#
# from utils.keyboards import main_menu_inline
#
#
# async def menu_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#
#     await query.answer()
#
#     action = query.data
#
#     # 🌤️ Погода
#     if action == "weather":
#         return await ask_city(update, context)
#
#     # 💱 Валюта
#     elif action == "currency":
#         await show_currency(update, context)
#         return ConversationHandler.END
#
#     # Крипта
#     elif action == "crypto":
#         await crypto_menu_handler(update, context)
#         return ConversationHandler.END
#
#     elif action == "crypto_top_3":
#         await show_top_3(update, context)
#         return ConversationHandler.END
#
#     elif action == "crypto_top_10":
#         await show_top_10(update, context)
#         return ConversationHandler.END
#
#     # 🔙 Назад
#     elif action == "back":
#         await query.edit_message_text(
#             text="📌 Главное меню:",
#             reply_markup=main_menu_inline()
#         )
#
#         return ConversationHandler.END
#
#     return ConversationHandler.END