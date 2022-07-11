from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


katalog1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="To'liq katalog",callback_data="katalog")
        ],
    ],
)
