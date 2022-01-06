from asyncpg import Connection
from aiogram import types
from all import dp, bot, db


class DBCommands:
    pool: Connection = db
    KEYWORDS = "SELECT * FROM keywords"
    keyword_id = ''
    DATA = "SELECT * FROM data where keyword_id=%s" % keyword_id


    async def get_keyword(self):
        command = self.KEYWORDS
        return await self.pool.fetchval(command)


db_com = DBCommands()


@dp.message_handler(commands=["start"])
async def get_keywords(message: types.Message):
    keyword = db_com.get_keyword()
    await bot.send_message('done', keyword)
