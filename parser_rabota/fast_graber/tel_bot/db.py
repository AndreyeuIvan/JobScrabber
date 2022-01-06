import asyncio
import asyncpg

from decouple import config


async def create_pool():
    return await asyncpg.create_pool(
        database=config('DB_NAME'),
        user=config('DB_USER'),
        host=config('DB_HOST')
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
