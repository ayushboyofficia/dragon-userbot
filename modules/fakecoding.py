from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

@Client.on_message(filters.command("fakecoding", prefixes=".") & filters.me)
async def fake_coding(client: Client, message: Message):
    text = "Compiling...\n"
    for i in range(1, 101):
        await message.edit(text + f"{i}% done")
        await asyncio.sleep(0.05)
    await message.edit("✅ Code compiled successfully!")
