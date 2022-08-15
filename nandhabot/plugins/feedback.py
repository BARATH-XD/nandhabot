
from nandhabot import bot, dev_user, SUPPORT_CHAT
from pyrogram import filters, enums
import random
from datetime import datetime
from pyrogram.types import *
from nandhabot.config import OWNER_ID

#made by t.me/nandhaxd | t.me/hodackaX

vegeta_img = [ "https://telegra.ph/file/03ba8fea3c3ed2b98b68a.jpg", 
"https://telegra.ph/file/be242e647504b5b253f79.jpg",
"https://telegra.ph/file/51323082ef6051f3a9721.jpg",
"https://telegra.ph/file/072bc7f5f9fdf7f04acb3.jpg"]

@bot.on_message(filters.group & filters.command(["feedback","bug"]))
async def feedback(_, m):
         USER = m.from_user
         if len(m.command) < 2:
               await m.reply_text("**Gime a Feedback!**")
               return
         text = m.text.split(None, 1)[1]
         feedback = "**#NewFeedBack**\n"
         if m.chat:
             feedback += f"**From chat:** `@{m.chat.username}`\n"
         feedback+= f"**user id**: `{USER.id}`\n"
         feedback+= f"**mention**: {USER.mention}\n"
         feedback += f"**Feedback**: `{text}`"
     
         msg = await bot.send_photo(f"@{SUPPORT_CHAT}",random.choice(vegeta_img),caption=feedback,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [    InlineKeyboardButton("Approve ✅", callback_data=f"approve={USER.id}={text}={USER.first_name}"),
                            InlineKeyboardButton("Reject ❌", callback_data=f"reject={USER.id}={text}={USER.first_name}")
                        ],
                    ]
                )
            )
    

         await m.reply_text("Your feedback Successfully Reported On SupportChat!",
                    reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ View Report", url=f"{msg.link}")]]))
  

@bot.on_callback_query(filters.regex("reject"))
async def rejected(_, query: CallbackQuery):
         try:
             mm = query.data.split("=")
             user_id = mm[1]
             text = mm[2]
             name = mm[3]
             if user_id in dev_user and OWNER_ID:
                  await query.edit_message_caption(f"**Feedback:** `{text}` **from** `{name}` | `{user_id}` **is Rejected by {query.from_user.mention} ❌**")
                  await bot.send_message(user_id, f"**Your Feedback:** `{text}` **Has been Rejected by {query.from_user.mention} ❌**")
             else:
                   except Exception as e:
                        await bot.send_message(query.message.chat.id, f"Error: {e}")

@bot.on_callback_query(filters.regex("approve"))
async def approved(_, query: CallbackQuery):
          mm = query.data.split("=")
          user_id = mm[1]
          text = mm[2]
          name = mm[3]
          await query.edit_message_caption(f"**Feedback:** `{text}` **from** `{name}` | `{user_id}` **is Approved by {query.from_user.mention} ✅**")
          await bot.send_message(user_id, f"**Your Feedback:** `{text}` **Has been Approved by {query.from_user.mention} ✅**")
          else:
              await query.answer("Only Rank User Can Approve this Feedback.", show_alert=True)
                                
  
