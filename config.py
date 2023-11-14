import os
from os import getenv


API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "YumikooBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6196153811:AAH6Gr18wpnO5gNndm0xvvqEQllLEIyMOp4")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BABiMZkASdPRWt1LvrkiuRVv0hp2qGcjeo4HhFjH8jDnH1jbSMJEkkWa_kDhKkn9pm7ncwBH2QFFq3YBSB9ckeUzC93_8vdiED7FTfmEpS35u_fDDkqlbtRIaBcGlkr2xDSX-3IeaZaYtxzTVfcLbhlHPuIXomM0x34jWC-yGvC7DJi7xQXERErYoBfNzUEAhQMb3k31of6oaBL2h2fme2Jc1SeSL8lH76wvKQgILc9hTh4F7ZmUaufQOADywWs8DNTEyznledk3UiTloAPuVAyJ5Pco7P2rJeJkxI5fbe-hJJG3XnZrze7pj0Iz2xlL2hOXqlo9QuCw6kFKT6PFEK8RhKmoygAAAAFRHMccAA")
