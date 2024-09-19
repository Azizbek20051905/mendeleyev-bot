from aiogram import types, F, Bot
from aiogram.fsm.context import FSMContext
from core.states.states import BackState, GetStudentInfo
from core.keyboards.reply import direction_btn, register_btn, account_btn, start_btn, address_btn
from core.settings import settings
import datetime

# Ta'lim Yo'nalishlari
async def direction_handler(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl5)  
    await message.answer("O'zingizga tegishli kursni tanlang: ", reply_markup=direction_btn)

# IT TA'LIM
async def rus_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Rus Tili")
    await state.set_state(BackState.lvl4)
    await message.answer("Rus tili: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

# Chet Tillari
async def english_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Ingliz Tili")
    await state.set_state(BackState.lvl4)
    await message.answer("Ingliz tili: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

async def arab_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Arab tili")
    await state.set_state(BackState.lvl4)
    await message.answer("Arab tili: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

async def kimyo_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Kimyo")
    await state.set_state(BackState.lvl4)
    await message.answer("Kimyo: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

async def ona_tili_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Ona tili")
    await state.set_state(BackState.lvl4)
    await message.answer("Ona tili: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

async def english_kids(message: types.Message, state: FSMContext):
    await state.update_data(course = "English kids")
    await state.set_state(BackState.lvl4)
    await message.answer("English kids: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

async def fizika_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Fizika")
    await state.set_state(BackState.lvl4)
    await message.answer("Fizika: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)


async def tarix_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Tarix")
    await state.set_state(BackState.lvl4)
    await message.answer("Tarix: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)

async def biologiya_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Biologia")
    await state.set_state(BackState.lvl4)
    await message.answer("Biologia: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)


async def Math_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Matematika")
    await state.set_state(BackState.lvl4)
    await message.answer("Matematika: Ro'yxatdan o'tishni bosing!", reply_markup=register_btn)


# # Orqaga lvl1
async def orqaga(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl6)
    print("orqaga1 lvl6")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga2(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl1)
    print("orqaga2 lvl1")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga3(message: types.Message, state : FSMContext):
    await state.set_state(BackState.lvl5)
    print("orqaga3 lvl5")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga4(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl6)
    print("orqaga4 lvl1")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga5(message: types.Message):
    print("orqaga5 non")
    await message.answer("🔙 Orqaga", reply_markup=start_btn)  

async def orqaga6(message : types.Message):
    print("orqaga6 non")
    await message.answer("🔙 Orqaga", reply_markup=start_btn)



# "Ro'yxatdan o'tish"
async def register_handler(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(GetStudentInfo.first_name)

async def first_name_hand(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
        print("if")
    else:
        print("Else")
        await state.update_data(first_name=message.text)
        await message.answer("Familiyangizni kiriting:")
        await state.set_state(GetStudentInfo.last_name)

    
async def last_name_hand(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        data = await state.get_data()
        await state.update_data(last_name=message.text)
        await message.answer("Telefon raqamingizni kiriting:\nMasalan: (998 XX XXX XX XX)", reply_markup=account_btn)
        await state.set_state(GetStudentInfo.number)


async def process_phone(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        if message.text:
            phone = message.text
        else:
            phone = message.contact.phone_number
        
        await state.update_data(number = phone)
        await message.answer("Sizga qayerda o'qish qulay:", reply_markup=address_btn)
        await state.set_state(GetStudentInfo.address)


async def address(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        user_data = await state.get_data()
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        phone = user_data.get('number')
        
        address = message.text
        latitude = 40.633913
        longitude = 71.081393

        await message.answer("Bizning Manzilimiz Buvayda tumani 24-maktab kirish qismida: 📍")
        await message.bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)

        course = user_data.get('course')
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        admin_id = settings.bots.admin_id

        await message.bot.send_message(admin_id, text=f"Yangi ro'yxatdan o'tish:\n\nIsm: <b>{first_name}</b>\nFamiliya: <b>{last_name}</b>\nTelefon: <b>{phone}</b>\nManzil: <b>{address}</b>\nKurs: <b>{course}</b>\n\n📅{date}")
        await message.bot.send_message(message.from_user.id, "Adminlar siz bilan aloqaga chiqishadi.✅\nMurojaat uchun: +998 50 506 22 11", reply_markup=direction_btn)

        await state.clear()