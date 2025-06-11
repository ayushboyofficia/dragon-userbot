from pyrogram import Client
import os
import glob
import importlib

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("STRING_SESSION", "")

app = Client(
    name="Dragon-Userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

# Load all plugins dynamically
plugin_files = glob.glob("plugins/*.py")
for plugin in plugin_files:
    module_name = plugin.replace("/", ".").rstrip(".py")
    importlib.import_module(module_name)

print("🔥 Dragon-Userbot (Userbot Mode) is online!")
app.run()
