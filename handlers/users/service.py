from loader import dp,bot
from aiogram.types import Message, CallbackQuery
from keyboards.inline.mahsulotlar_tab import mahsulot1,boglan
from keyboards.default.aloqa import aloqa1
from utils.db_api import send_ex


@dp.callback_query_handler(text="service")
async def serv(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bizda servis xizmati , asosan o'zimiz ishlab chiqargan mahsulotlar uchun qilinadi!\nIshlab chiqarilganiga 1 yildan oshmagan mahsulotlarga bepul xizmat ko'rsatamiz!")
    await call.message.answer("Undan tashqari o'zimiz ishlab chiqargan mahsulotlarni qayta transformatsya(restavratsya) qilish xizmati ham bor!\nXizmat pullik, xizmat ko'rsatish narxi mahsulotning holatiga qarab belgilanadi!",reply_markup=aloqa1)



@dp.callback_query_handler(text="ulchov")
async def ulch(call:CallbackQuery):
    await call.message.answer("Biz asosan quyidagi mahsulotlar uchin o'lchov olamiz!",reply_markup=mahsulot1)
    await call.message.answer("Agar biror qaysi mahsulotga buyurtma bermoqchi bo'lsangiz ,biz bilan aloqaga chiqing,yoki bizga murojaatingizni yozib qoldiring!",reply_markup=boglan)


@dp.callback_query_handler(text="consultation")
async def kons(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bizda konsultatsya bepul, o'zingizni qiziqtirgan barcha ma'lumotlarni so'rashingiz mumkin! Undan tashqari ushbu botda ham, faoliyatimiz haqida bir qancha ma'lumotlar berib o'tilgan!",reply_markup=boglan)
    await call.message.answer("Biz bilan bog'lanish uchun:\n+99891 537-33-99")


@dp.callback_query_handler(text="about")
async gef abi(call:CallbackQuery):
