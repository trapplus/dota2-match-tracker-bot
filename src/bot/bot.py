import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from src import container as cont
from src.bot.handlers.commands import commands_router

dp = Dispatcher()
dp.include_router(commands_router)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello! {message.from_user.full_name}")


async def main() -> None:
    """
    Telegram bot polling start
    """
    bot = Bot(
        token=cont.settings.telegram_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=cont.settings.log_level, stream=sys.stdout)
    asyncio.run(main())
