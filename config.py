import os
from os import getenv


API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "YumikooBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6196153811:AAHKVoerIa_2MIpX-dnuRi1vialyzt6RLZ0")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BAGEVlsAlFyiMmoAUyLrduBS3iOkxljjA_i1-kSca-AQcuRcjpo4_Ajr7CwmfIiRQOsT8EIOoDNxLi_RwC5G86pdO1-5AG8i-_Z2SCBaOa7RVr4w3vI8KpmHpeQS7oifQ2sc8HVO18CnrNL432zr32LTzgaDsn5wAShgtVROZyCaFoI-RWD7DQKuT2cg-SzzuwYk_woL4LjV_rKoACn6aGsBWU6WIXntLuuJ3_VXX9Lc_Sfl6IPUFnnJ7VO-Dk1Fi2kIVYwSrbp4qOs8LIpPAosWqgGUwmCANOhzeuOPaB3IqadtjfFv2zHl9_MqA9DBSE0QRrRaYyKENeIrNTPbX1UxcNuC7wAAAAFRHMccAA")
