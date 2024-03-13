from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from commands import set_commands

import keyboards as kb

router = Router()


# Основная команда /start
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEKbLBlGIjkgbUNgsPY41foi67itS-2BQACDAEAAiI3jgR7D1jAYFgdrjAE')
    await message.answer('Добро пожаловать!', reply_markup=kb.main)


# Получение id/имени с помощью message.from_user.id
@router.message(F.text == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')


# Пример отправки картинок
@router.message(F.text == '/send_image')
async def cmd_send_image(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAPhZRQPJ4XkzfLzMfcT8l32IC55GQoAAtDTMRuxl6FItPRqbg7TQ3QBAAMCAAN5AAMwBA',
                               caption='описание')


# Пример отправки документов
@router.message(F.text == '/send_doc')
async def cmd_send_doc(message: Message):
    await message.answer_document(document='BQACAgIAAxkBAAPlZRQRxKJ8eUdA2KLnXNIVUDh8zJ0AAvY4AAKxl6FI_xRE2_7FakQwBA',
                                  caption='описание')


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите бренд', reply_markup=kb.catalog)


@router.callback_query(F.data == 'adidas')
async def cb_catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали бренд', show_alert=True)
    await callback.message.answer(f'Вы выбрали {callback.data}')


@router.callback_query(F.data == 'nike')
async def cb_catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали бренд', show_alert=True)
    await callback.message.answer(f'Вы выбрали {callback.data}')


@router.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer('Наши контакты:', reply_markup=kb.socials)


# Пример обработки фотографий
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(message.photo[-1].file_id)


# Пример обработки документов
@router.message(F.document)
async def get_document(message: Message):
    await message.answer(message.document.file_id)


# Хэндлер без фильтра, сработает, если ни один выше не сработает.
@router.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')