from telegram import Update
from telegram.ext import ContextTypes
from services.currency_service import get_currency
from utils.keyboards import back_button

async def show_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = await get_currency()

    rates = data["Valute"]

    text = (
        "💱 Курсы валют\n"
        f"USD: {rates['USD']['Value']:.2f} ₽\n"
        f"EUR: {rates['EUR']['Value']:.2f} ₽\n"
        f"CNY: {rates['CNY']['Value']:.2f} ₽"
    )

    await query.edit_message_text(text, reply_markup=back_button())