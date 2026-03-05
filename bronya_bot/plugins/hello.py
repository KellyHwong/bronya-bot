from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent

# 测试命令：/hello
hello = on_command("hello", priority=5)


@hello.handle()
async def handle_hello(event: MessageEvent):
    await hello.finish(f"你好！{event.sender.nickname}")
