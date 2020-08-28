#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-30-20 12:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import nonebot
from nonebot import on_command, CommandSession

from datetime import datetime
import pytz

from aiocqhttp.exceptions import Error as CQHttpError
from config import ASSETS, BOT_NAME, MY_GROUP_IDs


@on_command('abyss', aliases=("深渊"))
async def abyss(session: CommandSession):
    """深渊鸭宝，您的深渊催肝砖家
    """
    message = "我是鸭宝，真正懂你的崩坏3机器人，您的深渊催肝砖家。"

    bot = session.bot
    bot = nonebot.get_bot()
    stripped_arg = session.current_arg_text.strip()

    if "哪个区" in stripped_arg:
        message = "降级区"
        await session.send(message)

# 鸭宝，您的深渊催肝砖家


@nonebot.scheduler.scheduled_job('cron', day_of_week="mon,fri", hour="14-15", minute=0, second=0)
async def abyss_begin_reminder():
    """深渊开始提醒
    """
    bot = nonebot.get_bot()
    china_now = datetime.now(pytz.timezone('Asia/Shanghai'))

    message = ""
    if china_now.hour == 14:
        message = f"{BOT_NAME}提醒舰长们，深渊还有{15-china_now.hour}个小时开始~"
    elif china_now.hour == 15:
        message = f"{BOT_NAME}提醒舰长们本轮深渊开始啦~"

    if message != "":
        for group_id in MY_GROUP_IDs:
            try:
                await bot.send_group_msg(group_id=group_id, message=message)
            except CQHttpError:
                pass


@nonebot.scheduler.scheduled_job('cron', hour="8,12", minute=0, second=0)
async def abyss_daily_reminder():
    """深渊日常提醒，每天早上8点触发一次，半夜12点睡觉提醒一次 # TODO
    """
    bot = nonebot.get_bot()
    china_now = datetime.now(pytz.timezone('Asia/Shanghai'))

    message = ""
    if china_now.hour == 8:
        if china_now.weekday+1 == 1 or 5:
            message = f"{BOT_NAME}提醒舰长们深渊还有{15-china_now.hour}个小时开始~"
        elif china_now.weekday+1 == 2 or 3 or 6 or 7:
            message = f"{BOT_NAME}提醒舰长们今天深渊进行中~"
    elif china_now.hour == 0:
        # TODO
        pass

    if message != "":
        for group_id in MY_GROUP_IDs:
            try:
                await bot.send_group_msg(group_id=group_id, message=message)
            except CQHttpError:
                pass


@nonebot.scheduler.scheduled_job('cron', day_of_week="wed,sun", hour="18-22", minute=0, second=0)
async def abyss_end_reminder():
    bot = nonebot.get_bot()
    china_now = datetime.now(pytz.timezone('Asia/Shanghai'))

    message = ""

    if china_now.hour == 18:
        filename = "stickers/今晚深渊结算.jpg"
        filepath = os.path.join(ASSETS, filename)
        message = f"[CQ:image,file=file:///{filepath}]"
        for group_id in MY_GROUP_IDs:
            try:
                await bot.send_group_msg(group_id=group_id, message=message)
            except CQHttpError:
                pass

    if china_now.hour in range(18, 22):
        message = f"{BOT_NAME}提醒舰长们，深渊还有{22-china_now.hour}个小时就要结算啦！"
    elif china_now.hour == 22:
        message = f"{BOT_NAME}提醒舰长们，深渊开始结算啦！"

    if message != "":
        for group_id in MY_GROUP_IDs:
            try:
                await bot.send_group_msg(group_id=group_id, message=message)
            except CQHttpError:
                pass


# 活动
# @nonebot.scheduler.scheduled_job('cron', hour="10-23,0", minute=0, second=0)
# async def activity_three_kingdoms_reminder():
#     """鸭宝，您的活动催肝砖家
#     """
#     bot = nonebot.get_bot()
#     china_now = datetime.now(pytz.timezone('Asia/Shanghai'))

#     activity_name = "崩坏国记"
#     message = ""
#     if china_now.hour == 10:  # begin
#         message = f"{BOT_NAME}提醒舰长们，{activity_name}活动开始啦！"
#     elif china_now.hour in range(18, 24):
#         message = f"{BOT_NAME}提醒舰长们，{activity_name}活动还有{24-china_now.hour}个小时~"
#     elif china_now.hour == 0:
#         message = f"{BOT_NAME}提醒舰长们，今天的{activity_name}活动结束啦！"

#     if message != "":
#         for group_id in MY_GROUP_IDs:
#             try:
#                 await bot.send_group_msg(group_id=group_id, message=message)
#             except CQHttpError:
#                 pass
