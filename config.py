import os
from os import getenv


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_USERNAME = getenv("BOT_USERNAME", "YumikooBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "")
SESSION_STRING = getenv("SESSION_STRING", "")
