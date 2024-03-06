from ast import Await
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from core.keyboards.my_key import my_kb, my_kb_mexc
from core.utils.get_mexc import get_mex

router = Router()


@router.message(CommandStart())
async def welcome(message: Message):
    await message.answer("Hello my friends!", reply_markup=my_kb)


@router.message(F.text == "MEXC")
async def get_mexc(message: Message):
    await message.delete()
    await message.answer("Выбери интервал:", reply_markup=my_kb_mexc)


@router.callback_query()
async def get_mex_int(call: CallbackQuery):
    # for rezult in get_mex(call.data):
    await call.message.edit_text(
        f"Закрытие торгов MEXC за {call.data} : \n"
        f"Закрытие текуще: {get_mex(call.data)[0][4]} \n"
        f"Закрытие предыдущее : {get_mex(call.data)[1][4]}", reply_markup=my_kb_mexc
    )
    await call.answer()
