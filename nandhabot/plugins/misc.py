import os, random , io, time
import requests
from PIL import Image
from pyrogram import filters, enums
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types import Message
from gpytranslate import Translator
from nandhabot import bot, SUPPORT_CHAT, arq
from urllib.parse import quote
import pyshorteners

@bot.on_message(filters.command("shorturl"))
async def short_url(_, message):
             if not message.reply_to_message:
                   return await message.reply("**Reply to URL**")
             elif message.reply_to_message:
                    search = pyshorteners.Shortener()
                    short_url = search.tinyurl.short(message.reply_to_message.text)
                    msg = await message.reply("**Generating URL Process.**")
                    time.sleep(2)
                    await msg.edit(f"**Short URL:**\n{short_url}",disable_web_page_preview=True) #NandhaxD

@bot.on_message(filters.command(["echo","text"]))
async def echo(_, m):
           reply = m.reply_to_message
           text = m.text.split(None, 1)[1]
           if not reply:
                await m.reply_text(text,parse_mode=enums.ParseMode.MARKDOWN,disable_web_page_preview=True)
                await m.delete()
           if reply:
                   await reply.reply_text(text,parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
                   await m.delete()

@bot.on_message(filters.command("spell"))
async def spellcheck(_, m):
      reply = m.reply_to_message
      if not reply:
          return await m.reply_text("reply to text")
      if reply:
          x = await arq.spellcheck(reply.text)
          y = x.result
      text = await m.reply_text("Spelling...")
      await text.edit(f"`{y.corrected}`")

@bot.on_message(filters.command("wall")) 
async def wall(_, m: Message):
       if len(m.command) < 2:
           return await m.reply_text("gime a text Baka!")
       search = m.text.split(None, 1)[1]
       x = await arq.wall(search)
       y = x.result
       await m.reply_photo(random.choice(y).url_image)
       await m.reply_document(random.choice(y).url_image)

@bot.on_message(filters.command("reddit"))
async def reddit(_, m):
          if len(m.command) < 2:
              await m.reply_text("Gime text to search reddit!")
              return 
          text = m.text.split(None, 1)[1]
          search = await arq.reddit(text)
          url = search.result["url"]
          title = search.result["title"]
          postlink = search.result["postLink"]
          await m.reply_photo(url,caption=f"**{title}**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Post Link", url=postlink)]]))

@bot.on_message(filters.command(["lang", "langs"]))
def language(_, m: Message):
       #langs codes
        m.reply_text("Click on the button below to see the list of supported language codes.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Language codes",
                        url="https://telegra.ph/Lang-Codes-03-19-3",
                    ),
                ],
            ],
        ),
    )


trans = Translator()


@bot.on_message(filters.command(["tl", "tr"]))
async def translate(_, message: Message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Reply to a message to translate it!\n Use: /langs for translation codes")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"**Translated from {source} to {dest}**:\n"
        f"`{translation.text}`"
    )

    await message.reply_text(reply)




@bot.on_message(filters.command('json'))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message

    try:
        await message.reply_text(f"<code>{the_real_message}</code>")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove("json.text")
       
       
@bot.on_message(filters.command("ud"))
async def ud(_, message: Message):
        if len(message.command) < 2:
             await message.reply("gime a ward")
             return
        text = message.text.split(None, 1)[1]
        results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
        reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        ud = await message.reply_text("finding.. define.")
        await ud.edit_text(reply_text)

  
def share_link(text: str) -> str:
    return "**Here is Your Sharing Text:**\nhttps://t.me/share/url?url=" + quote(text)

@bot.on_message(filters.command("share"))
async def share_text(_, message: Message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Support Chat", url=f"https://t.me/jacksparrowsupport")
                    ]                
                ]
            ),
        )
        return
    await message.reply_text(share_link(input_text))
