from pyrogram import Client, idle
import os
import glob
from pathlib import Path

# Environment variables for your Telegram bot
api_id = int(os.environ.get("API_ID", 123456))  # Replace with your real API_ID
api_hash = os.environ.get("API_HASH", "abcd1234abcd1234abcd1234abcd1234")  # Replace with your API_HASH
bot_token = os.environ.get("BOT_TOKEN", "123456:ABCdefGhIJKlmNoPQRstuVWxyZ")  # Replace with your BOT_TOKEN

# Initialize the Pyrogram Client
app = Client(
    "Dragon-Userbot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins={"root": "plugins"}
)

# Load all plugin files automatically
for plugin in glob.glob("plugins/*.py"):
    name = Path(plugin).stem
    __import__(f"plugins.{name}")

print("🔥 Dragon Userbot started!")
idle()
