import asyncio
import logging
import sys

from src import container as cont 

from src.bot.bot import main

if __name__ == "__main__":
    logging.basicConfig(level=cont.settings.log_level, stream=sys.stdout)
    asyncio.run(main())
