from telegram import Bot
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "@oferte_romania_zilnic"

async def main():
    bot = Bot(TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Salut! Botul funcționează! 🎉")

asyncio.run(main())