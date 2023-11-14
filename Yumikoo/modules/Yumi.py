from lexica import Client
from pyrogram import filters
from Yumikoo import Yumikoo




def main(prompt: str) -> str:
    client = Client()
    response = client.palm(prompt)
    return response["content"].strip()

@Yumikoo.on_message(filters.regex(r"baby|Baby"))
async def deepchat(Yumikoo: Yumikoo, message):
    if message.reply_to_message:
        query = message.text.split(' ', 1)[1]
        x = main(query)
        await message.reply(x)
    else:
        query = message.text.split(' ', 1)[1]
        x = main(query)
        await message.reply(x)
