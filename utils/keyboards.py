from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)


def main_menu_inline():
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