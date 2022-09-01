from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests 

anews = requests.get("https://api.safone.tech/anime/news").json() 


@bot.on_message(filters.command("anews"))
async def animenews(_, message):
       caption = anews["results"][0]['description']
       img = anews["results"][0]["imageUrl"]
       link = anews["results"][0]["link"]
       title = anews["results"][0]["title"] 
       await message.reply_photo(img,caption=caption,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Source Link", url=link)]]))
