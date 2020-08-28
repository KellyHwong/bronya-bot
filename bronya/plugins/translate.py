from nonebot import on_command, CommandSession, permission as perm
import nonebot
import os

@on_command('translate', aliases=("翻译", "谷歌翻译"))
async def translate(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()

    stripped_arg = session.current_arg_text.strip()

    from googletrans import Translator
    translator = Translator()

    detected = translator.detect(stripped_arg)
    if detected.lang.find("zh") is not -1: # 是中文
        result = translator.translate(stripped_arg, dest='en').text # 翻译成英文
    else: # 其他，翻译成中文
        result = translator.translate(stripped_arg, dest='zh-cn').text
    print(result)
    message = "翻译结果：" + result + "\nvia https://translate.google.com"
    await session.send(message)
