from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from bot.keyboards.inline import keyword_menu
from bot.utils.db_api.commands.keyword_commands import add_keyword, select_all_keywords, delete_keyword
from loader import dp


@dp.message_handler(text="Ключевые слова")
async def chat(message: types.Message):
    await message.answer("Вы находитесь в разделе ключевые слова.", reply_markup=keyword_menu)


@dp.callback_query_handler(text="add_keywords")
async def add_keyword_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="Введите ключевое слово или фразу по которым должен идти поиск")
    await state.set_state("input_keyword")


@dp.message_handler(state="input_keyword")
async def input_keyword_handler(message: types.Message, state: FSMContext):
    await add_keyword(message.text)
    await message.answer("Ключевое слово сохранено.", reply_markup=keyword_menu)
    await state.finish()

@dp.callback_query_handler(text="all_keywords")
async def result_keywords_handler(call: types.CallbackQuery):
    words_obj = await select_all_keywords()
    text_with_words = "\n".join(
        [f"{words.word} /delword_{words.id}" for words in words_obj]
    )
    text = f"Cписок слов:\n\n{text_with_words}"
    if len(text) > 4096:
        for x in range(0, len(text), 4096):
            await call.message.answer(text=text[x:x+4096])
    else:
        await call.message.answer(text=text)


@dp.message_handler(regexp=r"/delword_\d")
async def delete_word(message: types.Message):
    word_id = message.text.split("_")[1]
    if "@" in word_id:
        word_id = word_id.split("@")[0]

    await delete_keyword(id=int(word_id))
    await message.answer("Cлово удалено")



