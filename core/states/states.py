from aiogram.fsm.state import State, StatesGroup

class GetStudentInfo(StatesGroup):
    course = State()
    first_name = State()
    last_name = State()
    number = State()
    address = State()

class BackState(StatesGroup):
    lvl1 = State()
    lvl2 = State()
    lvl3 = State()
    lvl4 = State()
    lvl5 = State()
    lvl6 = State()