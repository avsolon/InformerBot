from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)


def main_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🌤️ Погода", callback_data="weather"),
            InlineKeyboardButton("📈 Валюта", callback_data="currency")
        ],
        [
            InlineKeyboardButton("📉 Крипта", callback_data="crypto"),
            InlineKeyboardButton("🖥️ Сайт", url="https://asolontsov.ru")
        ]
    ])

def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Назад", callback_data="back")]
    ])

def crypto_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📊 TOP 3", callback_data="crypto_top_3"),
            InlineKeyboardButton("📊 TOP 10", callback_data="crypto_top_10"),
        ],
        [
            InlineKeyboardButton("🔎 Поиск", callback_data="crypto_search")
        ],
        [
            InlineKeyboardButton("🏠 Назад", callback_data="back")
        ]
    ])

def crypto_back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Назад", callback_data="crypto")]
    ])