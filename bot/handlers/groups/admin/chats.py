import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.keyboards.inline import chat_menu
from bot.utils.db_api.commands.chat_commands import select_all_chats, add_chat, delete_chat
from data.config import CHATS
from loader import dp, app


@dp.message_handler(text="Чаты")
async def chat(message: types.Message):
    await message.answer("Вы находитесь в разделе чаты.", reply_markup=chat_menu)


@dp.callback_query_handler(text="add_chat")
async def add_chat_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите юзернейм группы.")
    await state.set_state("input_chat")


@dp.message_handler(state="input_chat")
async def input_chat_handler(message: types.Message, state: FSMContext):
    chat_username = message.text
    chats = chat_username.split("\n")
    for chat in chats:
        try:
            chat_obj = await app.join_chat(chat)
        except Exception as e:
            await message.answer(f"Что-то пошло не так. {e}")
            await asyncio.sleep(300)

    chat_title = chat_obj.title
    chat_id = chat_obj.id
    chat_username = chat_obj.username

    await add_chat(id=chat_id, username=chat_username, name=chat_title)
    await message.answer("Чат сохранен")
    await state.finish()


@dp.message_handler(regexp=r"/delchat_\d")
async def delete_chat_handler(message: types.Message):
    chat_number = message.text.split("_")[1]
    if "@" in chat_number:
        chat_number = chat_number.split("@")[0]
    await delete_chat(number=int(chat_number))
    await message.answer("Чат удален")


@dp.callback_query_handler(text="all_chats")
async def result_chats(call: types.CallbackQuery):
    chats = await select_all_chats()
    if len(chats) <= 0:
        text = "Пуст"
    else:
        text_with_chats = "\n\n".join([f"{chat.name} {chat.username} /delchat_{chat.number}" for chat in chats])
        text = f"Cписок групп:\n\n{text_with_chats}"

    if len(text) > 4096:
        for x in range(0, len(text), 4096):
            await call.message.answer(text=text[x:x+4096])
    else:
        await call.message.answer(text=text)
