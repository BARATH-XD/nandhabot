from nandhabot import bot
from pyrogram import filters
from nandhabot.utils.admin_check import *

async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)

@bot.on_message(filters.command("ban"))
async def ban(_, m):
