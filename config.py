import os
from os import getenv


API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "YumikooBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6576720076:AAGQz1tJZF2VLLPMeU2XGoUyntsUKSm2I8U")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BABiMZkAQb_D-2q23_o4-w1RJ9L1x-Kb0_Af0CapApkgxEpIPXK2WKZYjzvYIJOkeCCspPGfntkfxDtKof_lLnRU-90GQ2V33wO9a8NVW356BEzj2Xb8JuRzqqSvT5BOehfp84ZygiKqXkBWu5A6kxiA4c4QjIojUlqDU5w6Xh5DU0oeZPM4yTMiBgHYhv2waXL5PxLAvgSJsSRJGV2QAIKMQ25IIAt0Ne1f-GdTdH_4k2ZP-WxiMSuGGt6rRDjN4LRTM9n3LbvW907fFdScNahgsCnikBSM41y-x2xuRFJE04BaJ7GEV8r5Sd1LPTcK7GcYbosmfv6QRtVFtHc-iyEs1us35QAAAAFRHMccAA")
