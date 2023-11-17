import os
from os import getenv


API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "YumikooBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6196153811:AAGJrIbRqCQZgAuSinxZEs9orNMCqg2Pmp8")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BABiMZkAbe5o0nxPRivuf7xl0MU35q7XFPsMDcylv3I52WZyA4jjmZ7YrcyD_Wo3NGcCZ3nltdcb5SCAim-6LJ1rrQ9rPuEtLwlEwRihToKYkTFW9FZjCcdA7flVrtk9dQPpnDIWI_6ZaEQn1QhfI-SlBOiuYJ1ucoEQF2vOj1blvratq9-JGEtYDr8eA7o1Q3_neX82fDBAiBruh11ed6KpWiBgtKm9NERUZPvhvWbhSyODnI1QLbKx9Rd9wjn4CpS27TayfxgFQCHfpYAeLFAYGm0I6LPGYc6i0E1OOpD5Aq8cz-VYIJZylSu5kDf-m1quGBCBOxsQ9GObyxmmdDym0ZvMMQAAAAFRHMccAA")
