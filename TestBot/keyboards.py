from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)


# скобки это новая линия кнопок
main_kb = [
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Контакты')]
]
main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже!')


socials_kb = [
    [InlineKeyboardButton(text='Telegram', url='https://t.me/sudoteach')],
    [InlineKeyboardButton(text='YouNube', url='https://youtube.com/@sudoteach')]

]
socials = InlineKeyboardMarkup(inline_keyboard=socials_kb)


catalog_kb = [
    [InlineKeyboardButton(text='adidas', callback_data='adidas')],
    [InlineKeyboardButton(text='nike', callback_data='nike')]
]
catalog = InlineKeyboardMarkup(inline_keyboard=catalog_kb)














