from loader import dp
from aiogram import types
from utils.ramdom_dog import get_dog


@dp.message_handler()
async def dog(message: types.Message):
    await message.answer(text=get_dog())