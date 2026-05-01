from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from config import BOT_TOKEN

# handlers
from handlers.start import start
from handlers.menu import menu_click
from handlers.weather import ask_city, show_weather
from handlers.currency import show_currency
from handlers.stats import weather_stats
from states import WAIT_CITY


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # 🌤 Conversation: погода
    weather_conv = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(menu_click, pattern="^weather$")
        ],
        states={
            WAIT_CITY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, show_weather)
            ]
        },
        fallbacks=[],
        allow_reentry=True
    )

    # 🔘 Global callback router (меню)
    app.add_handler(CallbackQueryHandler(menu_click))

    # 📌 команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather_stats", weather_stats))

    # 🌤 conversation
    app.add_handler(weather_conv)

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()