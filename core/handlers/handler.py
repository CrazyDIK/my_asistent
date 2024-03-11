import os
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode, ChatAction
import dotenv
from core.keyboards.my_key import my_kb, my_kb_mexc
from core.utils.get_mexc import get_mex
from core.utils import weather
from dotenv import load_dotenv

load_dotenv()

router = Router()


@router.message(CommandStart())
async def welcome(message: Message):
    await message.answer("Hello my friends!", reply_markup=my_kb)


@router.message(F.text == "MEXC")
async def get_mexc(message: Message):
    await message.delete()
    await message.answer("Выбери интервал:", reply_markup=my_kb_mexc)


@router.message(F.text == "Weather")
async def get_weather(message: Message, bot: Bot):
    await message.delete()
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_PHOTO)
    weather.main()

    await message.answer_photo(photo=FSInputFile("screenshots\guido_pillow_crop.png"))


@router.callback_query()
async def get_mex_int(call: CallbackQuery):
    # for rezult in get_mex(call.data):
    await call.message.edit_text(
        f"Закрытие торгов MEXC за {call.data} : \n"
        f"Закрытие текуще: {get_mex(call.data)[0][4]} \n"
        f"Закрытие предыдущее : {get_mex(call.data)[1][4]}",
        reply_markup=my_kb_mexc,
    )
    await call.answer()
