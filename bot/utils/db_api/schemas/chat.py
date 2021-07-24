from sqlalchemy import Column, BigInteger, String, Boolean, sql, Integer

from bot.utils.db_api.db_gino import db


class Chat(db.Model):
    __tablename__ = "chat"
    number = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(BigInteger, primary_key=True)
    username = Column(String)
    name = Column(String)

    query: sql.Select

