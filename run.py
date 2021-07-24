from aiogram import Dispatcher
from aiogram.utils import executor
from bot import middlewares
from bot.utils.db_api.db_gino import db
from data.config import POSTGRES_URL
from loader import app, dp

async def on_startup(dp: Dispatcher):
    middlewares.setup(dp)
    await db.set_bind(POSTGRES_URL)
    # await db.gino.drop_all()
    await db.gino.create_all()
    await app.start()


if __name__ == "__main__":
    from userbot import app
    from bot.handlers import dp

    print("Запускаем юзербота")
    executor.start_polling(dp, on_startup=on_startup)