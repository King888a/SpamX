import asyncio
from datetime import datetime
from platform import python_version

from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from config import ALIVE_PIC, ALIVE_TEXT
from SpamX import START_TIME
from SpamX import SUDO_USER
from SpamX.helper.PyroHelpers import ReplyCheck
from SpamX.modules.help import add_command_help
from SpamX.modules.bot.inline import get_readable_time

alive_logo = ALIVE_PIC or "https://telegra.ph/file/17ded061a4ae0833a77b7.jpg"

if ALIVE_TEXT:
   txt = ALIVE_TEXT
else:
    txt = (
        f"**❏ ᴠᴇɴᴏᴍ ᴜsᴇʀʙᴏᴛ**\n\n"
        f"❏ **ᴠᴇʀsɪᴏɴ**: `𝟷.𝟷`\n"
        f"├• **ᴜᴘᴛɪᴍᴇ**: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"├• **ᴘʏᴛʜᴏɴ**: `{python_version()}`\n"
        f"├• **ᴘʏʀᴏɢʀᴀᴍ**: `{__version__}`\n"
        f"├• **sᴜᴘᴘᴏʀᴛ**: [Click](t.me/Its_Venom_family)\n"
        f"├• **ᴄʜᴀɴɴᴇʟ**: [ᴄʟɪᴄᴋ](t.me/Heroku_Dyno)\n"
        f"└• **ʀᴇᴘᴏ**: [ᴄʟɪᴄᴋ](https://GitHub.com/Itzvenomo/SpamX)"        
    )

@Client.on_message(
    filters.command(["alive", "awake"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def alive(client: Client, message: Message):
    xx = await message.reply_text("🔥️")
    try:
       await message.delete()
    except:
       pass
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    xd = (f"{txt}")
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=xd,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(xd, disable_web_page_preview=True)

@Client.on_message(filters.command("repo", ".") & filters.me)
async def repo(bot: Client, message: Message):
    await message.edit("⚡")
    await asyncio.sleep(1)
    await message.edit("ғᴇᴛᴄʜɪɴɢ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.....")
    await asyncio.sleep(1)
    await message.edit("ʜᴇʀᴇ ɪs ʀᴇᴘᴏ: \n\n\nhttps://github.com/Itzvenomo/SpamX\nғᴏʀᴋ & ɢɪᴠᴇ ᴀɴ sᴛᴀʀ ⭐")


@Client.on_message(filters.command("creator", ".") & filters.me)
async def creator(bot: Client, message: Message):
    await message.edit("https://gitHub.com/Itzvenomo")


@Client.on_message(filters.command(["uptime", "up"], ".") & filters.me)
async def uptime(bot: Client, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await message.edit(f"ᴜᴘᴛɪᴍᴇ ☢\n" f"```{str(current_uptime).split('.')[0]}```")


@Client.on_message(filters.command("id", ".") & filters.me)
async def get_id(bot: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.audio.file_id}`"
            file_id += "**ғɪʟᴇ ᴛʏᴘᴇ**: `audio`"

        elif rep.document:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.document.file_id}`"
            file_id += f"**ғɪʟᴇ ᴛʏᴘᴇ**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.photo.file_id}`"
            file_id += "**ғɪʟᴇ ᴛʏᴘᴇ**: `photo`"

        elif rep.sticker:
            file_id = f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**sᴛɪᴄᴋᴇʀ sᴇᴛ**: `{rep.sticker.set_name}`\n"
                file_id += f"**sᴛɪᴄᴋᴇʀ ᴇᴍᴏᴊɪ**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ**: `False`\n"
            else:
                file_id += "**sᴛɪᴄᴋᴇʀ sᴇᴛ**: __None__\n"
                file_id += "**sᴛɪᴄᴋᴇʀ ᴇᴍᴏᴊɪ**: __None__"

        elif rep.video:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.video.file_id}`\n"
            file_id += "**ғɪʟᴇ ᴛʏᴘᴇ**: `video`"

        elif rep.animation:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.animation.file_id}`\n"
            file_id += "**ғɪʟᴇ ᴛʏᴘᴇ**: `GIF`"

        elif rep.voice:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.voice.file_id}`\n"
            file_id += "**ғɪʟᴇ ᴛʏᴘᴇ**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**ғɪʟᴇ ɪᴅ**: `{rep.animation.file_id}`\n"
            file_id += "**ғɪʟᴇ ᴛʏᴘᴇ**: `Video Note`"

        elif rep.location:
            file_id = "**ʟᴏᴄᴀᴛɪᴏɴ**:\n"
            file_id += f"**ʟᴏɴɢɪᴛᴜᴅᴇ**: `{rep.location.longitude}`\n"
            file_id += f"**ʟᴀᴛɪᴛᴜᴅᴇ**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**ʟᴏᴄᴀᴛɪᴏɴ**:\n"
            file_id += f"**ʟᴏɴɢɪᴛᴜᴅᴇ**: `{rep.venue.location.longitude}`\n"
            file_id += f"**ʟᴀᴛɪᴛᴜᴅᴇ**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**ᴀᴅᴅʀᴇss**:\n"
            file_id += f"**ᴛɪᴛʟᴇ**: `{rep.venue.title}`\n"
            file_id += f"**ᴅᴇᴛᴀɪʟᴇᴅ**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**ғᴏʀᴡᴀʀᴅᴇᴅ ᴜsᴇʀ ɪᴅ**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**ᴜsᴇʀ ɪᴅ**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**ғᴏʀᴡᴀʀᴅᴇᴅ ᴜsᴇʀ ɪᴅ**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**ᴜsᴇʀ ɪᴅ**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`")




add_command_help(
    "start",
    [
        [".alive", "Check if the bot is alive or not."],
        [".repo", "Display the repo of this userbot."],
        [".creator", "Show the creator of this userbot."],
        [".id", "Send id of what you replied to."],
        [".up `or` .uptime", "Check bot's current uptime."],
    ],
)

add_command_help(
    "restart",
    [
        [".restart", "You are retarded if you do not know what this does."],
    ],
)
