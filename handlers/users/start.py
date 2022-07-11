from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from filters import IsPrivate
from keyboards.inline.mahsulotlar_tab import mahsulotlar

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} . Mebel uchun buyurtma qabul qiluvchi Botimizga xush kelibsiz!",reply_markup=mahsulotlar)