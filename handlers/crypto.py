from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from states.crypto import WAIT_COIN_SEARCH
from services.crypto_service import get_top_crypto, search_coin
from utils.keyboards import crypto_menu, crypto_back_button


async def crypto_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.edit_text(
        "🪙 Crypto menu",
        reply_markup=crypto_menu()
    )


async def show_top_3(update, context):
    query = update.callback_query
    await query.answer()

    data = await get_top_crypto(3)

    text = "📊 TOP 3 crypto:\n\n"
    for c in data:
        text += f"{c['name']} ({c['symbol']})\n💰 ${c['current_price']}\n\n"

    await query.message.edit_text(text, reply_markup=crypto_back_button())


async def show_top_10(update, context):
    query = update.callback_query
    await query.answer()

    data = await get_top_crypto(10)

    text = "📊 TOP 10 crypto:\n\n"
    for c in data:
        text += f"{c['name']} ({c['symbol']}) - ${c['current_price']}\n"

    await query.message.edit_text(text, reply_markup=crypto_back_button())


async def ask_search(update, context):
    query = update.callback_query
    await query.answer()

    await query.message.reply_text("🔎 Введите монету:")
    return WAIT_COIN_SEARCH


async def handle_search(update, context):
    coin = update.message.text

    data = await search_coin(coin)

    if not data:
        await update.message.reply_text("❌ Не найдено")
        return WAIT_COIN_SEARCH

    text = f"""
            🪙 {data['name']} ({data['symbol']})
            💰 Price: ${data['price']}
            📊 24h: {data['change']:.2f}%
            """

    await update.message.reply_text(text, reply_markup=crypto_back_button())
    return ConversationHandler.END