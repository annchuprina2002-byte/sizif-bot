import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiohttp import web

TOKEN = os.environ["BOT_TOKEN"]                       # токен берём из переменной Render
ADMIN_ID = int(os.environ.get("ADMIN_ID", "671141387"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

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


async def health(request):
    return web.Response(text="OK")

async def run_web():
    app = web.Application()
    app.router.add_get("/", health)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", "10000"))
    await web.TCPSite(runner, "0.0.0.0", port).start()

async def main():
    await run_web()                
    await dp.start_polling(bot)    

asyncio.run(main())
