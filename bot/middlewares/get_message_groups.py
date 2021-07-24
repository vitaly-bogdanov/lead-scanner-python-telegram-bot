from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

class GetMessageGroups(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):

        if not message.chat.type == "group":
            raise CancelHandler()

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        await call.message.delete()
        if not call.message.chat.type == "group":
            raise CancelHandler()
