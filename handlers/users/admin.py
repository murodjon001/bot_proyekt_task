from loader import dp,bot
from aiogram.types import Message, CallbackQuery
from aiogram.types import ContentTypes
from filters.admins import AdminFilter
from aiogram import Dispatcher
from aiogram.types import ContentTypes

@dp.message_handler(content_types=ContentTypes.PHOTO, chat_id=929064950)
async def id_file(message:Message):
    file_id1 = message.photo[-1].file_id
    print(file_id1)
    await message.answer("keldi")
