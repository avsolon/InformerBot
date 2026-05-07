from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from config import BOT_TOKEN

from handlers.start import start
from handlers.menu import menu_click
from handlers.weather import ask_city, show_weather
from handlers.stats import weather_stats
from handlers.crypto import ask_search, handle_search

from states.weather import WAIT_CITY
from states.crypto import WAIT_COIN_SEARCH


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # ✅ START
    app.add_handler(CommandHandler("start", start))

    # ✅ WEATHER FSM
    weather_conv = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(
                ask_city,
                pattern="^weather$"
            )
        ],
        states={
            WAIT_CITY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    show_weather
                )
            ]
        },
        fallbacks=[],
        per_message=False
    )

    app.add_handler(weather_conv)

    # ✅ CRYPTO FSM
    crypto_search_conv = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(
                ask_search,
                pattern="^crypto_search$"
            )
        ],
        states={
            WAIT_COIN_SEARCH: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    handle_search
                )
            ]
        },
        fallbacks=[],
        per_message=False
    )

    app.add_handler(crypto_search_conv)

    # ✅ MENU CALLBACKS
    app.add_handler(
        CallbackQueryHandler(
            menu_click,
            pattern="^(currency|crypto|crypto_top_3|crypto_top_10|crypto_search|back)$"
        )
    )

    app.add_handler(CommandHandler("weather_stats", weather_stats))

    print("Bot started...")

    app.run_polling()


if __name__ == "__main__":
    main()
