import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_IDS

from utils.analytics.repository import load_weather_logs
from utils.analytics.service import calculate_stats
from utils.analytics.plots import (
    plot_top_cities,
    plot_daily,
    plot_top_users
)


def generate_full_report():
    df = load_weather_logs()

    stats = calculate_stats(df)
    if not stats:
        return None

    text = (
        f"📊 Статистика:\n"
        f"Всего: {stats['total']}\n"
        f"Успешно: {stats['success']}\n"
        f"Не найдено: {stats['city_not_found']}\n"
        f"Ошибки: {stats['errors']}\n"
        f"Пользователи: {stats['users']}\n\n"
    )

    if not stats["top_cities"].empty:
        text += "🏙️ Топ городов:\n"
        for city, count in stats["top_cities"].items():
            text += f"{city}: {count}\n"

    plots = []

    if not stats["top_cities"].empty:
        plots.append(plot_top_cities(stats["top_cities"]))

    if not stats["daily"].empty:
        plots.append(plot_daily(stats["daily"]))

    if not stats["top_users"].empty:
        plots.append(plot_top_users(stats["top_users"]))

    return text, plots


async def weather_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("Нет доступа")
        return

    msg = await update.message.reply_text("⏳ Генерирую отчёт...")

    # 🔥 ВАЖНО: выносим в поток (не блокирует бота)
    result = await asyncio.to_thread(generate_full_report)

    if not result:
        await msg.edit_text("Нет данных")
        return

    text, plots = result

    await msg.edit_text(text)

    for p in plots:
        await update.message.reply_photo(photo=p)