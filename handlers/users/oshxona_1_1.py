from keyboards.default.aloqa import aloqa1
from keyboards.inline.katalog import katalog1
from keyboards.inline.mahsulotlar_tab import mahsulot1,oshxona_mebel
from loader import dp,bot
from aiogram.types import Message, CallbackQuery
from aiogram.types import ContentTypes
from utils.db_api.postgres_baza import send_ex


@dp.callback_query_handler(text="product")
async def sofa(call:CallbackQuery):
    await call.message.answer("Biz ishlab chiqaradigan mebellar bo'limini tanlang!",reply_markup=mahsulot1)
    await call.message.delete()

@dp.callback_query_handler(text="yumshoq")
async def yumshoq(call:CallbackQuery):
    await call.message.answer("Quyidagi rasmlarda oshxona uchun burchak to'plamining,yumshoq turini tanlashingiz mumkin!",reply_markup=katalog1)



@dp.callback_query_handler(text="oddiy")
async def simple(call:CallbackQuery):
    await call.message.answer("Quyidagi rasmlarda siz oddiy turdagi oshxona uchun burchak to'plamining, turini  tanlashingiz mumkin!",reply_markup=katalog1)
    file_id = send_ex("select file_id from oddiy_u")
    for i in file_id:
        await bot.send_photo(f"{i}")
        print(i)


@dp.callback_query_handler(text="sofa")
async def sufa(call:CallbackQuery):
    await call.message.answer("Biz asosan ikki xil, yumshoq va oddiy turdagi oshxona uchun burchak mebellarini ishlab chiqaramiz! O'zingizni qiziqtirgan turni tanlashingiz mumkin!",reply_markup=oshxona_mebel)
    await call.message.delete()