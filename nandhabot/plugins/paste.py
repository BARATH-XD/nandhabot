from requests import post, get
import requests 
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"



@bot.on_message(filters.command('paste'))
def paste(_, m):
    reply = m.reply_to_message
    if not reply:
           text = m.text.split(None, 1)[1]
           spacebin_url = spacebin(text)
           m.reply_text(spacebin_url,disable_web_page_preview=True)
           return 
    text = reply.text or reply.caption
    if reply:
        spacebin_url = spacebin(text)
        caption = f"[SPACEBIN]({spacebin_url})"
        m.reply(text=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("SPACEBIN", url=spacebin_url)]]),disable_web_page_preview=True)
