import os
from nonebot.default_config import *

# bot profile
BOT_NAME = "布洛妮娅"
COMMAND_START = {'', '/', '!', '／', '！'}

# paths
PROJECT_BRONYA = os.path.dirname(os.path.abspath(__file__))  # 本文件所在目录
ASSETS = os.path.join(PROJECT_BRONYA, "assets")
DATA = os.path.join(PROJECT_BRONYA, "data")

# super users
SUPERUSERS = []  # e.g., 1234567890

# define group ids
MY_GROUP_IDs = []  # e.g., 123456789

BED_TIME = [0, 8]  # 睡觉起始时间，0点到8点

GROUP_TIME_ZONE = {123456789: {"北京": "Asia/Shanghai",
                               "东京": "Asia/Tokyo"},
                   987654321: {"北京": "Asia/Shanghai",
                               "东京": "Asia/Tokyo",
                               "纽约": "America/New_York"}}

# 报时时间设置
GROUP_DAYTIME = {
    123456789: {"daytime": (0, 23)},  # all day long
    987654321: {"daytime": (9, 23)}  # day time
}

# whether -1s every minute
GROUP_MAHA = {123456789: False,
              987654321: True}


def main():
    print(f"PROJECT_BRONYA:{PROJECT_BRONYA}")


if __name__ == "__main__":
    main()
