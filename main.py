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
from handlers.weather import show_weather
from handlers.stats import weather_stats
from handlers.crypto import ask_search, handle_search

from states.crypto import WAIT_COIN_SEARCH


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # ✅ START
    app.add_handler(CommandHandler("start", start))

    # ✅ MENU CALLBACKS
    app.add_handler(
        CallbackQueryHandler(
            menu_click,
            pattern="^(weather|currency|crypto|crypto_top_3|crypto_top_10|crypto_search|back)$"
        )
    )

    # ✅ WEATHER INPUT
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            show_weather
        )
    )

    # ✅ CRYPTO SEARCH FSM
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

    # (если есть stats)
    app.add_handler(CommandHandler("weather_stats", weather_stats))

    print("Bot started...")

    app.run_polling()


if __name__ == "__main__":
    main()

# from telegram.ext import (
#     Application,
#     CommandHandler,
#     CallbackQueryHandler,
#     MessageHandler,
#     ConversationHandler,
#     filters
# )
#
# from config import BOT_TOKEN
#
# from handlers.start import start
# from handlers.menu import menu_click
# from handlers.weather import show_weather
# from handlers.stats import weather_stats
#
# from states.states import WAIT_CITY
#
#
# async def error_handler(update, context):
#     print("ERROR:", context.error)
#
#
# def main():
#     app = Application.builder().token(BOT_TOKEN).build()
#
#     weather_conv = ConversationHandler(
#         entry_points=[
#             CallbackQueryHandler(menu_click, pattern="^weather$")
#         ],
#         states={
#             WAIT_CITY: [
#                 MessageHandler(
#                     filters.TEXT & ~filters.COMMAND,
#                     show_weather
#                 )
#             ]
#         },
#         fallbacks=[],
#         allow_reentry=True
#     )
#
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("weather_stats", weather_stats))
#
#     # conversation FIRST
#     app.add_handler(weather_conv)
#
#     # остальные кнопки
#     app.add_handler(
#         CallbackQueryHandler(
#             menu_click,
#             pattern="^(currency|crypto|crypto_top_3|crypto_top_10|back|close)$"
#         )
#     )
#
#     app.add_error_handler(error_handler)
#
#     print("Bot started...")
#
#     app.run_polling()
#
#
# if __name__ == "__main__":
#     main()