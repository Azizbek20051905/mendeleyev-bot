from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ta'lim Yo'nalishlari🎯")],
        [KeyboardButton(text="Buvayda Tumani Lokatsiyasi📍")]
    ],
    resize_keyboard=True
)

direction_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺Rus tili🇷🇺"), KeyboardButton(text="🇺🇸Ingliz tili🇬🇧")],
        [KeyboardButton(text="🇸🇦Arab tili🇸🇦"),KeyboardButton(text="👶English kids👶")],
        [KeyboardButton(text="🔭Fizika🔭"),KeyboardButton(text="📚Ona tili📚")],
        [KeyboardButton(text="🧮Matematika📏"),KeyboardButton(text="🧬kimyo🧬")],
        [KeyboardButton(text="⚱️Tarix⚱️"),KeyboardButton(text="🦠Biologia🦠")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

register_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish✅")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

account_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt ulashish", request_contact=True)]
    ],
    resize_keyboard=True
)

address_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Buvayda tumani 24-maktab")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Admin qo'shish➕")],
        [KeyboardButton(text="Admin o'chirish➖")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)