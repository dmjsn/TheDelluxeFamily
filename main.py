import os
import asyncio
from dotenv import load_dotenv
from core import bot

load_dotenv()

async def main():
    try:
        await bot.start(os.getenv('BOT_TOKEN'))
    except KeyboardInterrupt:
        await bot.stop()

if __name__ == '__main__':
    asyncio.run(main())