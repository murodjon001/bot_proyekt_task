from aiogram.types import Message, CallbackQuery
from aiogram import types
from loader import dp,bot
from keyboards.inline.katalog import katalog1


@dp.callback_query_handler(text="tashqari")
async def tash(call:CallbackQuery):
    await call.message.answer("Quyidagi rasmlarda dala hovli uchun stol stul mebel to'plamlari turini tanlashingiz mumkin!",reply_markup=katalog1)
    await call.message.delete()