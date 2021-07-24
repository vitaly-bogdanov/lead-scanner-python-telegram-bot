from pyrogram.types import Message

from bot.utils.db_api.commands.chat_commands import select_all_chats


async def check_chat(_, __, message: Message):
    chat = message.chat.username
    chats = [chat.username for chat in await select_all_chats()]
    return chat in chats