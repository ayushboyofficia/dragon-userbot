from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("tagall", prefixes=".") & filters.me)
async def tagall(client: Client, message: Message):
    chat = message.chat
    users = []
    async for m in client.get_chat_members(chat.id):
        users.append(m.user.mention)
    text = " ".join(users)
    await message.reply(text)
