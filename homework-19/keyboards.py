from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Get recommendations'),
            KeyboardButton(text='Earn Money')
        ],
        [
            KeyboardButton(text='Buy house'),
            KeyboardButton(text='Filters')
        ],
        [
            KeyboardButton(text='Show info')
        ]
    ],
    resize_keyboard=True
)


filters_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Discount on', callback_data='on')
        ],
        [
            InlineKeyboardButton(text='Discount off', callback_data='off')
        ],
        [
            InlineKeyboardButton(text='No matter', callback_data='idc')
        ]
    ]
)


def houses_kb(houses):
    builder = ReplyKeyboardBuilder()
    for i in range(len(houses)):
        builder.button(text=f'House #{i+1}')

    return builder.adjust(5).as_markup()
