from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Cʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ",              
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(
                text="Cʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="[🇮🇳] Dᴇᴠ", url=f"https://t.me/Queen_xd29"),
            InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ", url=f"https://t.me/+PP2KpZ0kgZE2Y2Jl"),
        ],
        [
            InlineKeyboardButton(text="Iɴᴛʀᴏᴅᴜᴄᴛɪᴏɴ", url=f"https://t.me/+BgELkWdY2nhmZjhl"),
        ],
    ]
    
    return buttons
