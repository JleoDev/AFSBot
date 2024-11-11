# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.utils import user_validation, error_message_user_without_permission
from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if user_validation(Var.ALLOWED_USERS, m.from_user.id, m.from_user.username):
        return await m.reply(
            error_message_user_without_permission(),
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.'
    )
