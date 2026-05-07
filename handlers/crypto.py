from telegram import Update
from telegram.ext import ContextTypes

from services.crypto_service import get_top_crypto
from utils.keyboards import back_button


async def show_crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    data = await get_top_crypto(3)

    if not data:
        await query.edit_message_text(
            "❌ Не удалось получить криптовалюты"
        )
        return

    text = "🪙 Топ криптовалют:\n\n"

    for coin in data:
        text += (
            f"{coin['symbol'].upper()} — "
            f"${coin['current_price']:,}\n"
        )

    await query.edit_message_text(
        text,
        reply_markup=back_button()
    )