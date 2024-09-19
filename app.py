from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from core.settings import settings
from aiogram.client.bot import DefaultBotProperties

import asyncio
import logging

from core.handlers.basic import get_start, textfilters, location_buvayda
from core.handlers.keyboard_hand import (direction_handler, rus_course, english_course, arab_course,
                                         kimyo_course, ona_tili_course, english_kids, fizika_course, biologiya_course,
                                         tarix_course, register_handler, first_name_hand, last_name_hand,
                                         process_phone, Math_course, address,
                                         orqaga, orqaga2, orqaga3, orqaga4, orqaga5, orqaga6)
from core.states.states import GetStudentInfo, BackState
from core.utils.commands import set_commands

async def start_bot(bot: Bot):
    print("Bot ishga tushdi!")
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot ishga tushdi!")



async def stop_bot(bot: Bot):
    print("Bot ishdan to'xtadi!")
    await bot.send_message(settings.bots.admin_id, text="Bot to'xtadi!")

async def start():
    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    logging.basicConfig(
        level="ERROR",
        filename="debug.log",
        # format="%(asctime)s - %(name)s - [ %(message)s ]",
        format="%(asctime)s - ERROR - %(name)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S')
    
    dp = Dispatcher()
    dp.startup.register(start_bot)

    dp.message.register(get_start, Command(commands='start'))
    # dp.message.register(admin_panel, Command(commands='admin'))
    dp.message.register(direction_handler, F.text == "Ta'lim Yo'nalishlari🎯")
    dp.message.register(location_buvayda, F.text == "Buvayda Tumani Lokatsiyasi📍")
    dp.message.register(rus_course, F.text == "🇷🇺Rus tili🇷🇺")
    dp.message.register(english_course, F.text == "🇺🇸Ingliz tili🇬🇧")
    dp.message.register(arab_course, F.text == "🇸🇦Arab tili🇸🇦")
    dp.message.register(english_kids, F.text == "👶English kids👶")
    dp.message.register(fizika_course, F.text == "🔭Fizika🔭")
    dp.message.register(ona_tili_course, F.text == "📚Ona tili📚")
    dp.message.register(Math_course, F.text == "🧮Matematika📏")
    dp.message.register(kimyo_course, F.text == "🧬kimyo🧬")
    dp.message.register(tarix_course, F.text == "⚱️Tarix⚱️")
    dp.message.register(biologiya_course, F.text == "🦠Biologia🦠")
    dp.message.register(register_handler, F.text == "Ro'yxatdan o'tish✅")
    dp.message.register(first_name_hand, GetStudentInfo.first_name)
    dp.message.register(last_name_hand, GetStudentInfo.last_name)
    dp.message.register(process_phone, GetStudentInfo.number)
    dp.message.register(address, GetStudentInfo.address)
    dp.message.register(textfilters, F.text != "🔙Orqaga")
    dp.message.register(orqaga, F.text == "🔙Orqaga" and BackState.lvl1)
    dp.message.register(orqaga2, F.text == "🔙Orqaga" and BackState.lvl2)
    dp.message.register(orqaga3, F.text == "🔙Orqaga" and BackState.lvl3)
    dp.message.register(orqaga4, F.text == "🔙Orqaga" and BackState.lvl4)
    dp.message.register(orqaga5, F.text == "🔙Orqaga" and BackState.lvl5)
    dp.message.register(orqaga6, F.text == "🔙Orqaga" and BackState.lvl6)

    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

