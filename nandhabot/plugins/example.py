from telegram.ext import run_async, CommandHandler,MessageHandler
from nandhabot import dispatcher

import random 

OWO = (
    "*Neko pats {} on the head.",
    "*gently rubs {}'s head*.",
    "*Neko mofumofus {}'s head*",
    "*Neko messes up {}'s head*",
    "*Neko intensly rubs {}'s head*",
    "*{}'s waifu pats their head*",
    "*{}'s got free headpats*",
    "No pats for {}!",
)

def waku(update, context):
      msg = update.effective_message
      waku = random.choice(OWO)
      msg.reply_text(waku)

woku = CommandHandler("waku", waku)
dispatcher.add_handler(woku)
