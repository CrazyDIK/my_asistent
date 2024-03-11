from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

my_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="MEXC"),
     KeyboardButton(text="Weather")]
],resize_keyboard=True )

my_kb_mexc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="5 минут", callback_data="5m"),
     InlineKeyboardButton(text="1 час", callback_data="60m"),
     InlineKeyboardButton(text="4 часа", callback_data="4h"),
     InlineKeyboardButton(text="1 день", callback_data="1d"),
     ]
])