from aiogram.types import Message,CallbackQuery
# from keyboard.default.aloqa import aloqa1
from keyboards.inline.mahsulotlar_tab import *
from keyboards.inline.katalog import katalog1
from aiogram import types
from loader import dp,bot
from aiogram.types import ContentTypes

@dp.callback_query_handler(text="bathroom")
async def bath(call:CallbackQuery):
    await call.message.answer("Quyidagi rasmlarda ikki va bir qavatli krovatlarning turini tanlashingiz , mumkin!",reply_markup=katalog1)
    await call.message.delete()

