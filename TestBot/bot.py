import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from bot_token import TOKEN

# Polling, т.е бесконечный цикл проверки апдейтов
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


# Функция main() запускается только в случае если скрипт запущен с этого файла
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

