from aiogram import Bot, Dispatcher, types, F
import asyncio

TOKEN = "8553426786:AAHFhykr2-wkdxhF6JDy2dx24WEM43iQBtI"
ADMIN_ID = 671141387

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start (НОВЫЙ СИНТАКСИС)
@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer(
        "Привет, камнекат!\n\n"
        "Ты попал в бот SIZIF MEDIA — место, где абсурд не лечат, а коллекционируют.\n\n"
        "Здесь можно:\n"
        "— поделиться своей абсурдной историей из жизни\n"
        "— предложить тему для поста\n"
        "— просто написать, если стало невыносимо смешно или грустно\n\n"
        "Мы читаем всё. Иногда молча киваем, иногда пишем пост.\n\n"
        "Камень сам себя не покатит, давай, рассказывай 🪨"
    )

@dp.message()
async def handle_message(message: types.Message):
    await message.answer(
        "Получили, спасибо 🪨\n\n"
        "Твоя история уже где-то в середине горы — читаем, думаем, возможно скоро она станет постом.\n"
        "Катим дальше."
    )

    user = message.from_user.username or "без username"
    await bot.send_message(
        ADMIN_ID,
        f"Новое сообщение:\n\n{message.text}\n\nОт: @{user}"
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
