from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from config import BOT_TOKEN
from utils.keyboards import main_reply_keyboard, main_menu_inline
from handlers.weather import ask_city, show_weather
from handlers.currency import show_currency
from handlers.stats import weather_stats
from handlers.menu import menu_click, WAIT_CITY

WAIT_CITY = 1

async def start(update, context):
    await update.message.reply_text(
        "Привет!",
        reply_markup=main_reply_keyboard()
    )
    await update.message.reply_text(
        "Выбери действие:",
        reply_markup=main_menu_inline()
    )

async def menu_click(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "weather":
        return await ask_city(update, context)

    elif query.data == "currency":
        await show_currency(update, context)

    elif query.data == "back":
        await query.edit_message_text(
            "Меню",
            reply_markup=main_menu_inline()
        )

    elif query.data == "close":
        await query.message.delete()

    return ConversationHandler.END


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(menu_click, pattern="weather")],
        states={
            WAIT_CITY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, show_weather)
            ]
        },
        fallbacks=[]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)
    app.add_handler(CallbackQueryHandler(menu_click))
    app.add_handler(CommandHandler("weather_stats", weather_stats))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()