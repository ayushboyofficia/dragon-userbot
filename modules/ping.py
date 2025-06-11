from pyrogram import Client, filters
from pyrogram.types import Message
import time

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
async def pingme(client: Client, message: Message):
    start = time.time()
    m = await message.reply("🏓 Pinging...")
    end = time.time()
    ping_time = round((end - start) * 1000)
    await m.edit(f"🏓 Pong! `{ping_time} ms`")
