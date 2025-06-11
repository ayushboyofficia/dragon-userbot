import os, asyncio, glob, importlib
from pyrogram import Client, idle

app = Client(
    "dragon_userbot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["STRING_SESSION"]
)

# Load all plugin files
for file in glob.glob("modules/*.py"):
    importlib.import_module(file.replace("/", ".")[:-3])

print("🐉 Dragon-Userbot (Userbot Mode) is live!")
app.start()
idle()
app.stop()
