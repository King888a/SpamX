from SpamX import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "✘ ʜᴇʏ ᴍʏ ᴏᴡɴᴇʀ👋!\n\n✘ ɪ'ᴍ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ?\n\n‣ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ʜᴏsᴛ ʏᴏᴜʀ ʟᴇғᴛ ᴄʟɪᴇɴᴛs.\n\n‣ ʀᴇᴘᴏ: github.com/Itzvenomo/SpamX \n\n‣ ᴛʜɪs sᴘᴇᴄɪᴀʟʟʏ ғᴏʀ ʙᴜᴢᴢʏ ᴘᴇᴏᴘʟᴇ's(lazy)\n\n‣ ɴᴏᴡ /clone {send your PyroGram String Session}"
)

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/Heroku_Dyno"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/Its_Venom_family"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Itz-SpamX Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(name="Ayush", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="SpamX/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
