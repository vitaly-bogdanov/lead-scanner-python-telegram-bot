from aiogram import types


main_menu = types.ReplyKeyboardMarkup(keyboard=[
    [
        types.KeyboardButton(text="Чаты"),
        types.KeyboardButton(text="Ключевые слова")
    ]])


chat_menu = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Добавить", callback_data="add_chat"),
        ],
        [
            types.InlineKeyboardButton(text="Cписок", callback_data="all_chats")
        ]
    ]
)

keyword_menu = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Добавить", callback_data="add_keywords"),
        ],
        [
            types.InlineKeyboardButton(text="Cписок", callback_data="all_keywords")
        ]
    ]
)