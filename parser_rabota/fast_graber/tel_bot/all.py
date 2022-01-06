from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

from db import create_pool


storage = MemoryStorage()
bot = Bot(token=config("TOKEN"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
db = dp.loop.run_until_complete(create_pool())
