from pyrogram import filters
from nandhabot import bot
from pyrogram.types import *
import os

@bot.on_message(filters.command("del"))
async def delete(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not reply:
             await m.reply_text("reply to msg for deleting")
             return 
     if not bot_stats.privileges.can_delete_messages:
               await m.reply_text("**I'm missing the permission of**:\n`can_delete_messages`")
               return 
     if not user_stats.privileges.can_delete_messages:
               await m.reply_text("**your are missing the permission of**:\n`can_delete_messages`")
               return 
     if user_stats.privileges.can_delete_messages:
               await reply.delete()
               await m.delete()

@bot.on_message(filters.command("ban"))
async def banned(_, message):
         if not message.reply_to_message:
                   return await message.reply("Reply to Someone to BAN")
         reply_user = message.reply_to_message.from_user
         from_user = message.from_user
         bot_stats = await bot.get_chat_member(message.chat.id, "self")
         from_user_stats = await bot.get_chat_member(message.chat.id, from_user.id)
         reply_user_stats = await bot.get_chat_member(message.chat.id, reply_user.id)
         if not bot_stats.privileges:
                  return await message.reply("Make Me Admin with (`can_restrict_members`) power!")
         elif not from_user_stats.privileges:
                 return await message.reply("Only Admins Can Use This Commands")
         elif not bot_stats.privileges.can_restrict_members:
                 return await message.reply("Give Me (`can_restrict_members`) Permission")
         elif not from_user_stats.can_restrict_members:
                  return await message.reply("Your missing the rights (`can_restrict_members`)")
         elif reply_user_stats.privileges:
                   return await message.reply("Sorry son I can't ban administrators")
         elif not reply_user_stats.privileges:
                     await bot.ban_chat_member(message.chat.id, reply_user.id)
                     await message.reply_text(f"Admin {from_user.mention} BANNED {reply_user.mention} from {message.chat.title}")
                     return 
                    
@bot.on_message(filters.command(["setgtitle","setchattitle"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     new_title = m.text.split(None, 1)[1]
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not bot_stats.privileges.can_manage_chat:
               await m.reply_text("**I'm missing the permission of**:\n`can_manage_chat`")
               return 
     if not user_stats.privileges.can_manage_chat:
               await m.reply_text("**your are missing the permission of**:\n`can_manage_chat`")
               return 
     if user_stats.privileges.can_manage_chat:
               await m.chat.set_title(new_title)
               await m.reply_text(f"Successfully set {new_title} as new chat title!")

@bot.on_message(filters.command(["setgpic","setchatpic"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not bot_stats.privileges.can_manage_chat:
               await m.reply_text("**I'm missing the permission of**:\n`can_manage_chat`")
               return 
     if not user_stats.privileges.can_manage_chat:
               await m.reply_text("**your are missing the permission of**:\n`can_manage_chat`")
               return 
     if not reply:
                await m.reply_text("reply only document or photo")
                return 
     file = reply.document or reply.photo
     if not file:
               await m.reply_text("reply only document or photo")
               return 
     if user_stats.privileges.can_manage_chat:
               photo = await bot.download_media(file)
               await bot.set_chat_photo(chat.id, photo=photo)
               await m.reply_text("**Successfully group new photo changed!**")

