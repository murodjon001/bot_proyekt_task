from aiogram.dispatcher.filters.state import StatesGroup,State

class Zakazstate(StatesGroup):
    name = State()
    telephone = State()
    location = State()
