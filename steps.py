from aiogram.fsm.state import StatesGroup, State

class Steps(StatesGroup):
    start = State()
    register_login = State()
    register = State()
    login = State()
    messengers = State()
    git = State()
    dis = State()
    gygl = State()
    mail = State()
    fb = State()
    stm = State()
    tvtw = State()