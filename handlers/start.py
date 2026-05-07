from telegram import Update
from telegram.ext import ContextTypes

from utils.keyboards import main_menu_inline


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"👋 Привет, {user.first_name}!\n\n"
        "Я инфо бот.\n"
        "Могу тебе показать:\n"
        "• 🌤️ Погоду\n"
        "• 📈 Курсы валют\n"
        "• 📉 Курсы криптовалют\n\n"
        "Выбери действие 👇"
    )

    await update.message.reply_text(
        text
    )

    await update.message.reply_text(
        "📌 Основное меню:",
        reply_markup=main_menu_inline()
    )