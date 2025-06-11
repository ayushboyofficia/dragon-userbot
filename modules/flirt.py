from pyrogram import Client, filters
from pyrogram.types import Message
import random

flirts = [
    "Are you a magician? Because whenever I look at you, everyone else disappears!",
    "Do you have a map? Because I keep getting lost in your eyes.",
    "If beauty were time, you'd be an eternity.",
    "I must be a snowflake, because I've fallen for you.",
    "Are you a parking ticket? Because you've got FINE written all over you.",
    # ... add more lines
]

@Client.on_message(filters.command("flirt", prefixes=".") & filters.me)
async def flirt(client: Client, message: Message):
    await message.reply(random.choice(flirts))
