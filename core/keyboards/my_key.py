from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

my_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="MEXC")]
],resize_keyboard=True )

my_kb_mexc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="За день", callback_data="1d"),
     InlineKeyboardButton(text="За 4 часа", callback_data="4h"),
     InlineKeyboardButton(text="За час", callback_data="60m"),
     InlineKeyboardButton(text="За 5 минут", callback_data="5m"),
     ]
])