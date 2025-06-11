from pyrogram import Client, filters
from pyrogram.types import Message
import random

galis = [
    "Bhai, aap to ultimate bakchod ho!",
    "Chup kar, varna daant tod dunga!",
    "Arre o chutiye, kuch kaam kar le!",
    # ... add more lines
]

@Client.on_message(filters.command("gali", prefixes=".") & filters.me)
async def gali(client: Client, message: Message):
    await message.reply(random.choice(galis))
