from pyrogram import filters
from pyrogram.types import Message
import re
from bot.utils.db_api.commands.keyword_commands import select_keyword, select_all_keywords
from data.config import CHAT_ID
from loader import app, bot, stemmer
from userbot.filters_ub.chats import check_chat


@app.on_message(filters=filters.create(check_chat))
async def get_messages_channel(client, message: Message):

    keywords = [keyword.word.lower() for keyword in await select_all_keywords()]
    keywords.reverse()
    text = "<b>Потенциальный лид:</b>\n" \
           "<b>Чат:</b> {chat_title}\n" \
           "<b>Username:</b> @{username}\n" \
           "<b>Имя:</b> {name}\n" \
           "<b>Шаблон:</b> {pattern}\n" \
           "\n<b>Сообщение</b>:\n" \
           "<code>{message}</code>"

    for keyword in keywords:
        massive_t_f = []
        send_text = text.format(chat_title=message.chat.title,
                                username=message.from_user.username,
                                name=message.from_user.first_name,
                                pattern=keyword, message=message.text)
        words = re.findall(r'[a-zа-яё#]+', message.text.lower(), re.I)
        keyword_words = re.findall(r'[a-zа-яё#-]+', keyword, re.I)
        words_stemmer = list(map(stemmer.stem, words))
        keywords_stem = list(map(stemmer.stem, keyword_words))
        for keyword_stem in keywords_stem:
            if keyword_stem in words_stemmer:
                massive_t_f.append(True)

        if len(massive_t_f) >= len(keyword_words):
            if len(text) > 4096:
                for x in range(0, len(text), 4096):
                    await bot.send_message(chat_id=CHAT_ID, text=send_text[x:x + 4096])
                    return
            else:
                await bot.send_message(chat_id=CHAT_ID, text=send_text)
                return

