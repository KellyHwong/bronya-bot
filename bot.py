#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: onlymyflower
# Date: Feb 19th, 2019

import os
import sys
import nonebot
import config

# import chatbot


def main():
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'bronya', 'plugins'),
        'bronya.plugins'
    )
    nonebot.run()


if __name__ == '__main__':
    main()
