#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-05-19 18:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

from nonebot import on_command, CommandSession, permission as perm
import nonebot
import os
import random

song_list = ["cyberangel-segment1.m4a"]


@on_command('sing', aliases=('唱歌', '唱首歌'))
async def sing(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()
    filename = song_list[0]  # TODO more songs
    stripped_arg = session.current_arg_text.strip()
    file_relpath = os.path.join("./assets/songs", filename)
    file_abspath = os.path.abspath(file_relpath)
    message = r"[CQ:record,file=file:///{}]".format(file_abspath)

    print(file_abspath)

    await session.send(message)
