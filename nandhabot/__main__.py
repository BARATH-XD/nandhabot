from nandhabot import bot, arq
import logging #aasf
import random
import nandhabot.plugins
from pyrogram import idle
from nandhabot.config import SUPPORT_CHAT
from nandhabot.utils.dbfunctions import clean_restart_stage
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# enable logging
FORMAT = "[VEGETA ROBOT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)

async def start_bot():
    restart_data = await clean_restart_stage()
    x = await arq.wall("vegeta")
    y = x.result
    try:
        print("Sending online status")
        if restart_data:
            await bot.edit_message_media(
                restart_data["chat_id"],
                restart_data["message_id"],
                random.choice(y).url_image,
                caption="**Saiyan Prince Vegeta Successfully Restarted With New Powers**",
            )

        else:
           await bot.send_photo(f"@{SUPPORT_CHAT}", random.choice(y).url_image, caption="**Saiyan Prince Vegeta Was Successfully Deployed!**",
            reply_markup=InlineKeyboardMarkup(
                [
                   [                  
                       InlineKeyboardButton(
                             text="[► Summon Me ◄]",
                             url=f"https://t.me/VegetaRobot?startgroup=true")
                     ] 
                ]
            ),
        ) 
    except Exception as e:
        await bot.send_message("@VegetaSupport", e)
        await idle

if __name__ == "__main__":
   bot.run()
   start_bot()
