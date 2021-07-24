from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from nltk import SnowballStemmer
from pyrogram import Client
from data.config import API_TOKEN, API_ID, API_HASH

bot = Bot(token=API_TOKEN, parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)
stemmer = SnowballStemmer('russian')


__all__ = ["bot", "storage", "dp", "app", "stemmer"]


