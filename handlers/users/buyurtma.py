from loader import dp,bot
from aiogram.types import Message,CallbackQuery
from states.buyrtma_state import Zakazstate
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from keyboards.default.aloqa import contact1,location1
from utils.db_api.postgres_baza import send_ex
from keyboards.inline.mahsulotlar_tab import mahsulotlar
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(text="Buyurtma berish")
async def client(message: Message):
    await message.answer("Siz bilan bog'lanishimiz uchun, iltimos ma'lumotlaringizni yuboring!")
    await message.answer("Ism va familyangizni kiriting!")
    await Zakazstate.name.set()


@dp.message_handler(state=Zakazstate.name)
async def fio(message:Message,state=FSMContext):
    name = message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("Iltimos 'Raqamingizni yuboring' tugmasini bosing!",reply_markup=contact1)
    await Zakazstate.next()


@dp.message_handler(content_types=ContentTypes.CONTACT,state=Zakazstate.telephone)
async def phon(message:Message,state=FSMContext):

    phone = message.contact.phone_number
    await state.update_data(
        {"phone":phone}
    )
    await message.answer("Iltimos 'Joylashuvingizni yuboring', tugmasini yuboring!",reply_markup=location1)
    await Zakazstate.next()


@dp.message_handler(content_types=ContentTypes.LOCATION,state=Zakazstate.location)
async def loc(message:Message,state=FSMContext):

    location = message.location
    await state.update_data(
        {"location":location}
    )
    await message.answer("Tanlovingiz uchun tashakkur! Biz yaqin orada siz bilan bog'lanamiz!",reply_markup=mahsulotlar)

    data = await state.get_data()
    nam = data.get("name")
    tel = data.get("phone")
    loca = data.get("location")

    full_info = f"{nam}|{tel}|{loca}"


    send_ex(f"""insert into buyurtmalar (malumotlar)
                VALUES ('{full_info}')
                returning *""")

    await ReplyKeyboardRemove()
    await state.finish()




