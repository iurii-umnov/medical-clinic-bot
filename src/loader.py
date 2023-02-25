from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from .data.config import DB_HOST, REDIS_PORT, TOKEN
from .data import core

bot = Bot(token=TOKEN)
storage = RedisStorage2(
    host=DB_HOST,
    port=REDIS_PORT,
    pool_size=1000
)
dp = Dispatcher(
    bot=bot,
    storage=storage,
    loop=core.loop
)
