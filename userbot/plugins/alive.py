# For @borgHelp
"""Check if your userbot is working."""
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, telever
from userbot.__init__ import StartTime
from userbot.Config import Var

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
telemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**ℵ**"
if Var.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@blacklightningot"


@borg.on(admin_cmd(outgoing=True, pattern="alive"))
@borg.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = f"**Welcome To 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 **\n\n"
        tele += f"`{CUSTOM_ALIVE}`\n\n"
        tele += (
            f"{telemoji} **Telethon version**: `1.17`\n{telemoji} **Python**: `3.9`\n"
        )
        tele += f"{telemoji} **𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 Version**: `{telever}`\n"
        tele += f"{telemoji} **More Info**: @blacklightningot\n"
        tele += f"{telemoji} **Sudo** : `{sudo}`\n"
        tele += f"{telemoji} **My Creator**: `@krish1303y🔥🔥🔥🔥!`\n"
        tele += f"{telemoji} **Thunder Uptime**: `{uptime}`\n"
        tele += f"{telemoji} **Heroku Database** : `AWS - Working Properly`\n\n"
        tele += f"{telemoji} **License** : [GNU General Public License v3.0](github.com/Anmol-dot283/Black-Lightning/blob/master/LICENSE)\n"
        tele += f"{telemoji} **Copyright** : By [@krih1303y](GitHub.com/Anmol-dot283)\n"
        tele += f"{telemoji} **Database Status**: `All OK 👌!`\n"
        tele += (
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        tele += "    [✨ GitHub Repository ✨](https://github.com/Anmol-dot283/Black-Lightning)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=tele, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/7f72b0ea1893e84028298.mp4")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**Welcome To 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤  **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{telemoji} **Telethon version**: `1.17`\n{telemoji} **Python**: `3.9`\n"
            f"{telemoji} **𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤  Version**: `{telever}`\n"
            f"{telemoji} **More Info**:` @blacklightningot\n"
            f"{telemoji} **Sudo** : `{sudo}`\n"
            f"{telemoji} **Heroku Database** : `AWS - Working Properly`\n\n"
            f"{telemoji} **License** : [GNU General Public License v3.0](github.com/Anmol-dot283/Black-Lightning/blob/master/LICENSE)\n"
            f"{telemoji} **𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤  Uptime**: `{uptime}`\n"
            f"{telemoji} **Database Status**: `All OK 👌!`\n"
            f"{telemoji} **My Creator**: `@krish1303y🔥🔥🔥🔥!`\n"
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/Anmol-dot283/Black-Lightning)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
