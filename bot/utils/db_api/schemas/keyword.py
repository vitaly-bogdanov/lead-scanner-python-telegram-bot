from sqlalchemy import Column, sql, Integer, String

from bot.utils.db_api.db_gino import db


class Keyword(db.Model):
    __tablename__ = "keyword"
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String(400))

    query: sql.Select