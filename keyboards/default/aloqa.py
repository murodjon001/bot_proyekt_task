from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

aloqa1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Buyurtma berish"),
        ]
    ],
    resize_keyboard= True
)

location1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Joylashuvingizni yuboring!",request_location=True)
        ]
    ],
    resize_keyboard=True
)
contact1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Raqamingizni yuboring!",request_contact=True)
        ]
    ],
    resize_keyboard=True
)
