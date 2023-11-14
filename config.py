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
SESSION_STRING = getenv("SESSION_STRING", "BAAXQM8EQNN3DZHtSGI-S3ce9K5uCtdMvT4MneOF6SVPqF886P2l_rSsE8X2gws9g-bedupu5Uip9DE3PkPID1x36TvtevsGKu4l5E3EEV2fUL4xtbJaWdVZ1M4wf4aIhdp-Nl6z8M1yc6e3Cwkmgll8YNu3Yfbiwr2aIIgQk6TUveYPLfemlQ335Fys4Z8xNW9QwZNYNKVC5QLPGRJ5zUi0evhK3FfEBnxy2iQdx3Hb_F9QnT09F7eu4faBnw0q0VLyWnI7ILrXxF3U2iBg-sy7psjb3FQOzQVrHH6hyzra7pnIMUfET1f9du0ekyy_uLfHolLLK17Kv8zD2K4Zbw8MAAAAAVEcxxwA")
