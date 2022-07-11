from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mahsulotlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mahsulotlar🪑🛏", callback_data="product")
        ],
        [
            InlineKeyboardButton(text="Servis xizmati🛠", callback_data="service")
        ],
        [
            InlineKeyboardButton(text="O'lcham olish xizmati", callback_data="ulchov")
        ],
        [
            InlineKeyboardButton(text="Konsultatsya", callback_data="consultation")
        ],
        [
            InlineKeyboardButton(text="Biz haqimizda",callback_data="about")
        ],
        [
            InlineKeyboardButton(text="Biz bilan bog'laning!", url='https://t.me/developer_sam_city')
        ],
    ],
)

mahsulot1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oshxona mebeli",callback_data="sofa")
        ],
        [
            InlineKeyboardButton(text="Yotoqxona mebeli",callback_data="bathroom")
        ],
        [
            InlineKeyboardButton(text="Dala hovli mebeli",callback_data="tashqari")
        ],
    ],
)

oshxona_mebel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yumshoq",callback_data="yumshoq")
        ],
        [
            InlineKeyboardButton(text="Oddiy",callback_data="oddiy")
        ],
    ],
)

boglan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Biz bilan bog'laning!", url='https://t.me/developer_sam_city')
        ],
    ],
)
