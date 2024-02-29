from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

first_But = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Start')
        ],
    ], resize_keyboard=True
)
login_But = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Login')
        ],
        [
            KeyboardButton(text='Register')
        ]
    ], resize_keyboard=True
)

mes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Github', callback_data='git')
        ],
        [
            InlineKeyboardButton(text='Discord', callback_data='dis')
        ],
        [
            InlineKeyboardButton(text='Google', callback_data='gygl')
        ],
        [
            InlineKeyboardButton(text='Gmail', callback_data='mail')
        ],
        [
            InlineKeyboardButton(text='Facebook', callback_data='fb')
        ],
        [
            InlineKeyboardButton(text='Steam', callback_data='stm')
        ],
        [
            InlineKeyboardButton(text='Twitch', callback_data='tvtw')
        ]
    ]
)