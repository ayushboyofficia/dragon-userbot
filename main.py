from pyrogram import Client
import os
from modules import *  # will import all handlers

app = Client(
    "userbot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    session_string=os.getenv("SESSION_STRING")
)

# dynamic import to register handlers
import pkgutil, modules
for _, modname, _ in pkgutil.iter_modules(modules.__path__):
    __import__(f"modules.{modname}")

if __name__ == "__main__":
    app.run()
