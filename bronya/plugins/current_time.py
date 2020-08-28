#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-12-20 00:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org


from datetime import datetime
import pytz
import nonebot
from nonebot import on_command, CommandSession


@on_command('time', aliases=("时间"))
async def current_time(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()
    stripped_arg = session.current_arg_text.strip()

    tz_name, time_zone = '北京', 'Asia/Shanghai'
    now = datetime.now(pytz.timezone(time_zone))
    message = f"现在{tz_name}时间{now.hour}点整啦！"

    await session.send(message)
