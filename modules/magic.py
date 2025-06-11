from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

@Client.on_message(filters.command("magic", prefixes=".") & filters.me)
async def magic(client: Client, message: Message):
    msg = await message.reply("🔮 Magic is happening...")
    await asyncio.sleep(1)
    await msg.edit("✨✨✨ Abracadabra! ✨✨✨")
