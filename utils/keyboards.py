from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

def main_reply_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["🙂 Мой профиль"],
            [KeyboardButton("Отправить контакт", request_contact=True)],
            [KeyboardButton("Отправить геолокацию", request_location=True)]
        ],
        resize_keyboard=True
    )

def main_menu_inline():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🌤️ Погода", callback_data="weather"),
            InlineKeyboardButton("📈 Валюта", callback_data="currency")
        ],
        [
            InlineKeyboardButton("📉 Криптовалюта", callback_data="crypto"),
            InlineKeyboardButton("🖥️ Сайт", url="https://asolontsov.ru")
        ],
        [
            InlineKeyboardButton("❌ Очистить", callback_data="close")
        ]
    ])

def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Назад", callback_data="back")]
    ])