from aiogram import types, F, Bot
from core.keyboards.reply import start_btn, admin_btn
from core.settings import settings

async def get_start(message: types.Message, bot: Bot):
    text = f"Assalomu alaykum👋 <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\nMendeleyev botiga xush kelibsiz!😊"

    await message.answer(text=text, reply_markup=start_btn)

async def textfilters(message: types.Message, bot: Bot):
    text = f"Faqtgina tugmalardan foydalanishingiz mumkin!"

    await message.answer(text=text)


async def location_buvayda(message: types.Message, bot: Bot):
    latitude = 40.633913
    longitude = 71.081393

    await message.answer("Bizning Manzilimiz Buvayda tumani 24-maktab kirish qismida: 📍")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


# async def admin_panel(message: types.Message, bot: Bot):
#     if message.from_user.id == settings.bot.admin_id:
#         await message.answer("Xush kelibsiz Mendeleyev admin😊", reply_markup=admin_btn())
