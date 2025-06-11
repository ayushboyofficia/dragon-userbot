from pyrogram import Client, filters
from pyrogram.types import Message
import random

shayari_list = [
    "Teri muskurahat meri pehchan hai,\nTeri khushi meri jaan hai.",
    "Mere ishq ki koi inteha nahi,\nTu hi mera junoon hai, tu hi meri chahat hai.",
    "Dil se nikli hai dua aapke liye,\nZindagi rahe hamesha aapke liye.",
    # ... aur bhi add kar lo!
]

@Client.on_message(filters.command("shayari", prefixes=".") & filters.me)
async def shayari(client: Client, message: Message):
    await message.reply(random.choice(shayari_list))
