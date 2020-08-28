from nonebot import on_command, CommandSession, permission as perm
import nonebot
import os
import random

DEFAULT_DURATION = 1 * 60


@on_command('lucky_guy', aliases=('幸运星', '随机禁言'), permission=perm.SUPERUSER)
async def lucky_guy(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()

    stripped_arg = session.current_arg_text.strip()

    group_member_list = await bot.get_group_member_list(group_id=722501153)
    # group_member_list = await bot.get_group_member_list(group_id=972862953)
    # print(group_member_list)
    # 随机选择一个成员口球
    rand_index = random.randint(0, len(group_member_list)-1)
    rand_chosen = group_member_list[rand_index]

    await session.send("口球QQ号是 %s，名字叫做 %s（群昵称：%s），口球时间 %s 秒" % (rand_chosen["user_id"], rand_chosen["nickname"], rand_chosen["card"], DEFAULT_DURATION))
    await bot.set_group_ban(group_id=722501153, user_id=rand_chosen["user_id"], duration=DEFAULT_DURATION)
