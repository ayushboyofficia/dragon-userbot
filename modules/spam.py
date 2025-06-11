from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam(client: Client, message: Message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply("Usage: .spam <count> <text>")
        return
    count = int(args[1])
    text = args[2]
    for _ in range(count):
        await message.reply(text)
