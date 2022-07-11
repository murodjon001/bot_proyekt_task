from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Tarjimon"),
            KeyboardButton(text="Products")
        ],
    ],
    resize_keyboard=True

)

languagemenu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="En ➡️ Uz"),
            KeyboardButton(text="Uz ➡️ En")
        ],
    ],
    resize_keyboard=True
)

shart = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Yes")
        ],
        [
            KeyboardButton(text="No")
        ],
    ],
    resize_keyboard=True
)