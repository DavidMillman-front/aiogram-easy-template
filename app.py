import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from data.config import TOKEN
from data.config import ADMINS

from aiogram.methods.set_my_commands import SetMyCommands

dp = Dispatcher()


# notifiying admins about the start
async def notify_admins(bot):
    for admin in ADMINS:
        await bot.send_message(admin, "started")


# assigning the commands to the bot
async def on_startup(bot):
    commands = [
        {"command": "start", "description": "Start the bot"},
        {"command": "help", "description": "Get help"},
        # Add more commands as needed
    ]
    result: bool = await bot(SetMyCommands(commands=commands))
    print(result)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await notify_admins(bot)
    await on_startup(bot)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
