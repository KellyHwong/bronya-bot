#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019/02/19
# @Author  : Kelly Hwong
# @Desc    : NoneBot2 project with OneBot V11 adapter

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

# 加载内置插件
nonebot.load_builtin_plugins("echo")
# 加载自定义插件
nonebot.load_plugins("bronya_bot/plugins")

if __name__ == "__main__":
    nonebot.run()
