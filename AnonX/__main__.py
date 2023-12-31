import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AnonX import LOGGER, app, userbot
from AnonX.core.call import Anon
from AnonX.plugins import ALL_MODULES
from AnonX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AnonX").error(
            "String Session Not Filled Please A Program Session......"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AnonX").warning(
            " Spotify Id & Secret Not Filled. Don't Warry Not Problem Enjoy Tension Free."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnonX.plugins." + all_module)
    LOGGER("AnonX.plugins").info(
        " Aʟʟ Lᴜᴛᴜʀᴇꜱ Fᴏᴀᴅᴇᴅ Sɪʀ."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_call(
            "https://telegra.ph/file/2e626c10d754a9bad2237.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("AnonX").error(
            "[ERROR] - \n\nHᴇʏ Bᴀʙʜ, Fɪʀsᴛʟʏ Oᴘᴇɴ Tᴇʟᴇɢʀᴀᴍ Aɴᴅ Tᴜʀɴ Oɴ Vᴏɪᴄᴇ Cʜᴀᴛ Iɴ Lᴏɢɢᴇʀ Gʀᴏᴜᴘ ᴇʟsᴇ F*ᴄᴋ Oғғ. Iғ Yᴏᴜ Eᴠᴇʀ Eɴᴅᴇᴅ Vᴏɪᴄᴇ Cʜᴀᴛ Iɴ Lᴏɢ Gʀᴏᴜᴘ I Wɪʟʟ Sᴛᴏᴘ Wᴏʀᴋɪɴɢ Aɴᴅ Usᴇʀs Wɪʟʟ Fᴜ*ᴋ Yᴏᴜ Uᴘ."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("AnonX").info("╔═════ஜ۩۞۩ஜ════╗\n  🌼𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗥𝗬𝗔𝗡🌼\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AnonX").info("Sᴛᴏᴘɪɴɢ Aʀʏᴀɴ Mᴜsɪᴄ Bᴏᴛ...")
    
