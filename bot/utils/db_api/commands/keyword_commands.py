from bot.utils.db_api.schemas.keyword import Keyword


async def add_keyword(word: str):
    keyword = Keyword(word=word)
    await keyword.create()

async def delete_keyword(id: int):
    keyword = await Keyword.get(id)
    await keyword.delete()

async def select_keyword(word):
    keyword = await Keyword.query.where(Keyword.word == word).gino.status()
    return keyword

async def select_all_keywords():
    keywords = await Keyword.query.gino.all()
    return keywords