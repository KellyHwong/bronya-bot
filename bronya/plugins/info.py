#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-12-20 07:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import nonebot
from nonebot import on_command, CommandSession


@on_command('info', aliases=("信息"))
async def info(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()
    stripped_arg = session.current_arg_text.strip()

    message = "我是布宝，真正懂你的崩坏3机器人。"

    await session.send(message)
