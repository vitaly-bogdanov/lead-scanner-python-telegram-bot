from aiogram import Dispatcher
from bot.middlewares.get_message_groups import GetMessageGroups

def setup(dp: Dispatcher):
    dp.middleware.setup(GetMessageGroups())