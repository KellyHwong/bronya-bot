#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2025/06/08 20:54:08
# @Author  : Kelly Hwong
# @Desc    : None

import os


def get_assets_dir():
    return "assets"


def get_stickers_dir():
    return os.path.join(get_assets_dir(), "strickers")
