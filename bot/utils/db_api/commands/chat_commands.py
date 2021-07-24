from typing import Union

from bot.utils.db_api.schemas.chat import Chat


async def add_chat(id: int, username: str, name: str):
    chat = Chat(id=id, username=username, name=name)
    await chat.create()

async def delete_chat(number: Union[int]):
    chat = await Chat.query.where(Chat.number == number).gino.first()
    await chat.delete()

async def select_all_chats():
    chats = await Chat.query.gino.all()
    return chats
