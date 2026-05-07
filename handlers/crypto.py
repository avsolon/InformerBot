from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.crypto_service import get_top_crypto
from utils.keyboards import back_button


def crypto_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔥 Топ 3",
                callback_data="crypto_top_3"
            ),
            InlineKeyboardButton(
                "🚀 Топ 10",
                callback_data="crypto_top_10"
            )
        ],
        [
            InlineKeyboardButton(
                "🔎 Найти монету",
                callback_data="crypto_search"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 Назад",
                callback_data="back"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


async def crypto_menu_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query

    await query.edit_message_text(
        "🪙 Криптовалюты\n\n"
        "Выберите действие:",
        reply_markup=crypto_menu()
    )


async def show_top_crypto(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    limit=3
):
    query = update.callback_query

    data = await get_top_crypto(limit)

    if not data:
        await query.edit_message_text(
            "❌ Не удалось получить данные"
        )
        return

    text = f"🪙 Топ {limit} криптовалют:\n\n"

    for coin in data:
        change = coin.get(
            "price_change_percentage_24h",
            0
        )

        emoji = "📈" if change >= 0 else "📉"

        text += (
            f"{emoji} "
            f"{coin['symbol'].upper()}\n"
            f"💲 ${coin['current_price']:,}\n"
            f"24ч: {change:.2f}%\n\n"
        )

    await query.edit_message_text(
        text,
        reply_markup=crypto_menu()
    )


async def show_top_3(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await show_top_crypto(update, context, 3)


async def show_top_10(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await show_top_crypto(update, context, 10)

# from telegram import Update
# from telegram.ext import ContextTypes
#
# from services.crypto_service import get_top_crypto
# from utils.keyboards import back_button
#
#
# async def show_crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#
#     data = await get_top_crypto(3)
#
#     if not data:
#         await query.edit_message_text(
#             "❌ Не удалось получить криптовалюты"
#         )
#         return
#
#     text = "🪙 Топ криптовалют:\n\n"
#
#     for coin in data:
#         text += (
#             f"{coin['symbol'].upper()} — "
#             f"${coin['current_price']:,}\n"
#         )
#
#     await query.edit_message_text(
#         text,
#         reply_markup=back_button()
#     )