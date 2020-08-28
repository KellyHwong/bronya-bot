import os
import nonebot
from nonebot import on_command, CommandSession, permission as perm
from config import ASSETS


@on_command('help', aliases=('帮助', '怎么用'))
async def persecute(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()
    stripped_arg = session.current_arg_text.strip()

    filename = "help.png"
    filepath = os.path.join(ASSETS, filename)
    message = f"[CQ:image,file=file:///{filepath}]"
    await session.send(message)
