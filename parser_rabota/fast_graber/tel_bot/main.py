from aiogram import executor

from all import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    await bot.send_message("Я запущен!")


if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
